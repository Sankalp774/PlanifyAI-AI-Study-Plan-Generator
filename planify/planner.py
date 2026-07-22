"""Summarization, study plan construction, and question generation."""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class StudyDay:
    day: int
    focus: str
    topics: list[str]
    estimated_minutes: int


@dataclass
class StudyPlan:
    title: str
    summary: str
    days: list[StudyDay]
    questions: list[str] = field(default_factory=list)
    source_chars: int = 0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def to_markdown(self) -> str:
        lines = [f"# {self.title}", "", "## Summary", self.summary, "", "## Schedule"]
        for d in self.days:
            lines.append(
                f"### Day {d.day} — {d.focus} (~{d.estimated_minutes} min)\n"
                + "\n".join(f"- {t}" for t in d.topics)
            )
        if self.questions:
            lines.append("\n## Practice questions")
            lines.extend(f"{i}. {q}" for i, q in enumerate(self.questions, 1))
        return "\n\n".join(lines)


class PlanifyEngine:
    def __init__(
        self,
        summarizer_model: str = "facebook/bart-large-cnn",
        qg_model: str = "google/flan-t5-base",
        use_models: bool = True,
    ):
        self.use_models = use_models
        self.summarizer_model = summarizer_model
        self.qg_model = qg_model
        self._summarizer = None
        self._qg = None

    def _load(self) -> None:
        if not self.use_models or self._summarizer is not None:
            return
        from transformers import pipeline

        self._summarizer = pipeline("summarization", model=self.summarizer_model)
        self._qg = pipeline("text2text-generation", model=self.qg_model)

    def summarize(self, text: str, max_chunk: int = 900) -> str:
        text = text.strip()
        if not text:
            return ""
        if not self.use_models:
            # extractive fallback: first sentences
            sents = re.split(r"(?<=[.!?])\s+", text)
            return " ".join(sents[:5])[:800]

        self._load()
        chunks = [text[i : i + max_chunk] for i in range(0, min(len(text), max_chunk * 4), max_chunk)]
        outs = []
        for ch in chunks:
            outs.append(
                self._summarizer(ch, max_length=120, min_length=30, do_sample=False)[0][
                    "summary_text"
                ]
            )
        return "\n".join(outs)

    def build_plan(self, text: str, num_days: int = 5, minutes_per_day: int = 60) -> StudyPlan:
        num_days = max(1, min(14, int(num_days)))
        summary = self.summarize(text)
        # topic chunks by paragraph
        paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
        if not paras:
            paras = [text[i : i + 400] for i in range(0, len(text), 400)] or ["General review"]

        days: list[StudyDay] = []
        for d in range(num_days):
            # round-robin paragraphs into days
            assigned = [paras[i] for i in range(d, len(paras), num_days)][:4]
            if not assigned:
                assigned = [paras[d % len(paras)][:200]]
            topics = [a.replace("\n", " ")[:160] for a in assigned]
            days.append(
                StudyDay(
                    day=d + 1,
                    focus=f"Block {d + 1}",
                    topics=topics,
                    estimated_minutes=minutes_per_day,
                )
            )

        questions = self.generate_questions(summary or text[:1000], n=min(5, num_days + 1))
        title = "Study Plan"
        first_line = text.strip().splitlines()[0][:80] if text.strip() else title
        if len(first_line) > 12:
            title = f"Study Plan: {first_line}"

        return StudyPlan(
            title=title,
            summary=summary,
            days=days,
            questions=questions,
            source_chars=len(text),
        )

    def generate_questions(self, context: str, n: int = 5) -> list[str]:
        if not self.use_models:
            return [
                f"Explain the key idea in your own words (topic {i+1})."
                for i in range(n)
            ]
        self._load()
        prompt = (
            f"Generate {n} short study questions for active recall based on:\n{context[:1200]}"
        )
        out = self._qg(prompt, max_length=256, do_sample=False)[0]["generated_text"]
        lines = [ln.strip(" -•\t") for ln in out.splitlines() if ln.strip()]
        if len(lines) < n:
            lines = re.split(r"\d+\.\s+", out)
            lines = [ln.strip() for ln in lines if ln.strip()]
        return lines[:n] or [out.strip()]
