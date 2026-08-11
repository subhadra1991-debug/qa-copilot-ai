from pypdf import PdfReader

def extract_text(uploaded_file):

    if uploaded_file.type == "text/plain":
        text = uploaded_file.getvalue().decode("utf-8")
        return text
    elif uploaded_file.type == "application/pdf":
        pdf = PdfReader(uploaded_file)

        text = ""

        for page in pdf.pages:
            text += page.extract_text() + "\n"

        return text

    return ""