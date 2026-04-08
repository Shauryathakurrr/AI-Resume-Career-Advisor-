import streamlit as st
from resume_parser import extract_text
from ai_engine import analyze_resume, improve_resume, skill_gap_analysis, interview_prep

st.set_page_config(page_title="AI Resume Advisor", layout="wide")

st.title("🚀 AI Resume & Career Advisor")

# Sidebar
st.sidebar.title("Options")
mode = st.sidebar.radio("Choose Feature", [
    "Resume Analysis",
    "Resume Improver",
    "Skill Gap Analysis",
    "Interview Preparation"
])

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_role = st.text_input("Enter Target Job Role")

if uploaded_file:
    resume_text = extract_text(uploaded_file)

    if mode == "Resume Analysis":
        if st.button("Analyze"):
            with st.spinner("Analyzing..."):
                result = analyze_resume(resume_text, job_role)
                st.success("Done!")
                st.write(result)

    elif mode == "Resume Improver":
        if st.button("Improve Resume"):
            with st.spinner("Improving..."):
                result = improve_resume(resume_text)
                st.success("Done!")
                st.write(result)

    elif mode == "Skill Gap Analysis":
        if st.button("Check Skills"):
            with st.spinner("Analyzing skills..."):
                result = skill_gap_analysis(resume_text, job_role)
                st.success("Done!")
                st.write(result)

    elif mode == "Interview Preparation":
        if st.button("Generate Questions"):
            with st.spinner("Generating..."):
                result = interview_prep(job_role)
                st.success("Done!")
                st.write(result)

else:
    st.warning("Please upload a resume to continue.")