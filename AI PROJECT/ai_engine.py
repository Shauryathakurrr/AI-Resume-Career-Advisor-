from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional career advisor."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


def analyze_resume(text, role):
    prompt = f"""
    Analyze this resume for the role {role}.
    
    Provide:
    - Strengths
    - Weaknesses
    - Missing skills
    - Resume score out of 100
    - Suggestions for improvement
    """
    return ask_ai(prompt)


def improve_resume(text):
    prompt = f"""
    Rewrite this resume professionally.
    Make it ATS-friendly with proper formatting.
    
    Resume:
    {text}
    """
    return ask_ai(prompt)


def skill_gap_analysis(text, role):
    prompt = f"""
    Compare this resume with required skills for {role}.
    
    Provide:
    - Required skills
    - Missing skills
    - Learning roadmap (step-by-step)
    """
    return ask_ai(prompt)


def interview_prep(role):
    prompt = f"""
    Generate:
    - 5 technical interview questions
    - 5 HR questions
    - Sample answers
    
    Role: {role}
    """
    return ask_ai(prompt)