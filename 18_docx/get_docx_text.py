import docx

def get_text(filename):
    d = docx.Document(filename)
    text = []
    for paragraph in d.paragraphs:
        text.append(paragraph.text)
    return '\n\n'.join(text)

print(get_text("18_docx\\my_resume_copy.docx"))