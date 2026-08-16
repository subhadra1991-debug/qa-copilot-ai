# 🧪 QA-Copilot-AI

AI-Powered Requirement Analysis & Test Design Assistant built using Python, Streamlit, Groq LLM, Pandas, and OpenPyXL.

QA-Copilot-AI helps QA Engineers, Test Analysts, Business Analysts, and QA Leads accelerate requirement understanding, identify gaps, generate test scenarios, and create detailed test cases from requirement documents.

---

# 🚀 Features

## Requirement Upload

* Upload PDF requirement documents
* Upload TXT requirement documents
* Automatic text extraction

## Requirement Preview

* Preview extracted requirement content before analysis
* Validate uploaded document contents

## Test Scenario Generation

Generate comprehensive test scenarios including:

* Positive Scenarios
* Negative Scenarios
* Boundary Scenarios
* Security Scenarios

Output includes:

* Scenario ID
* Scenario Description
* Scenario Type
* Priority

## Requirement Gap Analysis

Identify:

* Missing Requirements
* Ambiguous Requirements
* Clarification Questions
* Business Risks
* Missing Negative Scenarios
* Boundary Conditions
* Integration Risks
* Data Validation Risks

## Test Case Generation

Generate detailed test cases including:

* Test Case ID
* Test Scenario
* Test Steps
* Test Data
* Expected Result
* Priority

## Excel Export

Export generated outputs to Excel:

* Test Scenarios XLSX
* Test Cases XLSX

## Session State Persistence

Results remain available until cleared by the user.

## Clear Results

Reset all generated outputs with a single click.

---

# 🏗️ Project Architecture

```text
qa-copilot-ai/
│
├── app.py
│
├── services/
│   ├── __init__.py
│   ├── scenario_service.py
│   ├── gap_analysis_service.py
│   └── testcase_service.py
│
├── utils/
│   ├── pdf_reader.py
│   ├── groq_client.py
│   ├── prompts.py
│   └── excel_exporter.py
│
├── requirements.txt
└── README.md
```

---

# 🛠️ Technology Stack

* Python 3.11+
* Streamlit
* Groq API
* Llama 3.3 70B Versatile
* Pandas
* OpenPyXL
* PyPDF
* Python Dotenv

---

# 📦 Installation

Clone repository:

```bash
git clone https://github.com/<your-username>/qa-copilot-ai.git
cd qa-copilot-ai
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

Application launches at:

```text
http://localhost:8501
```

---

# 📈 Development Progress

## Sprint 1

* Streamlit Setup
* Groq Integration

## Sprint 2

* Requirement Upload
* PDF/TXT Extraction

## Sprint 3

* Test Scenario Generation

## Sprint 4

* Requirement Gap Analysis

## Sprint 5

* Test Case Generation

## Sprint 6

* Test Case Excel Export

## Sprint 7

* Scenario Excel Export
* Session State Persistence

## Sprint 8

* Service Layer Refactoring
* Reusable Excel Export Utility
* Improved Code Maintainability

## Upcoming Sprint 9

* BA Question Generator
* BA Question Excel Export

---

# 🎯 Vision

To build an AI-powered QA Copilot that assists software testers throughout the entire testing lifecycle:

* Requirement Analysis
* Gap Analysis
* Test Scenario Design
* Test Case Design
* BA Clarification Questions
* Risk Analysis
* RTM Generation
* Test Data Generation
* Automation Accelerator

---

# 👩‍💻 Author

Subhadra Mahapatra

Senior QA Professional | AI Enthusiast | Building AI Solutions for Software Testing
