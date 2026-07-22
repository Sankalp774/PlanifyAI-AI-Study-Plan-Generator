# PlanifyAI — AI Study Plan Generator

Google Colab + Gradio app that turns course material into a **multi-day study plan**.

Upload PDF / DOCX / PPTX / TXT → extract → summarize → plan days → practice questions → optional email / Drive save.

## Pipeline

```text
Document → text extraction → BART summary → day-wise plan → FLAN-T5 questions
                ↘ optional: email at 5 PM (timezone-aware) + Google Drive
```

## Models

| Task | Model |
|------|--------|
| Summarization | `facebook/bart-large-cnn` |
| Question generation | `google/flan-t5-large` |

## Features

- Multi-format document ingest  
- Personalized plans for **1–14 days**  
- Practice questions for active recall  
- Email scheduling (Gmail **App Password** required)  
- Optional Google Drive save (Colab)  
- Demo mode with sample ML content  

## Run (Google Colab)

1. Open [`PlanifyAI.ipynb`](PlanifyAI.ipynb) in Colab  
2. Run setup cells:

```python
!pip install transformers PyMuPDF python-docx python-pptx scikit-learn spacy apscheduler pytz gradio
!python -m spacy download en_core_web_sm
```

3. Run the remaining cells and use the Gradio UI  

## Local notes

This project is **notebook-first** (Colab). Heavy models need GPU or patience on CPU.  
For a production study tool, extract the notebook into a FastAPI + worker service (future work).

## What I built

- Document multi-format ingestion for study workflows  
- Generative summarization + QG chained into a planner UX  
- Scheduling + Drive integration experiments in Colab  

## Limitations

- Colab session / secret management for email  
- Not a full LMS; plans are heuristic + generative  
- Large models may OOM on free runtimes — reduce plan length or use smaller checkpoints  

## License

See `LICENSE`.
