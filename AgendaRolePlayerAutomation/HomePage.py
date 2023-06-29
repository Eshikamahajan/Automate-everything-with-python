import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Connected Across Miles Toastmasters Club",
    page_icon="👋",
)

#st.sidebar.success("Select a page above.")

st.title('Welcome to Connected Across Toastmasters Home Page')
Reason='We all want to expand our horizons and achieve excellence beyond boundaries'
Mission='''
To embrace diversity, learn about various cultures, and foster excellence as global citizens thereby providing a supportive and positive learning experience in which members are empowered to develop communication and leadership skills, resulting in greater self-confidence and personal growth.
'''
Vision='''Connect with Toastmasters worldwide for global networking and collaboration.
'''
Schedule='6:30 PM to 8:00 PM IST, Every Saturday'
ContactUs1='Nimisha Singla (+91-9560673339)'
ContactUs2='Gayatri Deshmukh (+91-9967274730)'
MWL='Eshika Mahajan (+91-8368746806)'
st.subheader(Reason)

st.header('Mission of our Club')
st.write(Mission)

st.header('Vision of our Club')
st.write(Vision)

st.header('Schedule')
st.write(Schedule)

st.header('Interested or Curious to know more? Contact Us')
st.write(ContactUs1)
st.write(ContactUs2)

st.header("Made with Love By ")
st.text(MWL)
#DownloadAgenda.agenda()
