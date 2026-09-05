from services.gap_analysis_service import generate_gap_analysis
from services.ba_question_service import generate_questions
from services.scenario_service import generate_scenarios
from services.testcase_service import generate_testcases
from services.rtm_service import generate_rtm_matrix

def run_complete_qa_analysis(requirement_text):

    results = {}

    # Gap Analysis
    results["gap_analysis"] = generate_gap_analysis(
        requirement_text
    )

    # BA Questions
    results["ba_questions"] = generate_questions(
        requirement_text
    )

    # Test Scenarios
    results["scenarios"] = generate_scenarios(
        requirement_text
    )

    # Test Cases
    results["test_cases"] = generate_testcases(
        requirement_text
    )

    # RTM
    results["rtm"] = generate_rtm_matrix(
        requirement_text
    )

    return results