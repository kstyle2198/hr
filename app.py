import pandas as pd
import numpy as np
import streamlit as st
from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step
import plotly.express as px
import random
import time
import datetime
import plotly.figure_factory as ff
from repo import *
from chart import *
from streamlit.components.v1 import html


st.set_page_config(page_title="HR-DataStory", page_icon="11", layout="wide")


random_state = 43

##############################################
### Data Zone
df = df
gdf1 = create_ipyvizzu_gdf(df)


###############################################
col01, col02 = st.columns([1, 1])
with col01:
    st.title(" 📉 :red[HR] :blue[Data] Story")
with col02:
    st.markdown("공사중 - 대표 숫자 위치")
st.markdown("---")


st.subheader(":green[분기별 인원변동 현황]")

col1, col2, col3, col4  = st.columns([0.7, 0.5, 1.5, 0.7])
with col1:
    select1 =st.multiselect('👆 **회사를 선택해주세요 (복수 선택 가능)**', ['HG', 'HDI', 'HCE', 'HCM'], ['HG', 'HDI', 'HCE', 'HCM'])
with col2:
    select2 = st.multiselect('🪄 **고용형태 선택**', ['임원', '직원'], ['임원', '직원'])
with col3:
    select3 = st.multiselect('✏️ **사원유형 선택**', ['정규임원','전문위원','계약임원','사무기술직', '설계연구직', '전문직A', '사무지원/전문직B', '생산기술직', '별정직'], ['정규임원','전문위원','계약임원','사무기술직', '설계연구직', '전문직A', '사무지원/전문직B', '생산기술직', '별정직'])
with col4:
    select4 = st.radio('✔️ **겸직 임원 처리 방식 선택**', ['겸직임원 각사별 포함', '겸직임원 제뉴인 소속 처리'])

st.markdown("---")
st.error("차트 하단의 삼각형 화살표를 클릭하면 차트 형태가 변경됩니다.")

col1, col2  = st.columns([1, 1])
with col1:
    gdf1 = gdf1.loc[(gdf1["회사"].isin(select1))&((gdf1["고용형태"].isin(select2))&(gdf1["사원유형"].isin(select3)))]
    vz_회사별총원변동(gdf1)
    
with col2:
    gdf2 = gdf1.loc[(gdf1["회사"].isin(select1))&((gdf1["고용형태"].isin(select2))&(gdf1["사원유형"].isin(select3)))]
    if select4 == '겸직임원 각사별 포함':
        vz_회사별임원변동(gdf2)
    else: 
        vz_회사별임원변동_겸직은_제뉴인(gdf2)
        



st.markdown("---")
with st.expander("✌️ **사무/설계/연구/전문/사무지원 상세 보기 (직급, 연령, 성별)**"):
    
    col41, col42 = st.columns([1, 1])
    
    with col41:
        select5_41 =st.multiselect('**회사 선택1 (복수 선택 가능)**', ['HG', 'HDI', 'HCE'], ['HG'])
        
        if len(select5_41) == 0:
            st.text("회사를 선택해주세요.")
        else:
            tab1, tab2, tab3 = st.tabs(["**직급 구조**", "**연령 구조**", "**성별 구조**"])
            
            with tab1:
                st.markdown("L_직급 구조")
                직급박스플롯_df = 사무연구직급펀넬플롯_df(select5_41)
                st.plotly_chart(사무연구직급별펀넬플롯(직급박스플롯_df), theme="streamlit", use_container_width=True)
                
            with tab2:
                st.markdown("L_연령 구조")
                연령대박스플롯_df = 사무연구연령대박스플롯_df(select5_41)
                st.plotly_chart(연령박스플롯(연령대박스플롯_df), theme="streamlit", use_container_width=True)

            with tab3:
                st.markdown("L_성별 구조")
                성별_df1 = 사무연구성별_df(select5_41)
                st.plotly_chart(성별구조(성별_df1), theme="streamlit", use_container_width=True)

    with col42:
        select5_42 =st.multiselect('**회사 선택2 (복수 선택 가능)**', ['HG', 'HDI', 'HCE'], ['HDI'])
        
        if len(select5_42) == 0:
            st.text("회사를 선택해주세요.")
        else:
            tab1, tab2, tab3 = st.tabs(["**직급 구조**", "**연령 구조**", "**성별 구조**"])
            
            with tab1:
                st.markdown("R_직급 구조")
                직급박스플롯_df = 사무연구직급펀넬플롯_df(select5_42)
                st.plotly_chart(사무연구직급별펀넬플롯(직급박스플롯_df), theme="streamlit", use_container_width=True)
                
            with tab2:
                st.markdown("R_연령 구조")
                연령대박스플롯_df = 사무연구연령대박스플롯_df(select5_42)
                st.plotly_chart(연령박스플롯(연령대박스플롯_df), theme="streamlit", use_container_width=True)

            with tab3:
                st.markdown("R_성별 구조")
                성별_df2 = 사무연구성별_df(select5_42)
                st.plotly_chart(성별구조(성별_df2), theme="streamlit", use_container_width=True)
    
    
st.markdown("---")
st.subheader("✒️ **조직 그룹별 인원현황 (생산/별정 제외)**")
st.success("시점별로 회사간 ***동일/유사 조직간 인원/직급 규모***를 비교할 수 있습니다.")


col11, col22, col33  = st.columns([1, 1, 1])
with col11:
    col1_1, col1_2, col1_3 = st.columns([1, 1, 1])
    with col1_1:
        comp1 = st.selectbox('**회사 선택1**', ['HG', 'HDI', 'HCE'])
    with col1_2:
        t1 = st.selectbox('**기준일자 선택1**', ['t20230101', 't20220101', 't20210801'])
    with col1_3:
        표시_전환1 = st.checkbox('**값/비율 표시 전환1**')

    st.markdown("---")
    st.plotly_chart(create_sun_chart(df, comp1, t1, 표시_전환1), theme="streamlit", use_container_width=True)
    
with col22:
    col2_1, col2_2, col2_3 = st.columns([1, 1, 1])
    with col2_1:
        comp2 = st.selectbox('**회사 선택2**', ['HDI', 'HCE', 'HG'])
    with col2_2:
        t2 = st.selectbox('**기준일자 선택2**', ['t20230101', 't20220101', 't20210801'])
    with col2_3:
        표시_전환2 = st.checkbox('**값/비율 표시 전환2**')

    st.markdown("---")
    st.plotly_chart(create_sun_chart(df, comp2, t2, 표시_전환2), theme="streamlit", use_container_width=True)
    
with col33:
    col3_1, col3_2, col3_3 = st.columns([1, 1, 1])
    with col3_1:
        comp3 = st.selectbox('**회사 선택3**', ['HCE', 'HDI', 'HG'])
    with col3_2:
        t3= st.selectbox('**기준일자 선택3**', ['t20230101', 't20220101', 't20210801'])
    with col3_3:
        표시_전환3 = st.checkbox('**값/비율 표시 전환3**')
        
    st.markdown("---")
    st.plotly_chart(create_sun_chart(df, comp3, t3, 표시_전환3), theme="streamlit", use_container_width=True)

st.markdown("---")



gdf2 = racing_df1(gdf1)
    
with st.expander("✌️ **분기별 조직별 인원변동 현황 (Racing Chart)**"):
    
    st.info("인원 변동 효과를 극적으로 표현하기 위해 ***소수점 변동식***으로 표현되어 있습니다. 실제는 자연수 변동입니다.")

    col41, col42 = st.columns([2, 1])
    with col41:
        col411, col412 = st.columns([1, 1])
        with col411:
            회사선택41 = st.selectbox('**회사 선택41**', ['HG', 'HDI', 'HCE'])
        with col412:
            Speed = st.selectbox('**속도 선택** (숫자가 작을수록 빠름)', [2, 3, 4, 5])
        CHART = vz_racing_chart1(gdf2, 회사선택41, Speed)
        html(CHART, width=4000, height=500)

    with col42:
        st.text("공란")

st.markdown("end of the page - last updates on Mar 8th")



