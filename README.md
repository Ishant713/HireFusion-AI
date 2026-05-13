# 📄 HireFusion AI – Resume Analyzer & AI Interview Bot

An AI-powered web application designed to help students and job seekers improve their resumes and prepare for interviews using Google Gemini AI. The platform analyzes uploaded resumes, generates ATS-style feedback, and provides an interactive AI Interview Bot for real-time interview practice.

---

## 🚀 Live Demo

👉 https://hirefusion-ai-flw8amhq963qbwgcrgsi2t.streamlit.app/

---

## 📌 Overview

HireFusion AI uses Google's Gemini AI model to perform intelligent resume analysis and interview simulation.

Users can upload their resumes in PDF format and receive:

* Resume analysis & ATS feedback
* Skill gap identification
* Personalized interview questions
* AI-based answer evaluation
* Real-time interview practice

The application is designed to simulate a realistic interview preparation environment.

---

## ✨ Features

* 📄 Upload PDF resumes
* 🤖 AI-powered resume analysis
* 📊 ATS score & resume feedback
* 🧠 Skill gap detection
* 💼 Personalized HR interview questions
* 👨‍💻 Technical interview question generation
* 🎤 Interactive AI Interview Bot
* 📈 Real-time answer evaluation & scoring
* 📥 Downloadable analysis report
* 🌐 Interactive UI built with Streamlit

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini AI
* PyPDF2
* python-dotenv

---

## ⚙️ How It Works

1. User uploads a resume in PDF format
2. Resume text is extracted using PyPDF2
3. Gemini AI analyzes the resume
4. ATS-style feedback and suggestions are generated
5. AI Interview Bot asks role-specific questions
6. User submits answers
7. Gemini AI evaluates responses and provides feedback

---

## 📦 Installation (Local Setup)

```bash
git clone https://github.com/your-username/hirefusion-ai.git

cd hirefusion-ai

pip install -r requirements.txt

streamlit run app.py
```

---

## 📁 Project Structure

```bash
app.py                # Main Streamlit application
requirements.txt      # Python dependencies
.env                  # Gemini API key (local only)
.gitignore            # Ignore sensitive files
README.md             # Project documentation
```

---

## 🔐 Environment Variables

Create a `.env` file locally:

```env
GEMINI_API_KEY=your_api_key
```

For Streamlit Cloud deployment, add the API key inside:

```text
Settings → Secrets
```

---

## ⚠️ Disclaimer

This application is intended for educational and career preparation purposes only. AI-generated feedback may not always fully reflect real-world recruitment standards.

---

## 🎯 Future Improvements

* 📄 Resume-job description matching
* 🎙️ Voice-based AI interviews
* 📊 Advanced ATS scoring system
* 🔐 User authentication system
* 📚 Resume templates & optimization
* 🌍 Multi-language support
* 📈 Interview performance analytics

---

## 👨‍💻 Author

**Ishan Dhakad**
Aspiring AI Engineer | Information Security Student | Data Science Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
