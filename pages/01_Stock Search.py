from matplotlib import ticker
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime

import yfinance as yf
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator

# for sidebars and labels
st.markdown("<h1 style='text-align: center; color: white;'>WELCOME TO STOCK BOAT</h1>", unsafe_allow_html=True)
st.title('Stock Market Data Analysis')
st.subheader('Analyzing the Stock Market Data and its Fluctuations Using Graphical Representation')
option = st.sidebar.selectbox('Select Stock to View',('AMZN','AAPL', 'MSFT',"SPY",'WMT','SBIN.NS','MRF.NS','DJI','^NSEBANK','TSLA'))
#progress bar
progress = st.progress(0)
for i in range (100):
    time.sleep(0.01)
    progress.progress(i+1)
data_load_state = st.text('Loading data...')
data_load_state.text('Loading data... done!')

#data caching
@st.cache
def load_data(ticker):
    data = yf.download(ticker,TODAY)
    #START = "2021-07-21"
    TODAY = datetime.date.today().strftime("%Y-%m-%d")
    data.reset_index(inplace=True)
    return data

#side bar calender
today = datetime.date.today()
before = today - datetime.timedelta(days=700)
start_date = st.sidebar.date_input('Start date', before)
end_date = st.sidebar.date_input('End date', today)

if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')

# for Downloading the data from yahoo finance
df = yf.download(option,start= start_date,end= end_date)

# Bollinger Bands
indicator_bb = BollingerBands(df['Close'])
bb = df
bb['bb_high'] = indicator_bb.bollinger_hband()
bb['bb_low'] = indicator_bb.bollinger_lband()
bb = bb[['Close','bb_high','bb_low']]

# Moving Average Convergence Divergence
macd = MACD(df['Close']).macd()

# Resistence Strength Indicator
rsi = RSIIndicator(df['Close']).rsi()

# Set up main app
# Data of recent days
st.header('Data Frames for above Selected Assets  ')
st.dataframe(df.tail(7))


# Plot the prices and the bolinger bands
st.header('Stock Bollinger Bands')
st.line_chart(bb)

# Plotting MACD
st.header('Stock Moving Average Convergence Divergence (MACD)')
st.area_chart(macd)

# Plotting RSI
st.header('Stock Resistence Strength Indicator (RSI) ')
st.line_chart(rsi)

st.markdown("<h6 style='text-align: left; color: skyblue;'>© STOCK-BOAT</h6>", unsafe_allow_html=True)