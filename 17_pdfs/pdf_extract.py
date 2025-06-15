import PyPDF2
import os
pdf_file = open('C:\\Users\\mrmin\\OneDrive - Nanyang Technological University\\Y4S2\FYP\\FYP_Final_Submission.pdf', 'rb') 
#read-binary arg is necessary to process PDF

print(PyPDF2.__version__)

reader = PyPDF2.PdfReader(pdf_file) # returns PDF reader object

print(len(reader.pages))
page = reader.pages[2] # returns page object
#print(page.extract_text())

for page in range(len(reader.pages)):
    print(reader.pages[page].extract_text())
# this prints all text, but PDF formatting can be weird

# this is MY FIX
for page in range(len(reader.pages)):
    text = reader.pages[page].extract_text()
    cleaned = "".join(text.splitlines())
    print(cleaned)


# merging / creating pdf files
writer = PyPDF2.PdfWriter # writer obj is a BLANK PDF

#surely there is an easier way to iterate through all pdfs?
pdf1 = open(r"C:\Users\mrmin\OneDrive - Nanyang Technological University\Y4S2\Coursera Excel_to_MySQL_Analytic_Techniques_for_Business_Specialisation.pdf", "rb")
reader1 = PyPDF2.PdfReader(pdf1)
pdf2 = open(r"C:\Users\mrmin\OneDrive - Nanyang Technological University\Y4S2\Coursera Business Metrics.pdf", "rb")
reader2 = PyPDF2.PdfReader(pdf2)
pdf3 = open(r"C:\Users\mrmin\OneDrive - Nanyang Technological University\Y4S2\Coursera Data_Analysis_in_Excel.pdf", "rb")
reader3 = PyPDF2.PdfReader(pdf3)
pdf4 = open(r"C:\Users\mrmin\OneDrive - Nanyang Technological University\Y4S2\Coursera Data_Vis_in_Tableau.pdf", "rb")
reader4 = PyPDF2.PdfReader(pdf4)
pdf5 = open(r"C:\Users\mrmin\OneDrive - Nanyang Technological University\Y4S2\Coursera Managing_Big_Data_with_SQL.pdf", "rb")
reader5 = PyPDF2.PdfReader(pdf5)
pdf6 = open(r"C:\Users\mrmin\OneDrive - Nanyang Technological University\Y4S2\Coursera Increasing_Real_Estate_Profits_Data_Analytics.pdf", "rb")
reader6 = PyPDF2.PdfReader(pdf6)
pdf7 = open(r"C:\Users\mrmin\OneDrive - Nanyang Technological University\Y4S2\Coursera High_Stakes_Leadership.pdf", "rb")
reader7 = PyPDF2.PdfReader(pdf7)

for page_num in range(len(reader1.pages)):
    page = reader1.pages[page_num]
    writer.add_page(page)

#SAVING PDS
output_pdf = open('17_save_pdf_test.pdf', 'wb') # WRITE-BINARY necessary
writer.write(output_pdf)
output_pdf.close()
pdf1.close()
pdf2.close()
pdf3.close()
pdf4.close()
pdf5.close()