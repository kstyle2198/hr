import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

from ipyvizzu import Data, Config, Style
from ipyvizzustory import Slide, Step
from ipyvizzustory import Story  # or


st.set_page_config(page_title="HR_INSIGHT", page_icon=":bar_chart:", layout="wide")

con = sqlite3.connect("./hr.db")
df = pd.read_sql_query("SELECT * from base_info", con)
df["회사"] = df["회사"].replace("HCM", "HCE")  # 편의상 코어모션은 HCE로 변경
df["직위"] = df["직위"].replace("전문위원(상무급)", "상무").replace("전문위원(전무급)", "전무")# 편의상 코어모션은 HCE로 변경
convert_dict = {'기준일자': str}
df = df.astype(convert_dict)

def extract_df(고용형태, 사원유형):
    ex_df = df[["기준일자","회사","사번","성명","직위","고용형태", "사원유형", "그룹입사일자","당사입사일자", "승급일자", "생년월일"]]
    ex_df = ex_df[ex_df["고용형태"].isin(고용형태)]
    ex_df = ex_df[ex_df["사원유형"].isin(사원유형)]
    return ex_df

def get_age(birth_year):
    age = int(2023) - int(birth_year)
    return age

def executive_chart_by_number():
    df2 = ex_df1.sort_values(["기준일자","회사"],ascending=True).groupby(["기준일자", "회사"])[["사번"]].count().reset_index()
    df2 = df2.rename(columns={"사번": "인원"})
    convert_dict = {'기준일자': str}
    df2 = df2.astype(convert_dict)
    fig = px.bar(df2, x="기준일자", y='인원',  title="건설기계3사 분기별 임원 인원현황", color='회사', barmode='stack',
                text_auto=True,
                category_orders = {"회사": ["HCM", "HCE", "HDI", "HG"]})   #barmode='group'
    fig.update_layout(legend_traceorder="reversed", width=800, height=600)
    st.plotly_chart(fig)
    
def executive_chart_by_age():
    df2 = ex_df1.sort_values(["기준일자","회사"],ascending=True).groupby(["기준일자", "회사"])[["연령"]].mean().reset_index().round(1)
    df2 = df2.rename(columns={"연령": "평균연령"})
    convert_dict = {'기준일자': str}
    df2 = df2.astype(convert_dict)
    fig = px.bar(df2, x="기준일자", y='평균연령',  title="건설기계3사 분기별 임원 평균연령 현황", color='회사', barmode='group',
                text_auto=True,
                category_orders = {"회사": ["HCM", "HCE", "HDI", "HG"]})   #barmode='group'
    fig.update_layout(legend_traceorder="reversed", width=800, height=300)
    st.plotly_chart(fig)

# 기준 데이터프레임 생성
ex_df1 = extract_df(["정규임원", "전문위원"], ["임원", "전문위원"])
ex_df1['생년'] = ex_df1['생년월일'].str.slice(0, 4, 1)
ex_df1['생년'] = ex_df1['생년'].astype(int)
ex_df1["연령"] = ex_df1["생년"].apply(get_age)

######################################
st.title('(개발중) 건설기계 HR Insight (임원)')
st.markdown("---")

executive_chart_by_number()

st.markdown("---")


executive_chart_by_age()