import json
import pandas as pd

from utils.groq_client import (
    generate_ba_questions
)


def generate_questions(
    requirement_text
):

    questions = generate_ba_questions(
        requirement_text
    )

    question_json = json.loads(
        questions
    )

    question_df = pd.DataFrame(
        question_json
    )

    return question_df