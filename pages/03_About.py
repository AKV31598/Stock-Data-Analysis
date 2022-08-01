import streamlit as st
#Animation
import json

import requests
from streamlit_lottie import st_lottie

st.markdown("<h1 style='text-align: center; color: white;'>ABOUT US </h3>", unsafe_allow_html=True)
st.subheader('This is a python language based Stock Data analysis App Using Streamlit, which shows graphical representations of the Stock Market Data.')

##################################################################################################################################################

@st.cache
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ani1 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_tljjahng.json")
st_lottie(
    lottie_ani1,
    speed=1,
    reverse=False,
    quality="low",
    height=400,
    width=1400,
    key=None,
)

st.subheader('This Project has been made by Ayush kumar Vishwakarma and Yash Bante from Master of Computer Applications')

lottie_ani3 = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_qwwsom67.json")
st_lottie(
    lottie_ani3,
    speed=1,
    reverse=False,
    quality="low",
    height=900,
    width=1400,
    key=None,
)
st.markdown("<h1 style='text-align: center; color: white;'>Contact </h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: white;'>Ayush Kr. Vishwakarma (ayush31598@gmail.com) </h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: white;'>Yash Bante (yashbante410@gmail.com) </h5>", unsafe_allow_html=True)
st.write("check out this[link](www.linkedin.com/in/ayush-vishwakarma-054037194)")
st.markdown("<h6 style='text-align:center; color: skyblue;'> ©STOCK-BOAT </h6>", unsafe_allow_html=True)
######################################