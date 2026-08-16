import streamlit as st
import json
import pandas as pd
from io import BytesIO
from utils.pdf_reader import extract_text

from utils.groq_client import (
    generate_test_scenarios,
    analyze_requirement_gaps,
    generate_test_cases
)

# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="QA-Copilot-AI",
    page_icon="🧪",
    layout="wide"
)

# ---------------------------------
# Session State Initialization
# ---------------------------------

if "scenario_df" not in st.session_state:
    st.session_state["scenario_df"] = None

if "gap_output" not in st.session_state:
    st.session_state["gap_output"] = None

if "testcase_df" not in st.session_state:
    st.session_state["testcase_df"] = None

# ---------------------------------
# Title
# ---------------------------------

st.title("🧪 QA-Copilot-AI")
st.subheader(
    "AI-Powered Requirement Analysis & Test Design Assistant"
)

# ---------------------------------
# Clear Results Button
# ---------------------------------

if st.button("🔄 Clear Results"):

    st.session_state["scenario_output"] = None
    st.session_state["gap_output"] = None
    st.session_state["testcase_df"] = None

    st.rerun()

# ---------------------------------
# File Upload
# ---------------------------------

uploaded_file = st.file_uploader(
    "Upload Requirement Document",
    type=["pdf", "txt"]
)

# ---------------------------------
# Main Processing
# ---------------------------------

if uploaded_file:

    st.success("File uploaded successfully!")

    st.write(f"Filename: {uploaded_file.name}")
    st.write(f"File Type: {uploaded_file.type}")

    requirement_text = extract_text(uploaded_file)

    if len(requirement_text.strip()) == 0:

        st.error(
            "Uploaded file is empty. Please upload a valid requirement document."
        )

    else:

        # Requirement Preview

        st.subheader("Requirement Preview")

        st.text_area(
            "Extracted Requirement",
            requirement_text,
            height=300
        )

        # Buttons

        col1, col2, col3 = st.columns(3)

        with col1:

            generate_clicked = st.button(
                "Generate Test Scenarios"
            )

        with col2:

            gap_clicked = st.button(
                "Find Requirement Gaps"
            )

        with col3:

            testcase_clicked = st.button(
                "Generate Test Cases"
            )

        # -------------------------
        # Scenario Generation
        # -------------------------

        if generate_clicked:

            with st.spinner(
                "Generating test scenarios..."
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

                st.session_state[
                "scenario_df"
                ] = scenario_df

        # -------------------------
        # Gap Analysis
        # -------------------------

        if gap_clicked:

            with st.spinner(
                "Analyzing requirements..."
            ):

                gap_analysis = analyze_requirement_gaps(
                    requirement_text
                )

                st.session_state[
                    "gap_output"
                ] = gap_analysis

        # -------------------------
        # Test Case Generation
        # -------------------------

        if testcase_clicked:

            with st.spinner(
                "Generating test cases..."
            ):

                test_cases = generate_test_cases(
                    requirement_text
                )

                try:

                    test_cases_json = json.loads(
                        test_cases
                    )

                    df = pd.DataFrame(
                        test_cases_json
                    )

                    st.session_state[
                        "testcase_df"
                    ] = df

                except Exception as e:

                    st.error(
                        f"Error processing test cases: {e}"
                    )

                    st.code(
                        test_cases
                    )

# ---------------------------------
# Display Scenario Output
# ---------------------------------

if st.session_state["scenario_df"] is not None:

    scenario_df = st.session_state[
        "scenario_df"
    ]

    st.subheader(
        "Generated Test Scenarios"
    )

    st.dataframe(
        scenario_df,
        use_container_width=True
    )

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        scenario_df.to_excel(
            writer,
            index=False,
            sheet_name="Scenarios"
        )

    st.download_button(
        label="📥 Download Scenarios Excel",
        data=output.getvalue(),
        file_name="test_scenarios.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# ---------------------------------
# Display Gap Analysis
# ---------------------------------

if st.session_state["gap_output"]:

    st.subheader(
        "Requirement Gap Analysis"
    )

    st.markdown(
        st.session_state[
            "gap_output"
        ]
    )

# ---------------------------------
# Display Test Cases
# ---------------------------------

if st.session_state["testcase_df"] is not None:

    df = st.session_state[
        "testcase_df"
    ]

    st.subheader(
        "Generated Test Cases"
    )

    st.write(
        f"Number of Test Cases: {len(df)}"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    # Excel Export

    excel_file = "test_cases.xlsx"

    df.to_excel(
        excel_file,
        index=False
    )

    with open(
        excel_file,
        "rb"
    ) as file:

        st.download_button(
            label="📥 Download Test Cases Excel",
            data=file,
            file_name="test_cases.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )