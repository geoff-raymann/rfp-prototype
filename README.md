🚦 Safaricom ESP Onboarding Prototype
This is a proof-of-concept Streamlit app that showcases how Safaricom’s vendor onboarding process can be automated with AI, OCR, and staged validations to cut onboarding from 12 weeks to 3 weeks.

✅ Features
📑 Technical Response Scoring — AI-powered NLP scoring (BERT-based).

📄 Certifications Verification — Mock database check.

🚗 Logbook Verification — OCR placeholder.

🏠 Site Visit Evidence — Prototype text input for notes.

✅ Staged Workflow — Must complete one step to move to the next.

🎯 Final Review & Score

📌 How to run locally
bash
Copy
Edit
# Clone the repo
git clone https://github.com/your-org/esp_onboarding_prod.git
cd esp_onboarding_prod

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
🚀 Deploy on Streamlit Community Cloud
✅ 1️⃣ Push this repo to GitHub
Include:

app.py

modules/ folder

requirements.txt

This README.md

✅ 2️⃣ Sign up or log in at Streamlit Community Cloud
✅ 3️⃣ Click ‘New app’, link your GitHub repo
Pick branch (e.g., main)

app.py as entry point

✅ 4️⃣ Click Deploy
✅ Your app will be live at:

cpp
Copy
Edit
https://<your-app-name>.streamlit.app
Share this link with stakeholders for testing!

⚡ Limitations on Streamlit Cloud
OCR (pytesseract) may not work because Tesseract binary is not installed.
👉 Use placeholder inputs or mock data for now.

PDF export with pdfkit may not work (no wkhtmltopdf binary).
👉 Show final scores on-screen instead.

This version uses session_state — no database for now.

✅ Good enough to prove the concept!

🔒 Security Note
This is a prototype only — do not upload real vendor data.
For production, use:

Proper authentication.

PostgreSQL for storing final results.

PDF reports, S3 storage, and email notifications.

A containerized setup with a secured cloud server.

🟢 Requirements
requirements.txt:

php
Copy
Edit
streamlit
torch
transformers
Pillow
pytesseract  # Optional, works only if Tesseract is installed
PyYAML
psycopg2-binary
✅ Remove pdfkit if not needed for Streamlit Cloud.

🎉 Who to contact
For questions or support on this prototype:
Safaricom Enterprise Service Partner (ESP) Onboarding Team

Done!
Your prototype is ready to test & share with your team.
✅ Reduce onboarding delays
✅ Cut costs
✅ Protect customer SLAs

🔗 Next Steps
If you want to:

Deploy on your own server with OCR & PDF fully working

Add authentication & real DB storage

Connect to vendor APIs

… just run docker compose build && docker compose up with your full production image!

Built with ❤️ by your RFP Ideation Team.