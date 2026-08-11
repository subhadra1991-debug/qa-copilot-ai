import streamlit as st
from utils.pdf_reader import extract_text
from utils.groq_client import generate_test_scenarios
st.set_page_config(
    page_title="QA-Copilot-AI",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 QA-Copilot-AI")

st.subheader("Requirement to Test Scenario Generator")

uploaded_file = st.file_uploader(
    "Upload Requirement Document",
    type=["pdf","txt"],
    #accept_multiple_files=True
)

if uploaded_file:

    st.success("File uploaded successfully!")

    st.write(f"Filename: {uploaded_file.name}")
    st.write(f"File Type: {uploaded_file.type}")

    requirement_text = extract_text(uploaded_file)
    st.write("Length of extracted text:", len(requirement_text))
    st.write(repr(requirement_text[:100]))

    st.subheader("Requirement Preview")

    st.text_area(
        "Extracted Requirement",
        requirement_text,
        height=300
    )

    if st.button("Generate Test Scenarios"):

        with st.spinner("Analyzing requirements..."):

            scenarios = generate_test_scenarios(
                requirement_text
            )

            st.subheader("Generated Test Scenarios")

            st.markdown(scenarios)