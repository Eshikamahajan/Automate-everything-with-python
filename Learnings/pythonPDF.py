print("hello there")
from fpdf import FPDF
pdf=FPDF(orientation="P",unit='pt',format="A4")
pdf.add_page() # adding a page in the pdf
pdf.image('Automate-everything-with-python/LogoTM.png',w=100,h=100,x=50) # adding an image to the pdf

pdf.set_font(family="Times",style="B",size=24)  #setting the font type of the line to be printed below
pdf.cell(w=0,h=50,txt="Agenda Meeting #2", align="C",ln=1) #w=0 means only 1 cell occupies the entire line

pdf.set_font(family="Times",style="B",size=15)
pdf.multi_cell(w=0,h=50,txt='''Here we are talking about multine cell text. writing a lot fo text so that is goes to the next line. hahahaha. Here we are talking about multine cell text. writing a lot fo text so that is goes to the next line. hahahaha ''')


#printing tabular data by playing with the cell width to display borders, just write borders
pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Kingdom:',border=1)

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Animalia',border=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Phylum:',border=1)

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Chordata',border=1,ln=1)

#SAME THING WITHOUT BORDER
pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Kingdom:')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Animalia',ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Phylum:')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Chordata',ln=1)

'''
output will look like 
Kingdom: Animalia
Phylum: Chordata
'''


pdf.output("Automate-everything-with-python/Agenda_simple.pdf")