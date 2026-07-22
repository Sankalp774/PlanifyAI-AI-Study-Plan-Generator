"""Gradio UI for PlanifyAI."""

from __future__ import annotations

import tempfile
from pathlib import Path

import gradio as gr

from planify.ingest import extract_text
from planify.planner import PlanifyEngine

# Default to models on; set PLANIFY_LIGHT=1 for extractive-only demos
import os

LIGHT = os.environ.get("PLANIFY_LIGHT", "0") == "1"
ENGINE = PlanifyEngine(use_models=not LIGHT)


def run(file, days: int, minutes: int, light: bool):
    if file is None:
        return "Upload a document first.", ""
    path = file.name if hasattr(file, "name") else str(file)
    text = extract_text(path)
    engine = PlanifyEngine(use_models=not light)
    plan = engine.build_plan(text, num_days=int(days), minutes_per_day=int(minutes))
    return plan.to_markdown(), plan.to_dict()


def build() -> gr.Blocks:
    with gr.Blocks(title="PlanifyAI") as demo:
        gr.Markdown(
            """
# PlanifyAI — Document → Study Plan
Ingest notes/slides → summarize → multi-day plan → active-recall questions.

Set `PLANIFY_LIGHT=1` for CPU-only extractive mode without downloading transformers.
"""
        )
        f = gr.File(label="PDF / DOCX / PPTX / TXT", file_types=[".pdf", ".docx", ".pptx", ".txt"])
        days = gr.Slider(1, 14, value=5, step=1, label="Study days")
        minutes = gr.Slider(20, 180, value=60, step=10, label="Minutes / day")
        light = gr.Checkbox(value=LIGHT, label="Light mode (no HF models)")
        btn = gr.Button("Generate plan", variant="primary")
        md = gr.Markdown()
        raw = gr.JSON()
        btn.click(fn=run, inputs=[f, days, minutes, light], outputs=[md, raw])
    return demo


if __name__ == "__main__":
    build().launch()
