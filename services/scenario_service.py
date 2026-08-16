import json
import pandas as pd

from utils.groq_client import (
    generate_test_scenarios
)


def generate_scenarios(
    requirement_text
):

    scenarios = generate_test_scenarios(
        requirement_text
    )

    scenario_json = json.loads(
        scenarios
    )

    scenario_df = pd.DataFrame(
        scenario_json
    )

    return scenario_df