import pandas as pd


def export_testcases_to_excel(df):

    file_name = "test_cases.xlsx"

    df.to_excel(
        file_name,
        index=False
    )

    return file_name