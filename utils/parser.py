import pandas as pd


def create_sample_dataframe():

    data = {
        "TC_ID": [
            "TC001",
            "TC002"
        ],
        "Test Scenario": [
            "Verify Login",
            "Invalid Password"
        ],
        "Priority": [
            "High",
            "Medium"
        ]
    }

    return pd.DataFrame(data)