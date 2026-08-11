# 🧪 QA-Copilot-AI

QA-Copilot-AI is an AI-powered testing assistant that helps QA engineers analyze business requirements and generate test scenarios automatically.

The goal of this project is to reduce the time spent on requirement analysis and test design by leveraging Large Language Models (LLMs).

---

## 🚀 Features

### Current Features

✅ Upload Requirement Documents (.txt / .pdf)

✅ Extract Requirement Content

✅ Requirement Preview

✅ AI-Powered Test Scenario Generation

### Planned Features

🔄 Requirement Gap Analysis

🔄 Ambiguity Detection

🔄 Risk Assessment

🔄 Test Case Generation

🔄 Excel Export

🔄 Requirement Traceability Matrix (RTM)

🔄 Jira Integration

🔄 Multi-Agent QA Workflow

---

## 🏗️ Architecture

```text
Requirement File
      │
      ▼
Document Reader
      │
      ▼
Text Extraction
      │
      ▼
Groq LLM
      │
      ▼
Test Scenario Generation
      │
      ▼
QA Output
```

---

## 🛠️ Technology Stack

- Python
- Streamlit
- Groq API
- PyPDF
- Pandas
- Python Dotenv

---

## 📂 Project Structure

```text
qa-copilot-ai/
│
├── app.py
├── requirements.txt
├── .env
│
├── data/
├── output/
│
└── utils/
    ├── pdf_reader.py
    ├── groq_client.py
    └── prompts.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/qa-copilot-ai.git

cd qa-copilot-ai
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📸 Example Workflow

1. Upload a Business Requirement Document
2. Review Extracted Requirement
3. Click "Generate Test Scenarios"
4. Receive AI-generated:
   - Functional Scenarios
   - Positive Scenarios
   - Negative Scenarios
   - Boundary Scenarios

---

## 🎯 Vision

QA-Copilot-AI aims to evolve into an intelligent QA assistant capable of:

- Understanding business requirements
- Identifying missing requirements
- Detecting ambiguities
- Generating test scenarios
- Generating test cases
- Creating RTMs
- Acting as a virtual Senior QA Analyst

---

## 👩‍💻 Author

Subhadra Mahapatra

Senior QA Professional | GenAI Enthusiast | Automation Learner

Built as part of a journey to combine 13+ years of testing expertise with Generative AI.