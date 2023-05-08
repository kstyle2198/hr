import streamlit as st
from roughviz.charts import Bar

def roughviz_chart(df):

    chart = Bar(data=df, title="My Chart")
    chart.set_xlabel("Region", fontsize=2)
    chart.set_ylabel("Number", fontsize=2)

    # Render the chart in Streamlit using an iframe
    html = f'<iframe srcdoc="{chart.render()}" width="100%" height="500"></iframe>'

    st.markdown(html, unsafe_allow_html=True)