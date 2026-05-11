import pdfplumber

def extract_text_from_pdf(file):
    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted

    return text


def extract_skills(text):
    skills_list = [
        "python",
        "java",
        "c++",
        "html",
        "css",
        "javascript",
        "react",
        "node",
        "sql",
        "mongodb",
        "machine learning",
        "data science",
        "streamlit",
        "django",
        "flask"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills
