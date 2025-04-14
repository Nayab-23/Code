import pdfplumber
from docx import Document

def pdf_to_docx(pdf_file, docx_file):
    doc = Document()

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:  
                doc.add_paragraph(text)

    doc.save(docx_file)
    print(f"Converted '{pdf_file}' to '{docx_file}' successfully.")

pdf_to_docx("example.pdf", "output.docx")