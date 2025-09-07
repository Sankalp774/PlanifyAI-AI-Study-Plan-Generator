# PlanifyAI-AI-Study-Plan-Generator-With-Gradio
An AI Study Plan Generator with Email Scheduling

An AI-powered study planner built for Google Colab with a Gradio interface.

Upload a document (PDF, DOCX, PPTX, or TXT), and the app will:

✅ Extract the content

✅ Summarize the document

✅ Generate a personalized, multi-day study plan

✅ Suggest practice questions for active recall

✅ Email the study plan at 5 PM in your timezone

✅ Save study plans directly to Google Drive

🚀 Features

Multi-format support: Works with PDF, DOCX, PPTX, and TXT files
AI-powered summarization: Uses facebook/bart-large-cnn
Question generation: Powered by google/flan-t5-large
Custom study plans: Distributes content over 1–14 days
Email scheduling: Sends study plans at 5 PM (per-user timezone)
Google Drive integration: Save study plans automatically
Demo mode: Try it with sample content (Machine Learning example)

🛠 Installation (Google Colab)
Open the notebook in Google Colab and run the setup cells:

!pip install transformers PyMuPDF python-docx python-pptx scikit-learn spacy apscheduler pytz gradio
!python -m spacy download en_core_web_sm

📖 Usage

1. Upload Document
Supported formats: PDF, DOCX, PPTX, TXT

2. Generate Study Plan

Choose the number of study days (1–14)
View structured plan with daily topics

3. Generate Questions

Select or enter a topic
Generate 1–10 practice questions

4. Email Setup

Enter your email & password
Gmail users must use an App Password

5. Email & Save

Schedule Emails: Automatically delivered at 5 PM in your timezone

Send Now: Instant email delivery

Save to Drive: Save study plans as .txt files

📸 Interface (Gradio)

Tab 1 – Upload: Upload your study material or load demo content

<img width="1680" height="1021" alt="Screenshot 2025-09-07 140043" src="https://github.com/user-attachments/assets/44755097-24dc-4564-ad4b-41cf29044001" />


Tab 2 – Study Plan: Generate summary, study plan, and questions

<img width="1671" height="941" alt="Screenshot 2025-09-07 140255" src="https://github.com/user-attachments/assets/2b36883d-f034-4584-a80e-9c3b3000c5aa" />


Tab 3 – Email Setup: Configure email & register users

<img width="1557" height="714" alt="Screenshot 2025-09-07 140733" src="https://github.com/user-attachments/assets/f4738da8-2f87-4c1c-bb3f-61dbb9fd9be2" />

Tab 4 – Send & Save: Schedule emails or save plans to Google Drive

<img width="1552" height="718" alt="Screenshot 2025-09-07 140812" src="https://github.com/user-attachments/assets/c35778c5-a420-4be2-a3f0-530a8d467450" />


📂 Project Structure

📁 AI-Study-Plan-Generator
│── app.py                 # Main Colab script with Gradio interface
│── user_database.json      # Stores registered users & preferences
│── requirements.txt        # Required Python dependencies
│── README.md               # Project documentation

📬 Email Configuration

Uses SMTP (Gmail by default)

Credentials stored temporarily in memory

Emails formatted with HTML for readability

⚠ Important for Gmail users:

You cannot use your regular password. Generate an App Password from your Google account security settings.

📅 Scheduling

Emails are scheduled with APScheduler

Study plans delivered daily at 5 PM local time (per user’s timezone)

Runs in the background until the Colab session ends

🧪 Demo Mode

No file? No problem!

Load Machine Learning sample content with one click

Instantly test summarization, planning, and questions

🛡 Limitations

Requires Colab runtime to remain active for scheduled emails

Email credentials are session-based (not stored permanently)

Heavy documents may take longer to process

🤝 Contributing

Pull requests and feature suggestions are welcome!

Possible future improvements:

Export plans to PDF/Word

Add support for cloud storage APIs

Improve question generation with more advanced models

📜 License

MIT License. Free to use and modify.

🌟 Acknowledgements

Hugging Face Transformers

Gradio

spaCy

APScheduler
