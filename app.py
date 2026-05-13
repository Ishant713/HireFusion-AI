import streamlit as st
import PyPDF2
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# Gemini API Key
API_KEY = os.getenv("GEMINI_API_KEY")

# Check API Key
if not API_KEY:
    st.error("❌ Gemini API Key not found in .env file")
    st.stop()

# Configure Gemini
genai.configure(api_key=API_KEY)

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Start Chat Session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Streamlit Page Config
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("📄 AI Resume Analyzer & AI Interview Bot")

st.write("Upload your resume and get AI-powered analysis")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

# Job Role Input
job_role = st.text_input(
    "Enter Target Job Role",
    placeholder="Example: AI Engineer"
)

# Extract Text from PDF
def extract_text_from_pdf(pdf_file):

    text = ""

    try:

        reader = PyPDF2.PdfReader(pdf_file)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text[:5000]

    except Exception as e:

        return f"PDF Reading Error: {str(e)}"

# Resume Analysis Function
@st.cache_data(show_spinner=False)
def analyze_resume(resume_text, job_role):

    prompt = f"""
    You are an expert HR recruiter and technical interviewer.

    Analyze this resume for the role: {job_role}

    Resume:
    {resume_text}

    Give output in this format:

    1. Resume Summary
    2. Strengths
    3. Weaknesses
    4. Missing Skills
    5. ATS Score out of 100
    6. Suggestions to Improve Resume
    7. Suitable Job Roles
    8. 10 HR Interview Questions
    9. 10 Technical Interview Questions
    10. 5 Project-Based Questions
    11. 5 Scenario-Based Questions
    """

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"""
❌ Gemini API Error

{str(e)}
"""

# Generate Interview Question
def generate_question(job_role):

    prompt = f"""
    Ask one professional interview question for a {job_role} role.
    """

    try:

        response = st.session_state.chat.send_message(prompt)

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"

# Evaluate Candidate Answer
def evaluate_answer(question, answer):

    prompt = f"""
    Evaluate this interview answer.

    Question:
    {question}

    Candidate Answer:
    {answer}

    Give output in this format:

    1. Score out of 10
    2. Strengths
    3. Weaknesses
    4. Better Professional Answer
    """

    try:

        response = st.session_state.chat.send_message(prompt)

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"

# Main App
if uploaded_file is not None and job_role:

    # Extract Resume Text
    resume_text = extract_text_from_pdf(uploaded_file)

    # Analyze Resume Button
    if st.button("Analyze Resume"):

        with st.spinner("🤖 Analyzing Resume..."):

            analysis = analyze_resume(
                resume_text,
                job_role
            )

        st.subheader("📌 Resume Analysis")

        st.write(analysis)

        # Save Analysis
        st.session_state.analysis = analysis
        st.session_state.resume_text = resume_text

    # AI Interview Bot Section
    st.divider()

    st.header("🎤 AI Interview Bot")

    # Generate New Question
    if st.button("Generate Interview Question"):

        question = generate_question(job_role)

        st.session_state.current_question = question

    # Show Question
    if "current_question" in st.session_state:

        st.subheader("🧑‍💼 Interviewer Question")

        st.write(st.session_state.current_question)

        # User Answer
        user_answer = st.text_area(
            "✍️ Your Answer",
            height=150
        )

        # Evaluate Answer
        if st.button("Evaluate My Answer"):

            if user_answer.strip() == "":

                st.warning("Please enter your answer")

            else:

                with st.spinner("📊 Evaluating Answer..."):

                    feedback = evaluate_answer(
                        st.session_state.current_question,
                        user_answer
                    )

                st.subheader("📈 Interview Feedback")

                st.write(feedback)

    # Download Report
    if "analysis" in st.session_state:

        report = f"""
AI RESUME ANALYZER REPORT

========================================

TARGET ROLE:
{job_role}

========================================

RESUME ANALYSIS:

{st.session_state.analysis}
"""

        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name="AI_Resume_Analysis_Report.txt",
            mime="text/plain"
        )

else:

    st.info("📄 Upload a PDF resume and enter a target job role")