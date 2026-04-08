import streamlit as st
import matplotlib.pyplot as plt
from resume_parser import extract_text
from ai_engine import analyze_resume, improve_resume, skill_gap_analysis, interview_prep

st.set_page_config(page_title="AI Resume Advisor", layout="wide")

# 🎨 Premium UI Styling
st.markdown("""
<style>
.card {
    padding: 25px;
    border-radius: 16px;
    background: linear-gradient(145deg, #1e1e1e, #111);
    box-shadow: 0px 0px 20px rgba(0,255,150,0.1);
    margin-top: 20px;
    border: 1px solid rgba(255,255,255,0.05);
}
body {
    background-color: #0e1117;
}
</style>
""", unsafe_allow_html=True)

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

    # =========================
    # 📊 RESUME ANALYSIS
    # =========================
    if mode == "Resume Analysis":
        if st.button("Analyze"):
            with st.spinner("Analyzing..."):
                result, score = analyze_resume(resume_text, job_role)

            st.success("Done!")

            # 📊 Score Section
            st.subheader("📊 Resume Score")

            color = "#00ff88" if score >= 75 else "#ffaa00" if score >= 50 else "#ff4d4d"

            st.markdown('<div class="card">', unsafe_allow_html=True)

            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                fig, ax = plt.subplots(figsize=(4, 3))

                bars = ax.bar(["Score"], [score], color=color, width=0.4)

                ax.set_ylim(0, 100)
                ax.set_facecolor("#1e1e1e")
                fig.patch.set_facecolor("#1e1e1e")

                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                ax.tick_params(colors='white')
                ax.set_ylabel("Score", color='white')

                # Score label
                for bar in bars:
                    yval = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2, yval + 2,
                            f'{score}',
                            ha='center', va='bottom', color='white', fontsize=12)

                st.pyplot(fig)

            st.markdown('</div>', unsafe_allow_html=True)

            # 🎯 Score Feedback
            if score >= 75:
                st.success(f"🔥 Excellent Resume: {score}/100")
            elif score >= 50:
                st.warning(f"⚡ Average Resume: {score}/100")
            else:
                st.error(f"❌ Needs Improvement: {score}/100")

            # 📦 Detailed Analysis
            st.subheader("📄 Detailed Analysis")

            st.markdown(f"""
            <div class="card">
            {result.replace('\n', '<br>')}
            </div>
            """, unsafe_allow_html=True)

    # =========================
    # ✨ RESUME IMPROVER
    # =========================
    elif mode == "Resume Improver":
        if st.button("Improve Resume"):
            with st.spinner("Improving..."):
                result = improve_resume(resume_text)

            st.success("Done!")

            st.subheader("✨ Improved Resume")

            st.markdown(f"""
            <div class="card">
            {result.replace('\n', '<br>')}
            </div>
            """, unsafe_allow_html=True)

    # =========================
    # 🧠 SKILL GAP ANALYSIS
    # =========================
    elif mode == "Skill Gap Analysis":
        if st.button("Check Skills"):
            with st.spinner("Analyzing skills..."):
                result = skill_gap_analysis(resume_text, job_role)

            st.success("Done!")

            st.subheader("🧠 Skill Gap Analysis")

            st.markdown(f"""
            <div class="card">
            {result.replace('\n', '<br>')}
            </div>
            """, unsafe_allow_html=True)

    # =========================
    # 🎤 INTERVIEW PREP
    # =========================
    elif mode == "Interview Preparation":
        if st.button("Generate Questions"):
            with st.spinner("Generating..."):
                result = interview_prep(job_role)

            st.success("Done!")

            st.subheader("🎤 Interview Preparation")

            st.markdown(f"""
            <div class="card">
            {result.replace('\n', '<br>')}
            </div>
            """, unsafe_allow_html=True)

else:
    st.warning("Please upload a resume to continue.")