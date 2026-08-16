from io import BytesIO
import pandas as pd


def dataframe_to_excel(
    df,
    sheet_name="Sheet1"
):

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name=sheet_name
        )

    output.seek(0)

    return output.getvalue()