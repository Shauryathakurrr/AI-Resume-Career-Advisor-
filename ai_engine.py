import ollama
def ask_ai(prompt):
    response = ollama.chat(
        model='llama3:instruct',
        messages=[
            {
                "role": "system",
                "content": "You are a professional HR expert. Give structured answers."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0.6,
            "top_p": 0.9
        }
    )
    return response['message']['content']


import re

def analyze_resume(text, role):
    result = ask_ai(f"""
    You are an expert resume reviewer.

    Analyze this resume for the role: {role}

    STRICT FORMAT:

    Resume Score: XX/100

    Strengths:
    - point
    - point

    Weaknesses:
    - point

    Missing Skills:
    - point

    Suggestions:
    - point

    Resume:
    {text}
    """)

    # 🎯 Extract score
    match = re.search(r'(\d{1,3})/100', result)
    score = int(match.group(1)) if match else 50

    return result, score

def improve_resume(text):
    return ask_ai(f"""
    Rewrite the following resume professionally.

    Make it:
    - ATS-friendly
    - Clear and well-structured
    - Use bullet points

    Resume:
    {text}
    """)


def skill_gap_analysis(text, role):
    return ask_ai(f"""
    Compare this resume with the required skills for {role}.

    Resume:
    {text}

    Provide:
    1. Required Skills
    2. Missing Skills
    3. Step-by-step Learning Roadmap
    """)


def interview_prep(role):
    return ask_ai(f"""
    Generate interview preparation for {role}.

    Provide:
    - 5 Technical Questions with answers
    - 5 HR Questions with answers
    """)