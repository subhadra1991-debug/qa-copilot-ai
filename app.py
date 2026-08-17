import streamlit as st
from utils.pdf_reader import extract_text

from services.scenario_service import (
    generate_scenarios
)

from services.gap_analysis_service import (
    generate_gap_analysis
)

from services.testcase_service import (
    generate_testcases
)

from utils.excel_exporter import (
    dataframe_to_excel
)
from services.ba_question_service import (
    generate_questions
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

if "ba_question_df" not in st.session_state:
    st.session_state["ba_question_df"] = None

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

if st.button("🗑️ Clear Generated Results"):

    st.session_state["scenario_df"] = None
    st.session_state["gap_output"] = None
    st.session_state["testcase_df"] = None
    st.session_state["ba_question_df"] = None

    #st.rerun()

# ---------------------------------
# Upload Requirement
# ---------------------------------

uploaded_file = st.file_uploader(
    "Upload Requirement Document",
    type=["pdf", "txt"]
)

# ---------------------------------
# Main Processing
# ---------------------------------

if uploaded_file:

    st.success(
        "File uploaded successfully!"
    )

    st.write(
        f"Filename: {uploaded_file.name}"
    )

    st.write(
        f"File Type: {uploaded_file.type}"
    )

    requirement_text = extract_text(
        uploaded_file
    )

    if len(
        requirement_text.strip()
    ) == 0:

        st.error(
            "Uploaded file is empty."
        )

    else:

        # -------------------------
        # Requirement Preview
        # -------------------------

        st.subheader(
            "Requirement Preview"
        )

        st.text_area(
            "Extracted Requirement",
            requirement_text,
            height=300
        )

        # -------------------------
        # Action Buttons
        # -------------------------

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            scenario_clicked = st.button(
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
        with col4:

            ba_clicked = st.button(
                "Generate BA Questions"
            )

        # -------------------------
        # Generate Scenarios
        # -------------------------

        if scenario_clicked:

            with st.spinner(
                "Generating test scenarios..."
            ):

                scenario_df = (
                    generate_scenarios(
                        requirement_text
                    )
                )

                st.session_state[
                    "scenario_df"
                ] = scenario_df

        # -------------------------
        # Requirement Gaps
        # -------------------------

        if gap_clicked:

            with st.spinner(
                "Analyzing requirements..."
            ):

                gap_output = (
                    generate_gap_analysis(
                        requirement_text
                    )
                )

                st.session_state[
                    "gap_output"
                ] = gap_output

        # -------------------------
        # Generate Test Cases
        # -------------------------

        if testcase_clicked:

            with st.spinner(
                "Generating test cases..."
            ):

                try:

                    testcase_df = (
                        generate_testcases(
                            requirement_text
                        )
                    )

                    st.session_state[
                        "testcase_df"
                    ] = testcase_df

                except Exception as e:

                    st.error(
                        f"Error: {e}"
                    )
        if ba_clicked:

            with st.spinner(
                "Generating BA Questions..."
            ):

                try:

                    ba_df = generate_questions(
                    requirement_text
                    )

                    st.session_state[
                        "ba_question_df"
                    ] = ba_df

                except Exception as e:

                    st.error(
                    f"Error: {e}"
            )

# ---------------------------------
# Display Scenarios
# ---------------------------------

if st.session_state[
    "scenario_df"
] is not None:

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

    excel_data = dataframe_to_excel(
        scenario_df,
        sheet_name="Scenarios"
    )

    st.download_button(
        label="📥 Download Scenarios Excel",
        data=excel_data,
        file_name="test_scenarios.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# ---------------------------------
# Display Gap Analysis
# ---------------------------------

if st.session_state[
    "gap_output"
]:

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

if st.session_state[
    "testcase_df"
] is not None:

    testcase_df = st.session_state[
        "testcase_df"
    ]

    st.subheader(
        "Generated Test Cases"
    )

    st.write(
        f"Number of Test Cases: {len(testcase_df)}"
    )

    st.dataframe(
        testcase_df,
        use_container_width=True
    )

    excel_data = dataframe_to_excel(
        testcase_df,
        sheet_name="TestCases"
    )

    st.download_button(
        label="📥 Download Test Cases Excel",
        data=excel_data,
        file_name="test_cases.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


if st.session_state[
    "ba_question_df"
] is not None:

    ba_df = st.session_state[
        "ba_question_df"
    ]

    st.subheader(
        "BA Clarification Questions"
    )

    st.write(
        f"Number of Questions: {len(ba_df)}"
    )

    st.dataframe(
        ba_df,
        use_container_width=True
    )

    excel_data = dataframe_to_excel(
        ba_df,
        sheet_name="BA_Questions"
    )

    st.download_button(
        label="📥 Download BA Questions Excel",
        data=excel_data,
        file_name="ba_questions.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )