import docx
import PyPDF2

def parse_file(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])

    elif file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages])

    return ""