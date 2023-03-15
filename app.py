import pandas as pd
import numpy as np
import streamlit as st
from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step
import plotly.express as px
# import random
# import time
# import datetime
import plotly.figure_factory as ff
from prepare_df import *
from prepare_chart import *
from streamlit.components.v1 import html
from PIL import Image


st.set_page_config(page_title="HR-DataStory", page_icon="11", layout="wide")
random_state = 10

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



#############################################################################

def story_of_present():
    global df
    global gdf1
    global gdf2
    global gdf3
    global gdf4
    
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
        col41, col42 = st.columns([9, 1])
        with col41:
            col411, col412 = st.columns([1, 1])
            with col411:
                회사선택41 = st.selectbox('**회사 선택41**', ['HG', 'HDI', 'HCE'])
            with col412:
                Speed = st.selectbox('**속도 선택** (숫자가 작을수록 빠름)', [2, 3, 4, 5])
            CHART = vz_racing_chart1(gdf3, 회사선택41, Speed)
            html(CHART, height=500)
        with col42:
            st.text("공란")
            
    st.markdown("---")
################################################################


image1 = Image.open('./images/Data-Science.jpeg')

def 사무설계연구시뮬(df, 회사, 시작기준시점, 퇴사시점, 채용시점, 승급시점, random_state, 직급별퇴사율, 채용인원비율들, 직급별승진율):
    
    남녀선택 = ["남성","남성","여성","남성","남성","여성","남성","남성","여성","남성"]  # 7:3
    대상직급 = ["HL1", "HL2", "HL3(1)", "HL3(2)", "HL3(3)"]
    채용대상직급 = ["HL1", "HL2", "HL3(1)", "HL3(2)"]
    
    직급별퇴사율 = 직급별퇴사율
    채용인원비율들 = 채용인원비율들
    직급별승진율 = 직급별승진율
    
    # base_df 만들기
    base_df = df.loc[(df["회사"] == 회사) & (df["사원유형"].isin(["사무기술직", "설계연구직"]))& (df["직급"].isin(대상직급))]
    # print(f"-------------{회사} base_df: {base_df.shape}-----------------")

    start_df = df.loc[(df["회사"] == 회사)&(df["기준일자"] == 시작기준시점) & (df["사원유형"].isin(["사무기술직", "설계연구직"]))]
    print(f"-------------{회사} start_df: {start_df.shape}---------------------")
    
    retire_df = 사무설계연구퇴직(start_df, 퇴사시점, 직급별퇴사율, random_state)[0]
    퇴직인원 = 사무설계연구퇴직(start_df, 퇴사시점, 직급별퇴사율, random_state)[1]
    print(퇴직인원)
    print(f"-------------{회사} retire_df: {retire_df.shape}---------------------")

    recruit_df = 사무설계연구채용(retire_df, 회사, 채용시점, random_state, 채용인원비율들, 채용대상직급, 남녀선택)[0]
    채용인원 = 사무설계연구채용(retire_df, 회사, 채용시점, random_state, 채용인원비율들, 채용대상직급, 남녀선택)[1]
    print(채용인원)
    print(f"-------------{회사} recruit_df: {recruit_df.shape}---------------------")

    promotion_df = 사무설계연구승급(recruit_df, 승급시점, 직급별승진율)[0]
    승급인원 = 사무설계연구승급(recruit_df, 승급시점, 직급별승진율)[1]
    print(승급인원)
    print(f"-------------{회사} promotion_df: {promotion_df.shape}---------------------")

    total_df = pd.concat([base_df, retire_df, recruit_df, promotion_df], axis=0)
    
    퇴사입사승급인원 = {"퇴사": 퇴직인원, "입사": 채용인원, "승급": 승급인원}
    # print(f"-------------{회사} total_df: {total_df.shape}---------------------")
    
    return total_df, 퇴사입사승급인원
    




def story_of_future1():
    
    global random_state
    
    with st.form("sim-conditions1"):
        st.markdown("#### **🤔 Simulation Conditions(1)**")
        select201 =st.selectbox('✅ **회사를 선택해주세요**', ['HG', 'HDI', 'HCE'])
        select202 =st.multiselect('👆 **사원유형 (복수 선택 가능)**', ['설계연구직', '사무기술직'], ['설계연구직', '사무기술직'])
        

        
        st.markdown("**😥 직급별 퇴사율**")
        co1501, col502, col503, col504, col505 = st.columns([1, 1, 1, 1, 1])
        with co1501:
            사원퇴사율 = st.selectbox(":green[HL1 퇴사율]", [0.05, 0.10, 0.08, 0.04, 0.03])
        with col502:
            대리퇴사율 = st.selectbox(":green[HL2 퇴사율]", [0.05, 0.10, 0.08, 0.04, 0.03])
        with col503:
            과장퇴사율 = st.selectbox(":green[HL3(1) 퇴사율]", [0.04, 0.08, 0.04, 0.03])
        with col504:
            차장퇴사율 = st.selectbox(":green[HL3(2) 퇴사율]", [0.03, 0.04, 0.02, 0.01])
        with col505:
            부장퇴사율 = st.selectbox(":green[HL3(3) 퇴사율]", [0.01, 0.03])   
        직급별퇴사율 = [사원퇴사율, 대리퇴사율, 과장퇴사율, 차장퇴사율, 부장퇴사율]

        st.markdown("**❤️ 직급별 채용율**")
        co1601, col602, col603, col604 = st.columns([1, 1, 1, 1])
        with co1601:
            사원채용율 = st.selectbox(":green[HL1 채용율]", [0.3, 0.2, 0.1, 0.05])
        with col602:
            대리채용율 = st.selectbox(":green[HL2 채용율]", [0.3, 0.2, 0.1, 0.05])
        with col603:
            과장채용율 = st.selectbox(":green[HL3(1) 채용율]", [0.2, 0.1, 0.08, 0.05])
        with col604:
            차장채용율 = st.selectbox(":green[HL3(2) 채용율]", [0.1, 0.08, 0.05, 0.03])
        채용인원비율들 = [사원채용율, 대리채용율, 과장채용율, 차장채용율]
        
        st.markdown("**🐬 직급별 승진율**")
        co1601, col602, col603, col604 = st.columns([1, 1, 1, 1])
        with co1601:
            대리승진율 = st.selectbox(":green[HL2 승진율]", [0.7, 0.5, 0.3])
        with col602:
            과장승진율 = st.selectbox(":green[HL3(1) 승진율]", [0.4, 0.3, 0.1])
        with col603:
            차장승진율 = st.selectbox(":green[HL3(2) 승진율]", [0.2, 0.1, 0.08, 0.05])
        with col604:
            부장승진율 = st.selectbox(":green[HL3(3) 승진율]", [0.1, 0.08, 0.05, 0.03])
        직급별승진율 = [대리승진율, 과장승진율, 차장승진율, 부장승진율]        
        
        st.markdown("---")

        # 2023년 시뮬레이션
        simul1 = 사무설계연구시뮬(df, select201, "t20230101", "t20230401", "t20230801", "t20240101", random_state, 직급별퇴사율, 채용인원비율들, 직급별승진율)
        df100 = simul1[0]
        퇴사입사승급인원_2023 = simul1[1]
        
        # 2024년 시뮬레이션
        simul2 = 사무설계연구시뮬(df100, select201, "t20240101", "t20240401", "t20240801", "t20250101", random_state, 직급별퇴사율, 채용인원비율들, 직급별승진율)
        df101 = simul2[0]
        퇴사입사승급인원_2024 = simul2[1]
        # 2025년 시뮬레이션
        simul3 = 사무설계연구시뮬(df101, select201, "t20250101", "t20250401", "t20250801", "t20260101", random_state, 직급별퇴사율, 채용인원비율들, 직급별승진율)
        df102 = simul3[0]
        퇴사입사승급인원_2025 = simul3[1]

        total_df = df102
        기준일자들 = total_df.기준일자.unique().tolist()
        
        start, end = st.select_slider(
            '**📅 Select Simulation Period**',
            options=기준일자들,
            value=('t20230101', 기준일자들[-1]))
                
        기준일자들1 = 기준일자들[기준일자들.index(start):기준일자들.index(end)+1]
        # st.write(기준일자들1)
    
        submitted1 = st.form_submit_button("**✔️ Submit1**")

        
        
        if submitted1:
            total_df = total_df.loc[(total_df["회사"] == select201)&(total_df["사원유형"].isin(select202))&(total_df["기준일자"].isin(기준일자들1))]
            gdf7 = create_ipyvizzu_gdf1(total_df)
            vz_인력운영계획(gdf7)
            
            
            # gdf10 = racing_df1(total_df)
            # col4112, col4122 = st.columns([1, 1])
            # with col4112:
            #     회사선택41 = st.selectbox('**회사 선택41**', ['HG', 'HDI', 'HCE'])
            # with col4122:
            #     Speed = st.selectbox('**속도 선택** (숫자가 작을수록 빠름)', [2, 3, 4, 5])
            # CHART = vz_racing_chart1(gdf10, 회사선택41, Speed)
            # html(CHART, height=500)

            # st.plotly_chart(chart1(기준일자들1, total_df), theme="streamlit", use_container_width=True)
            
            st.markdown(f"2023년 인원 변동 : {퇴사입사승급인원_2023}")
            st.markdown(f"2024년 인원 변동 : {퇴사입사승급인원_2024}")
            st.markdown(f"2025년 인원 변동 : {퇴사입사승급인원_2025}")
            
            st.markdown("---")            


########################################################

def story_of_test():
    st.markdown("# 테스트 페이지 (공란)")
    
    
    with st.form("my_form"):
        st.write("Simulation Conditions")
        slider_val = st.slider("Time Slider")
        checkbox_val = st.checkbox("Form checkbox")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)

    st.write("Outside the form")


################################################




with st.sidebar:
    st.header("**:red[HR] :blue[Data] Story**")
    st.markdown("---")
    sdv1 = st.selectbox('**✏️ Select Story**', ["Present", "Future", "Test"])
    st.markdown("---")
    
    st.echo("test1")




    
if sdv1 == "Present":
    story_of_present()
    
elif sdv1 == "Future":
    st.markdown("### **🌞 :blue[설계연구직/사무기술직] 인력운영 계획**")
    story_of_future1()
    st.markdown("---")
    # st.image(image1, caption='Data Image')

else:
    story_of_test()
    
  
    
