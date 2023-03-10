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
from prepare_df import *
from prepare_chart import *
from streamlit.components.v1 import html


st.set_page_config(page_title="HR-DataStory", page_icon="11", layout="wide")
random_state = 43

##############################################
### Data Zone
df = df
gdf1 = create_ipyvizzu_gdf(df)
gdf3 = racing_df1(gdf1)
gdf4 = create_summary_df(df)

###############################################
# st.markdown("Session State Check")

# "Session State", st.session_state

###################################################


def check_zero(val):
    if val != 0:
        return f"{val} 명"
    else:
        return ""
    
    
col01, col02 = st.columns([1, 2])
with col01:
    st.title(" 📈 :red[HR] :blue[Data] Story")
with col02:
    col1001, col1002, col1003 = st.columns(3)
    with col1001:
        select001 =st.multiselect('🏢 **회사 선택 (복수 선택 가능)**', ['HG', 'HDI', 'HCE', 'HCM'], ['HG'], key="회사0")
    with col1002:
        select002 =st.selectbox('📆 **기준 시점**', ['t20230101', 't20221001', 't20220701', 't20220401', 't20220101'], key="기준일자0")
    with col1003:
        select003 =st.selectbox('📆 **비교 시점**', ['t20221001', 't20220701', 't20220401', 't20220101'], key="기준일자1")
        
        
    임원1 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select002)&(gdf4["고용형태"]=="임원")]["임시키"].sum()
    설계연구직1 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select002)&(gdf4["사원유형"]=="설계연구직")]["임시키"].sum()
    사무기술직1 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select002)&(gdf4["사원유형"]=="사무기술직")]["임시키"].sum()
    전문직A1 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select002)&(gdf4["사원유형"]=="전문직A")]["임시키"].sum()
    사무지원전문직B1 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select002)&(gdf4["사원유형"]=="사무지원/전문직B")]["임시키"].sum()
    생산직1 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select002)&(gdf4["사원유형"]=="생산기술직")]["임시키"].sum()
    별정직1 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select002)&(gdf4["사원유형"]=="별정직")]["임시키"].sum()
    생산별정직1 = int(생산직1) + int(별정직1)
    총원1 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select002)]["임시키"].sum()

    임원2 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select003)&(gdf4["고용형태"]=="임원")]["임시키"].sum()
    설계연구직2 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select003)&(gdf4["사원유형"]=="설계연구직")]["임시키"].sum()
    사무기술직2 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select003)&(gdf4["사원유형"]=="사무기술직")]["임시키"].sum()
    전문직A2 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select003)&(gdf4["사원유형"]=="전문직A")]["임시키"].sum()
    사무지원전문직B2 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select003)&(gdf4["사원유형"]=="사무지원/전문직B")]["임시키"].sum()
    생산직2 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select003)&(gdf4["사원유형"]=="생산기술직")]["임시키"].sum()
    별정직2 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select003)&(gdf4["사원유형"]=="별정직")]["임시키"].sum()
    생산별정직2 = int(생산직2) + int(별정직2)
    총원2 = gdf4.loc[(gdf4["회사"].isin(select001))&(gdf4["기준일자"]==select003)]["임시키"].sum()
    
    임원변동 = 임원1 - 임원2
    설계연구변동 = 설계연구직1 - 설계연구직2
    사무기술변동 = 사무기술직1 - 사무기술직2
    전문직A변동 = 전문직A1 - 전문직A2
    사무지원전문직B변동 = 사무지원전문직B1 - 사무지원전문직B2
    생산별정직변동 = 생산별정직1 - 생산별정직2
    총원변동 = 총원1 - 총원2


    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    col1.metric("**:blue[임 원]**", f"{임원1} 명", f"{check_zero(임원변동)}")
    col2.metric("**:blue[설계연구직]**", f"{설계연구직1} 명", f"{check_zero(설계연구변동)}")
    col3.metric("**:blue[사무기술직]**", f"{사무기술직1} 명", f"{check_zero(사무기술변동)}")
    col4.metric("**:blue[전문직A]**", f"{전문직A1} 명", f"{check_zero(전문직A변동)}")
    col5.metric("**:blue[사무지원/전문직B]**", f"{사무지원전문직B1} 명", f"{check_zero(사무지원전문직B변동)}")
    col6.metric("**:blue[생산/별정직]**", f"{생산별정직1} 명", f"{check_zero(생산별정직변동)}")
    col7.metric("**:blue[총 원]**", f"{총원1} 명", f"{check_zero(총원변동)}")
    
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


with st.expander("✌️ **분기별 조직별 인원변동 현황 (Racing Chart)**"):
    
    st.info("인원 변동 효과를 극적으로 표현하기 위해 ***소수점 변동식***으로 표현되어 있습니다. 실제는 자연수 변동입니다.")
    col41, col42 = st.columns([2, 1])
    with col41:
        col411, col412 = st.columns([1, 1])
        with col411:
            회사선택41 = st.selectbox('**회사 선택41**', ['HG', 'HDI', 'HCE'])
        with col412:
            Speed = st.selectbox('**속도 선택** (숫자가 작을수록 빠름)', [2, 3, 4, 5])
        CHART = vz_racing_chart1(gdf3, 회사선택41, Speed)
        html(CHART, width=4000, height=500)
    with col42:
        st.text("공란")
        
st.markdown("---")
st.markdown("end of the page - last updates on Mar 8th")



