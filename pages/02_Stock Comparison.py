import streamlit as st
import yfinance as yf
import pandas as pd
import time
#Animation
import json

import requests
from streamlit_lottie import st_lottie

st.markdown("<h1 style='text-align: center; color: white;'>WELCOME TO STOCK BOAT</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>Compare Stocks graph</h4>", unsafe_allow_html=True)


# Extracting market data
tickers=('AAPL', 'MSFT',"SPY",'WMT','SBIN.NS','MRF.NS','DJI','^NSEBANK','TSLA')

#progress bar
progress = st.progress(0)
for i in range (100):
    time.sleep(0.01)
    progress.progress(i+1)

#yfinance API
tickers_df = yf.download(tickers=tickers, period='max')

@st.cache
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ani1 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_m7f8h8mu.json")
st_lottie(
    lottie_ani1,
    speed=1,
    reverse=False,
    quality="low",
    height=400,
    width=1400,
    key=None,
)


st.header("Select asset to Compare ")
dropdown = st.multiselect( ' Select assets to Compare',tickers)
st.header('Select Specific Dates')
start = st.date_input('Start Date',value = pd.to_datetime('2021-01-01'))
end = st.date_input('End Date',value = pd.to_datetime('today'))

def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    return cumret



if len(dropdown) > 0:
    df = yf.download(dropdown,start,end)['Adj Close']
    df = relativeret(yf.download(dropdown,start,end)['Adj Close'])
    st.dataframe(df.tail(7))
    st.header('Line Chart Returns of {}'.format(dropdown))
    st.line_chart(df)
    st.header('Bar Chart Returns of {}'.format(dropdown))
    st.bar_chart(df)
    st.header('Area Chart Returns of {}'.format(dropdown))
    st.area_chart(df)
    

lottie_ani2 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_xjjlxgvw.json")
st_lottie(
    lottie_ani2,
    speed=1,
    reverse=False,
    quality="low",
    height=400,
    width=1400,
    key=None,
)
st.markdown("<h6 style='text-align: left; color: skyblue;'>© STOCK-BOAT</h6>", unsafe_allow_html=True)
###############################################################################################################################################
