from utils.groq_client import (
    analyze_requirement_gaps
)


def generate_gap_analysis(
    requirement_text
):

    return analyze_requirement_gaps(
        requirement_text
    )