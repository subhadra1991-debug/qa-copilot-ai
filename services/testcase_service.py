import json
import pandas as pd

from utils.groq_client import (
    generate_test_cases
)


def generate_testcases(
    requirement_text
):

    test_cases = generate_test_cases(
        requirement_text
    )

    test_cases_json = json.loads(
        test_cases
    )

    testcase_df = pd.DataFrame(
        test_cases_json
    )

    return testcase_df