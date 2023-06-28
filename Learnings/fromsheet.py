import pandas
from fpdf import FPDF
import textwrap

fontSize=10
height=20

def dataframe(csv):
    df = pandas.read_csv(csv)
    #df = df.iloc[: , :-1] # remove the last column
    #df = df.iloc[:-1] # remove the last row
    #df=df.iloc[:,[2,1,0,3]] # re arrange the columns 
    print(df)
    df['agenda'] = df['agenda'].str.wrap(100)
    #df.rename(columns = {"Time Taken":'Time', 'Role':'Agenda','Name':'Role Player','Time Range':'Time Allotted'}, inplace = True)
    print(df)
    return df

def pdf(df):
    
    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()
    #print(help(pdf)) 
    pdf.set_font(family='Times',size=12)
    pdf.set_fill_color(10,80,180)
    pdf.set_draw_color(0,80,180) # gves colors to the border of the cell

    pdf.cell(w=0, h=height, txt="Connnected Across Miles Toastmasters Club", align='C', ln=1,border=1,fill=True,)

    #pdf.set_font(family='Times',size=14)
    pdf.cell(w=0, h=height, txt="Division K| Area 03 | District 124", align='C', ln=1,border=1)

    #pdf.set_font(family='Times',size=14)
    pdf.cell(w=0, h=height, txt="Meeting No. 2 | Agenda - 2nd July 2023 | 6:30 PM", align='C', ln=1,border=1)

    pdf.set_font(family='Times', style='B', size=fontSize)
    pdf.cell(w=70, h=height, txt="Time",border=1, align='C')
    pdf.cell(w=220, h=height, txt="Agenda", align='C',border=1)
    pdf.cell(w=150, h=height, txt="Role Player", align='C',border=1)
    pdf.cell(w=98.5, h=height, txt="Time allotted", align='C',border=1,ln=1)

    pdf.set_font(family='Times', size=fontSize)
    # read the excel here
    sample='Table Topics Master conducts the Table Topics session and\n hands over to the TMoD'
    for index, row in df.iterrows():
        #print(row[0], row["Agenda"])
        pdf.multi_cell(w=70, h=height, txt=str(row[0]),border=1, align='C') #time
        wrapper = textwrap.TextWrapper(width=250)
  
        word_list = wrapper.wrap(text=str(row[1]))
        print(word_list)
        pdf.multi_cell(w=270, h=height, txt=str(sample), align='L',border=1) #agenda
        pdf.multi_cell(w=100, h=height, txt=str(row[2]), align='L',border=1) #role players
        pdf.multi_cell(w=98.5, h=height, txt=str(row[3]), align='L',border=1) # time allotted

    #end of the meeting PO
    #pdf.set_font(family='Times',size=fontSize)
    pdf.cell(w=70, h=height, txt="8:00 PM",border=1, align='C')
    pdf.cell(w=468.5, h=height, txt="President Adjourns the meeting", align='C',border=1,ln=1)
    pdf.cell(w=0, h=height, txt="Networking Session", align='C',border=1)
    pdf.output("Automate-everything-with-python/Meeting2.pdf")

df=dataframe('Automate-everything-with-python/agenda_near.csv')
pdf(df)

'''

for index, row in df.iterrows():
  pdf = FPDF(orientation='P', unit='pt', format='A4')
  pdf.add_page()

  pdf.set_font(family='Times', style='B', size=24)
  pdf.cell(w=0, h=50, txt=row['name'], align='C', ln=1)

  for column in df.columns[1:]:
    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100, h=25, txt=f"{column.title()}:")

    pdf.set_font(family='Times', size=14)
    pdf.cell(w=100, h=25, txt=row[column], ln=1)


  pdf.output(f"{row['name']}.pdf")
'''