import streamlit as st
from utils import extract_text_from_pdf, extract_skills

from model import (
    match_roles,
    calculate_resume_score,
    generate_suggestions,
    fetch_jobs,
    get_learning_resources,
    resume_sections_check,
    suggest_projects,
    career_path
)

# 🔹 Page settings
st.set_page_config(page_title="AI Career Assistant", layout="wide")

# 🔹 Custom CSS
st.markdown("""
<style>
.badge {
    display:inline-block;
    padding:6px 12px;
    margin:5px;
    background-color:#1f77b4;
    color:white;
    border-radius:10px;
    font-size:14px;
}
</style>
""", unsafe_allow_html=True)

# 🔹 Sidebar
st.sidebar.title("🚀 AI Career Assistant")
st.sidebar.info("""
Upload your resume and get:
✔ Resume Score  
✔ Skills Analysis  
✔ Career Suggestions  
✔ Job Opportunities  
✔ Learning Resources  
""")

# 🔹 Title
st.title("🚀 AI Career Assistant")
st.markdown("### Turn your resume into opportunities")

# 🔹 Upload
uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

# 🔹 Main logic
if uploaded_file is not None:
    with st.spinner("🔍 Analyzing resume..."):

        text = extract_text_from_pdf(uploaded_file)
        skills = extract_skills(text)

        # ✅ Career path (FIXED)
        path = career_path(skills)

        score = calculate_resume_score(text, skills)
        suggestions = generate_suggestions(text, skills, score)
        results = match_roles(skills)
        jobs = fetch_jobs(skills)
        resources = get_learning_resources(skills)
        tips = resume_sections_check(text)
        projects = suggest_projects(skills)

    # 🔥 Dashboard metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📊 Resume Score", f"{score}/100")

    with col2:
        st.metric("🧠 Skills Found", len(skills))

    with col3:
        top_role = results[0]['role'] if results else "N/A"
        st.metric("💼 Best Role", top_role)

    st.divider()

    # 🎯 Career Path
    st.subheader("🎯 Career Path Recommendation")
    st.success(path)

    st.divider()

    # 🧠 Skills
    st.subheader("🧠 Your Skills")
    for skill in skills:
        st.markdown(f"<span class='badge'>{skill}</span>", unsafe_allow_html=True)

    st.divider()

    # 💼 Roles
    st.subheader("💼 Recommended Roles")

    for res in results:
        st.markdown(f"""
        ### {res['role']}
        **Match Score:** {res['score']}%  
        **Missing Skills:** {', '.join(res['missing_skills'])}
        """)
        st.progress(int(res['score']))
        st.markdown("---")

    st.divider()

    # 📚 Learning Resources
    st.subheader("📚 Learning Resources")

    if resources:
        for skill, link in resources.items():
            st.markdown(f"👉 Learn **{skill}**: [Start Learning]({link})")
    else:
        st.write("No resources found")

    st.divider()

    # 📄 Resume Tips
    st.subheader("📄 Resume Improvement Tips")

    if tips:
        for tip in tips:
            st.warning(tip)
    else:
        st.success("Your resume has all important sections!")

    st.divider()

    # 💡 Projects
    st.subheader("💡 Project Ideas")

    if projects:
        for p in projects:
            st.info(p)
    else:
        st.write("Add more skills to get project ideas")

    st.divider()

    # 🤖 Suggestions
    st.subheader("🤖 AI Suggestions")

    for s in suggestions:
        st.success(s)

    st.divider()

    # 🌍 Jobs
    st.subheader("🌍 Job Opportunities")

    for job in jobs:
        st.markdown(f"""
        **{job['title']}**  
        Company: {job['company']}  
        Location: {job['location']}  
        [Apply Here]({job['link']})
        """)
        st.markdown("---")

    # 📥 Download Report
    report = f"""
Resume Score: {score}

Skills: {', '.join(skills)}

Career Path: {path}

Top Role: {top_role}

Suggestions:
{' '.join(suggestions)}
"""

    st.download_button("📥 Download Report", report, file_name="career_report.txt")