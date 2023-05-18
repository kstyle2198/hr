# pip install yfinance
from datetime import datetime
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go


t_df = pd.read_csv('ticker_code.csv')
company_names = t_df["l_name"]
today = datetime.now().strftime("%Y-%m-%d")
start_date = datetime(2015,1,1)
end_date = datetime.now()

@st.cache_resource
def get_info(name):
    company = yf.Ticker(name)
    return company

@st.cache_resource
def get_states(name):
    company = yf.Ticker(name).financials
    return company

@st.cache_resource
def get_ticker(a):
    ticker = t_df[t_df["l_name"] == a]["ticker"]
    return ticker.values[0]

@st.cache_resource
def get_name(a):
    name = t_df[t_df["ticker"] == a]["l_name"]
    return name.values[0]


def stock_chart(ticker, start, end):
    with st.container():
        st.subheader(get_name(ticker))
        df = get_info(ticker).history(period="id", start=start, end=end)
        df_reverse = df.sort_index(ascending=False)
        
        fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df.Open,
                high=df.High,
                low=df.Low,
                close=df.Close,
                increasing_line_color= 'red', decreasing_line_color= 'blue')])

        st.plotly_chart(fig, use_container_width=True)

        with st.expander(f"🥕 **See Details** ---- {yf.Ticker(ticker).info['longName']}"):
            # st.dataframe(df_reverse, height=200)
            # st.markdown(yf.Ticker(ticker).info)
            try:
                st.markdown(f"💰 enterprise value : {yf.Ticker(ticker).info['enterpriseValue']:,} {yf.Ticker(ticker).info['currency']}")
                st.markdown(f"💲 total revenue : {yf.Ticker(ticker).info['totalRevenue']:,} {yf.Ticker(ticker).info['currency']}")
                st.markdown(f"💸 revenue growth: {yf.Ticker(ticker).info['revenueGrowth']}")
                st.markdown(f"💵 ebita : {yf.Ticker(ticker).info['ebitda']:,} {yf.Ticker(ticker).info['currency']}")
                st.markdown(f"💶 ebita margin : {yf.Ticker(ticker).info['ebitdaMargins']}")

            except:
                st.markdown("해당 값을 제공하지 않습니다.")
            

