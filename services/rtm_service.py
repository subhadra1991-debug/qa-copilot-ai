import json
import pandas as pd

from utils.groq_client import (
    generate_rtm
)

def generate_rtm_matrix(
    requirement_text
):

    result = generate_rtm(
        requirement_text
    )

    rtm_json = json.loads(
        result
    )

    return pd.DataFrame(
        rtm_json
    )