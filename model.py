import pandas as pd

# 📊 Load skills dataset
data = pd.read_csv("skills_data.csv")


# 💼 Match roles based on skills
def match_roles(user_skills):
    results = []

    for _, row in data.iterrows():
        role = row["Role"]
        required_skills = [s.strip().lower() for s in row["Skills"].split(",")]

        matched = list(set([s.lower() for s in user_skills]) & set(required_skills))
        score = int((len(matched) / len(required_skills)) * 100)

        missing = list(set(required_skills) - set([s.lower() for s in user_skills]))

        results.append({
            "role": role,
            "score": score,
            "missing_skills": missing
        })

    # sort by score
    results = sorted(results, key=lambda x: x["score"], reverse=True)
    return results


# 📊 Resume score calculation
def calculate_resume_score(text, skills):
    score = 0

    if len(text) > 1000:
        score += 30
    else:
        score += 10

    score += min(len(skills) * 5, 40)

    if "project" in text.lower():
        score += 10

    if "experience" in text.lower():
        score += 10

    if "education" in text.lower():
        score += 10

    return min(score, 100)


# 🤖 Suggestions generator
def generate_suggestions(text, skills, score):
    suggestions = []

    if "education" not in text.lower():
        suggestions.append("Add your education details clearly.")

    if len(skills) < 5:
        suggestions.append("Add more technical skills to strengthen your profile.")

    if score < 50:
        suggestions.append("Your resume is weak. Improve content and structure.")
    elif score < 75:
        suggestions.append("Good resume, but can be improved with more details.")
    else:
        suggestions.append("Strong resume! Just fine-tune formatting.")

    return suggestions


# 🌍 Dummy job data (no API needed)
def fetch_jobs(skills):
    jobs = [
        {
            "title": "Python Developer",
            "company": "Infosys",
            "location": "Bangalore",
            "link": "https://www.infosys.com/careers"
        },
        {
            "title": "Data Analyst",
            "company": "TCS",
            "location": "Delhi",
            "link": "https://www.tcs.com/careers"
        },
        {
            "title": "Web Developer",
            "company": "Wipro",
            "location": "Hyderabad",
            "link": "https://www.wipro.com/careers"
        }
    ]

    return jobs


# 📚 Learning resources
def get_learning_resources(skills):
    resources = {
        "python": "https://www.youtube.com/watch?v=_uQrJ0TkZlc",
        "java": "https://www.youtube.com/watch?v=eIrMbAQSU34",
        "machine learning": "https://www.coursera.org/learn/machine-learning",
        "data science": "https://www.coursera.org/professional-certificates/data-science",
        "html": "https://www.w3schools.com/html/",
        "css": "https://www.w3schools.com/css/",
        "javascript": "https://www.youtube.com/watch?v=PkZNo7MFNFg"
    }

    result = {}
    for skill in skills:
        key = skill.lower()
        if key in resources:
            result[skill] = resources[key]

    return result


# 📄 Resume section checker
def resume_sections_check(text):
    tips = []

    text = text.lower()

    if "project" not in text:
        tips.append("Add projects section")

    if "experience" not in text:
        tips.append("Add experience section")

    if "skills" not in text:
        tips.append("Add skills section")

    return tips


# 💡 Project suggestions
def suggest_projects(skills):
    skills_lower = [s.lower() for s in skills]
    projects = []

    if "python" in skills_lower:
        projects.append("Build a Web Scraper using Python")

    if "machine learning" in skills_lower:
        projects.append("Create a House Price Prediction Model")

    if "html" in skills_lower:
        projects.append("Build a Portfolio Website")

    return projects


# 🎯 Career path recommendation
def career_path(skills):
    skills = [s.lower() for s in skills]

    if "python" in skills and "machine learning" in skills:
        return "AI Engineer / Data Scientist"

    elif "html" in skills and "css" in skills:
        return "Frontend Developer"

    elif "java" in skills:
        return "Backend Developer"

    return "Explore multiple domains"