# PlanifyAI — AI Study Plan Generator

**Applied NLP product**: turn course material into a structured multi-day study plan with active-recall questions.

```text
PDF/DOCX/PPTX/TXT
  → ingest
  → BART summary (or extractive light mode)
  → day-wise topic allocation
  → FLAN-T5 practice questions
  → Markdown / JSON / Gradio UI
```

Originally a Colab notebook — now a **installable Python package** with CLI, tests, and light mode for offline demos.

## Why it's portfolio-grade

| Signal | Where |
|--------|-------|
| Multi-format ingestion | `planify/ingest.py` |
| Modular planner engine | `planify/planner.py` |
| Light mode (no GPU/weights) | `PLANIFY_LIGHT=1` / `--light` |
| CLI + Gradio dual interface | `planify/cli.py`, `planify/app.py` |
| Unit tests without HF downloads | `tests/test_planner_light.py` |
| Sample curriculum notes | `samples/ml_notes.txt` |

## Quickstart

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Light mode (instant, no model download)
python -m planify.cli samples/ml_notes.txt --days 5 --light

# Full generative mode
python -m planify.cli samples/ml_notes.txt --days 7

# UI
PLANIFY_LIGHT=1 python -m planify.app

# Tests
pytest tests/ -q
```

## Package layout

```text
planify/
  ingest.py
  planner.py
  app.py
  cli.py
samples/
tests/
PlanifyAI.ipynb   # original Colab research notebook
```

## Models

| Task | Default |
|------|---------|
| Summarization | `facebook/bart-large-cnn` |
| Question gen | `google/flan-t5-base` |

## Limitations

- Plans are heuristic topic allocation + generative assist, not a full adaptive tutor  
- Email/Drive scheduling remains Colab-era; core value is the planner package  
- Large PDFs should be chunked; light mode recommended for demos  

## Author

Sankalp Sahu — Applied AI portfolio
