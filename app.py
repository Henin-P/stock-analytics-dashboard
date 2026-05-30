import streamlit as st
st.title("📈 Stock Market Dashboard")

ticker = st.text_input(
    "Enter Stock Symbol",
    "RELIANCE.NS"
)

st.write("Selected Stock:", ticker)


import yfinance as yf

stock = yf.Ticker(ticker)

hist = stock.history(period="1y")
st.subheader("Historical Data")
st.dataframe(hist)
st.subheader("Price Chart")
st.line_chart(hist["Close"])

current_price = hist["Close"].iloc[-1]
st.metric(
    "Current Price",
    round(current_price,2)
)
info = stock.info

st.subheader("Company Information")
st.write(info.get("longName"))
st.write(info.get("sector"))
st.write(info.get("industry"))