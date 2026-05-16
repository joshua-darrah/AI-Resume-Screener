import docx
import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
        
        if extracted:
            text += extracted

    return text



def extract_text_from_docx(docx_path):
    text = ''
    doc = docx.Document(docx_path)

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text
