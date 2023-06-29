import streamlit as st
import pandas as pd
#import openpyxl
import helperFiles.main_file as main_file
# 
from fpdf import FPDF

def downloadPDF(file_name):
    with open(file_name, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="Download PDF",key=file_name, data=PDFbyte,file_name=file_name,mime='application/octet-stream')

def agenda():
    st.title('Automate your Role Players list and Agenda from Download Agenda')
    st.header('Please upload the excel')
    uploaded_files = st.file_uploader('Upload a file', type=['xlsx'],key='excel')
    if uploaded_files is not None:
        st.write(uploaded_files)
        df=main_file.get_final_df(uploaded_files)
        df,pdf=main_file.make_pdf(df)
        filename="Automate-everything-with-python/AgendaRolePlayerAutomation/OutPut/Final.pdf"
        pdf.output(filename)
        st.write("A demo of your agenda")
        st.write(df)
        downloadPDF(filename)


agenda()


