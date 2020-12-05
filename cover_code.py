'''
This is a Python code to edit cover letter based on the job position and company name.

@author Amir Hallak
'''

###########################################################
###########################################################

# import modules
from fpdf import FPDF
from datetime import datetime

###########################################################
###########################################################

# constants
TEXT_FILE = './cover_text.txt'
FONT = 'Times'
FONT_SIZE = 12
UNIT = 'mm'
FORMAT = 'letter'

# globals
applicant_name = None
company_name = None
company_position = None
company_location = None
date = None

###########################################################
###########################################################

# retrieving application information 
def company_info():
    '''
    '''

    global applicant_name, date
    global company_name, company_position, company_location
    
    applicant_name = input("Enter your full name: ")
    company_name = input("Enter company name: ")
    company_position = input("Enter company positon: ")
    company_location = input("Enter company location: ")
    date = datetime.today().strftime('%B %d, %Y')

###########################################################
###########################################################

# header specifications in the pdf
def pdf_header(document):

    # header text
    header_text = f'{date}\n{company_name}\n{company_location}\nPosition: {company_position}'

    # writing header information
    document.set_font(FONT, 'B', FONT_SIZE)
    document.multi_cell(0,5, header_text, ln=2)
    
# body specifications and body text import
def pdf_body(document):

    # cover text
    with open(TEXT_FILE, 'rb') as F1:
        body_text = F1.read().decode('latin1').format(company_position, company_name)

    # writing body
    document.ln(12.5)
    document.set_font(FONT, '', FONT_SIZE)
    document.multi_cell(0,5, body_text, ln=2)

# footer specifications in the pdf
def pdf_footer(document):

    # footer text
    footer_text = f'Thank you,\n{applicant_name}'
    
    # writing footer
    document.ln(12.5)
    document.set_font(FONT, 'B', FONT_SIZE)
    document.multi_cell(0, 5, footer_text)
    
###########################################################
###########################################################

# writing pdf
def pdf_writer():
    '''
    The actual PDF writer starts.
    '''
    
    # setting up page settings
    document = FPDF()
    document.set_margins(25.4, 25.4, 25.4)
    document.add_page()
    
    pdf_header(document)
    pdf_body(document)
    pdf_footer(document)

    # export
    document.output(f"./Hallak_Cover_{company_name}.pdf")

###########################################################
###########################################################

#run
if __name__ == "__main__":
    company_info()
    pdf_writer()
