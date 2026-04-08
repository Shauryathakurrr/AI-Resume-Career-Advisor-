import requests
from config import GEMINI_API_KEY

URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"


def ask_ai(prompt):
    try:
        data = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        response = requests.post(URL, json=data)
        result = response.json()

        # 🔍 DEBUG (optional)
        # print(result)

        if "candidates" in result:
            return result['candidates'][0]['content']['parts'][0]['text']
        elif "error" in result:
            return f"API Error: {result['error']['message']}"
        else:
            return f"Unexpected response: {result}"

    except Exception as e:
        return f"Error: {str(e)}"

def analyze_resume(text, role):
    return ask_ai(f"""
    Analyze this resume for the role {role}.
    
    Give:
    - Strengths
    - Weaknesses
    - Missing skills
    - Resume score out of 100
    - Suggestions
    """)


def improve_resume(text):
    return ask_ai(f"Improve this resume:\n{text}")


def skill_gap_analysis(text, role):
    return ask_ai(f"Find missing skills for {role}:\n{text}")


def interview_prep(role):
    return ask_ai(f"Generate interview questions for {role}")