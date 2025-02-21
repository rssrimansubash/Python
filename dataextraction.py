import fitz

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path) 
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

pdf_file = "Path"  # Full path
extracted_text = extract_text_from_pdf(pdf_file)

print(extracted_text)
