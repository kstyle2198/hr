# pip install yfinance
import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go


t_df = pd.read_csv('ticker_code.csv')
company_names = t_df["l_name"]
today = datetime.now().strftime("%Y-%m-%d")
start_date = datetime(2015,1,1)
end_date = datetime.now()

def get_info(name):
    company = yf.Ticker(name)
    return company

def get_states(name):
    company = yf.Ticker(name).financials
    return company

def get_ticker(a):
    ticker = t_df[t_df["l_name"] == a]["ticker"]
    return ticker.values[0]

def get_name(a):
    name = t_df[t_df["ticker"] == a]["l_name"]
    return name.values[0]

def stock_chart(ticker, start):
    with st.container():
        st.subheader(get_name(ticker))
        df = get_info(ticker).history(period="id", start=start, end=today)
        df_reverse = df.sort_index(ascending=False)
        
        fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df.Open,
                high=df.High,
                low=df.Low,
                close=df.Close,
                increasing_line_color= 'red', decreasing_line_color= 'blue')])

        st.plotly_chart(fig, use_container_width=True)

        with st.expander("See Details"):
            st.dataframe(df_reverse, height=200)


# Sidebar
# st.sidebar.title("Sidebar")

# opts = st.sidebar.multiselect("Choose Companies", (company_names))
# print(opts)
# tickers = []
# for opt in opts:
#     tickers.append(get_ticker(opt))
# # print(tickers)

# start_date = st.sidebar.selectbox("Select the Starting Date", ("2015-01-01", "2016-01-01", "2017-01-01", "2018-01-01", "2019-01-01","2020-01-01"))



# # Main
# st.write("# Stock Price")

# col1, col2 = st.columns(2)
# lst = [col1, col2]

# for ticker in tickers:
#     # print(int(tickers.index(ticker))%2)
#     with lst[int(tickers.index(ticker))%2]:
#         stock_chart(ticker)


# st.markdown("---")

            
# st.markdown("---")
# st.dataframe(get_states("CAT"))

