from groq import Groq
from dotenv import load_dotenv
import json
import os

from utils.prompts import (
    SCENARIO_PROMPT,
    GAP_ANALYSIS_PROMPT,
    TEST_CASE_PROMPT,
    BA_QUESTION_PROMPT
)
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_test_scenarios(requirement_text):

    prompt = SCENARIO_PROMPT.format(
            requirement=requirement_text
        )
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

def analyze_requirement_gaps(requirement_text):

    prompt = GAP_ANALYSIS_PROMPT.format(
        requirement=requirement_text
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


def generate_test_cases(requirement_text):

    prompt = TEST_CASE_PROMPT.format(
        requirement=requirement_text
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    result = response.choices[0].message.content

    return result

#generate ba questions
def generate_ba_questions(
        requirement_text
):

    prompt = BA_QUESTION_PROMPT.format(
        requirement=requirement_text
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content