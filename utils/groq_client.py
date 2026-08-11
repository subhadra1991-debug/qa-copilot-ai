from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_test_scenarios(requirement_text):

    prompt = f"""
    You are a Senior QA Lead.

    Analyze the requirement below and generate:

    1. Functional Test Scenarios
    2. Positive Test Scenarios
    3. Negative Test Scenarios
    4. Boundary Test Scenarios

    Requirement:
    {requirement_text}
    """

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