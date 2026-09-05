SCENARIO_PROMPT = """
You are a Senior QA Lead.

Generate test scenarios in JSON format.

Return ONLY valid JSON.

Format:

[
  {{
    "Scenario_ID": "TS001",
    "Scenario": "Verify successful login",
    "Scenario_Type": "Positive",
    "Priority": "High"
  }}
]

Generate at least 15 scenarios.

Include:
- Positive Scenarios
- Negative Scenarios
- Boundary Scenarios
- Security Scenarios

Requirement:
{requirement}
"""
GAP_ANALYSIS_PROMPT = """
You are a highly experienced QA Lead with 15+ years of experience in
Retail, Utilities and Enterprise applications.

Review the requirement like a senior tester.

Identify:

1. Missing Requirements
2. Ambiguous Requirements
3. Clarification Questions for Business Analyst
4. Potential Business Risks
5. Missing Negative Scenarios
6. Missing Boundary Conditions
7. Integration Risks
8. Data Validation Risks

For each finding explain:
- Why it is important
- What defect could occur if ignored

Requirement:
{requirement}
"""

TEST_CASE_PROMPT = """
You are a Senior QA Lead.

Generate test cases in JSON format.

Return ONLY valid JSON.

Format:

[
  {{
    "TC_ID": "TC001",
    "Test_Scenario": "Verify successful login",
    "Test_Steps": "Enter valid username and password and click Login",
    "Test_Data": "user1/password1",
    "Expected_Result": "User should login successfully",
    "Priority": "High"
  }}
]

Generate at least 15 test cases.

Requirement:
{requirement}
"""

BA_QUESTION_PROMPT = """
You are a Senior Business Analyst and QA Lead.

Analyze the requirement and identify all
clarification questions that should be asked
before testing begins.

Return ONLY valid JSON.

Format:

[
    {{
        "Question_ID": "BA001",
        "Question": "What happens if user enters invalid email?",
        "Category": "Validation",
        "Priority": "High"
    }}
]

Generate at least 15 questions.

Cover:

- Business Rules
- Validation Rules
- Boundary Conditions
- Error Handling
- Security
- Integration
- Notifications
- User Roles
- Data Persistence
- Reporting

Requirement:

{requirement}
"""



RTM_PROMPT = """
You are a Senior QA Lead.

Analyze the requirement.

Generate a Requirements Traceability Matrix.

Return ONLY valid JSON.

Format:

[
    {{
        "Requirement_ID":"R001",
        "Requirement":"User Login",
        "Scenario_ID":"TS001",
        "Scenario":"Verify successful login",
        "Test_Case_ID":"TC001",
        "Test_Case":"Verify login with valid credentials"
    }}
]

Generate at least 15 rows.

Requirement:

{requirement}
"""