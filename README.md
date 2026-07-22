# PlanifyAI — AI Study Plan Generator

> **Academic stage:** **3rd / 4th year** Applied AI · **Created:** September 2025  
> **Learning focus:** Multi-format ingest · summarization pipelines · study-plan heuristics · question generation · packaging notebooks into CLI/UI modules · light vs generative modes

## About

Turn notes/slides into a multi-day study plan with practice questions.

```text
Document → ingest → summary → day allocation → active-recall questions
```

## What I learned

| Topic | How this project taught it |
|-------|----------------------------|
| Document AI | PDF/DOCX/PPTX/TXT extraction |
| LLM/NLP apps | BART + FLAN-T5 (full mode) |
| Product design | Light mode without GPU/weights |
| Software packaging | `planify/` package, CLI, Gradio |
| Testing | Unit tests for light planner |

## Quickstart

```bash
pip install -r requirements.txt
python -m planify.cli samples/ml_notes.txt --days 5 --light
PLANIFY_LIGHT=1 python -m planify.app
pytest tests/ -q
```

## Author

Sankalp Sahu
