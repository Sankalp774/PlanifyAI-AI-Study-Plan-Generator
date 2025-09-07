# PlanifyAI-AI-Study-Plan-Generator-With-Gradio
Automated study planner leveraging AI summarization, document ingestion, and email scheduling. Built with Python, Gradio, and Google Colab compatibility.


Features
📄 Upload PDFs, DOCX, PPTX, or TXT files

🧠 Extracts & summarizes key concepts using advanced NLP

🗓️ Creates a customizable study plan (1-14 days)

❓ Generates context-aware practice questions per topic

🕔 Schedules end-of-day study plan emails per user/timezone

📩 One-click instant emailing

💾 Google Drive study plan export

⚡ Clean, interactive Gradio web interface

Demo
Tech Stack
Python 3.x
Gradio (UI)
Hugging Face Transformers (NLP/summarization, QG)
spaCy (NLP)
PyMuPDF, python-docx, python-pptx (file parsing)
scikit-learn (question deduplication)
Apscheduler, smtplib, pytz (email scheduling)
Google Colab & Drive integration

#Installation
bash
pip install transformers PyMuPDF python-docx python-pptx scikit-learn spacy apscheduler pytz gradio
python -m spacy download en_core_web_sm
Or open in Google Colab for an instant, dependency-free setup.

#Usage
Upload a study document in supported format.

Set study plan parameters (days, topics).

Generate summary and plan; optionally produce practice questions.

Register email/info for scheduled notifications.

Export the plan, send immediate/scheduled emails, or save to Google Drive.

Email Setup
Uses SMTP (supports Gmail App Passwords; see instructions)

Contribution
Contributions and PRs welcome!
Please open an issue for feature requests or bug reports.
