import streamlit as st
import pandas as pd
from PIL import Image
MediaFolder='Automate-everything-with-python/AgendaRolePlayerAutomation/Assets/'
st.title("Meet the Executive Comittee of Connected Accross Miles Toastmasters Club")
Eshika=MediaFolder+'Eshika.png'
Nimisha=MediaFolder+'Nimisha.png'
Gayatri=MediaFolder+'Gayatri.png'

image1 = Image.open(Nimisha)
img1=image1.resize((300,300))
# st.write(Nimisha)

# st.image(image, caption="President: Nimisha Singla", width=350)

image2 = Image.open(Gayatri)
img2=image2.resize((300,300))
# st.write(Gayatri)
# st.image(image, caption="Vice President Education: Gayatri Deshmukh", width=350)

image3 = Image.open(Eshika)
img3=image3.resize((300,300))
# st.write(Eshika)
# st.image(image, caption="Secretary: Eshika Mahajan", width=350)
Captions=["President: Nimisha Singla", "Vice President Education: Gayatri Deshmukh","Secretary: Eshika Mahajan"]
st.image([img1,img2,img3], width=300, caption=Captions) 