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
        return f"{val} λͺ"
    else:
        return ""
      
col01, col02 = st.columns([1, 2])
with col01:
    st.title(" π :red[HR] :blue[Data] Story")
with col02:
    col1001, col1002, col1003 = st.columns(3)
    with col1001:
        select001 =st.multiselect('π’ **νμ¬ μ ν (λ³΅μ μ ν κ°λ₯)**', ['HG', 'HDI', 'HCE', 'HCM'], ['HG'], key="νμ¬0")
    with col1002:
        select002 =st.selectbox('π **κΈ°μ€ μμ **', ['t20230101', 't20221001', 't20220701', 't20220401', 't20220101'], key="κΈ°μ€μΌμ0")
    with col1003:
        select003 =st.selectbox('π **λΉκ΅ μμ **', ['t20221001', 't20220701', 't20220401', 't20220101'], key="κΈ°μ€μΌμ1")
        
        
    μμ1 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select002)&(gdf4["κ³ μ©νν"]=="μμ")]["μμν€"].sum()
    μ€κ³μ°κ΅¬μ§1 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select002)&(gdf4["μ¬μμ ν"]=="μ€κ³μ°κ΅¬μ§")]["μμν€"].sum()
    μ¬λ¬΄κΈ°μ μ§1 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select002)&(gdf4["μ¬μμ ν"]=="μ¬λ¬΄κΈ°μ μ§")]["μμν€"].sum()
    μ λ¬Έμ§A1 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select002)&(gdf4["μ¬μμ ν"]=="μ λ¬Έμ§A")]["μμν€"].sum()
    μ¬λ¬΄μ§μμ λ¬Έμ§B1 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select002)&(gdf4["μ¬μμ ν"]=="μ¬λ¬΄μ§μ/μ λ¬Έμ§B")]["μμν€"].sum()
    μμ°μ§1 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select002)&(gdf4["μ¬μμ ν"]=="μμ°κΈ°μ μ§")]["μμν€"].sum()
    λ³μ μ§1 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select002)&(gdf4["μ¬μμ ν"]=="λ³μ μ§")]["μμν€"].sum()
    μμ°λ³μ μ§1 = int(μμ°μ§1) + int(λ³μ μ§1)
    μ΄μ1 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select002)]["μμν€"].sum()

    μμ2 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select003)&(gdf4["κ³ μ©νν"]=="μμ")]["μμν€"].sum()
    μ€κ³μ°κ΅¬μ§2 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select003)&(gdf4["μ¬μμ ν"]=="μ€κ³μ°κ΅¬μ§")]["μμν€"].sum()
    μ¬λ¬΄κΈ°μ μ§2 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select003)&(gdf4["μ¬μμ ν"]=="μ¬λ¬΄κΈ°μ μ§")]["μμν€"].sum()
    μ λ¬Έμ§A2 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select003)&(gdf4["μ¬μμ ν"]=="μ λ¬Έμ§A")]["μμν€"].sum()
    μ¬λ¬΄μ§μμ λ¬Έμ§B2 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select003)&(gdf4["μ¬μμ ν"]=="μ¬λ¬΄μ§μ/μ λ¬Έμ§B")]["μμν€"].sum()
    μμ°μ§2 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select003)&(gdf4["μ¬μμ ν"]=="μμ°κΈ°μ μ§")]["μμν€"].sum()
    λ³μ μ§2 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select003)&(gdf4["μ¬μμ ν"]=="λ³μ μ§")]["μμν€"].sum()
    μμ°λ³μ μ§2 = int(μμ°μ§2) + int(λ³μ μ§2)
    μ΄μ2 = gdf4.loc[(gdf4["νμ¬"].isin(select001))&(gdf4["κΈ°μ€μΌμ"]==select003)]["μμν€"].sum()
    
    μμλ³λ = μμ1 - μμ2
    μ€κ³μ°κ΅¬λ³λ = μ€κ³μ°κ΅¬μ§1 - μ€κ³μ°κ΅¬μ§2
    μ¬λ¬΄κΈ°μ λ³λ = μ¬λ¬΄κΈ°μ μ§1 - μ¬λ¬΄κΈ°μ μ§2
    μ λ¬Έμ§Aλ³λ = μ λ¬Έμ§A1 - μ λ¬Έμ§A2
    μ¬λ¬΄μ§μμ λ¬Έμ§Bλ³λ = μ¬λ¬΄μ§μμ λ¬Έμ§B1 - μ¬λ¬΄μ§μμ λ¬Έμ§B2
    μμ°λ³μ μ§λ³λ = μμ°λ³μ μ§1 - μμ°λ³μ μ§2
    μ΄μλ³λ = μ΄μ1 - μ΄μ2


    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    col1.metric("**:blue[μ μ]**", f"{μμ1} λͺ", f"{check_zero(μμλ³λ)}")
    col2.metric("**:blue[μ€κ³μ°κ΅¬μ§]**", f"{μ€κ³μ°κ΅¬μ§1} λͺ", f"{check_zero(μ€κ³μ°κ΅¬λ³λ)}")
    col3.metric("**:blue[μ¬λ¬΄κΈ°μ μ§]**", f"{μ¬λ¬΄κΈ°μ μ§1} λͺ", f"{check_zero(μ¬λ¬΄κΈ°μ λ³λ)}")
    col4.metric("**:blue[μ λ¬Έμ§A]**", f"{μ λ¬Έμ§A1} λͺ", f"{check_zero(μ λ¬Έμ§Aλ³λ)}")
    col5.metric("**:blue[μ¬λ¬΄μ§μ/μ λ¬Έμ§B]**", f"{μ¬λ¬΄μ§μμ λ¬Έμ§B1} λͺ", f"{check_zero(μ¬λ¬΄μ§μμ λ¬Έμ§Bλ³λ)}")
    col6.metric("**:blue[μμ°/λ³μ μ§]**", f"{μμ°λ³μ μ§1} λͺ", f"{check_zero(μμ°λ³μ μ§λ³λ)}")
    col7.metric("**:blue[μ΄ μ]**", f"{μ΄μ1} λͺ", f"{check_zero(μ΄μλ³λ)}")
    
st.markdown("---")



#############################################################################

def story_of_present():
    global df
    global gdf1
    global gdf2
    global gdf3
    global gdf4
    
    st.subheader(":green[λΆκΈ°λ³ μΈμλ³λ νν©]")
    col1, col2, col3, col4  = st.columns([0.7, 0.5, 1.5, 0.7])
    with col1:
        select1 =st.multiselect('π **νμ¬λ₯Ό μ νν΄μ£ΌμΈμ (λ³΅μ μ ν κ°λ₯)**', ['HG', 'HDI', 'HCE', 'HCM'], ['HG', 'HDI', 'HCE', 'HCM'])
    with col2:
        select2 = st.multiselect('πͺ **κ³ μ©νν μ ν**', ['μμ', 'μ§μ'], ['μμ', 'μ§μ'])
    with col3:
        select3 = st.multiselect('βοΈ **μ¬μμ ν μ ν**', ['μ κ·μμ','μ λ¬Έμμ','κ³μ½μμ','μ¬λ¬΄κΈ°μ μ§', 'μ€κ³μ°κ΅¬μ§', 'μ λ¬Έμ§A', 'μ¬λ¬΄μ§μ/μ λ¬Έμ§B', 'μμ°κΈ°μ μ§', 'λ³μ μ§'], ['μ κ·μμ','μ λ¬Έμμ','κ³μ½μμ','μ¬λ¬΄κΈ°μ μ§', 'μ€κ³μ°κ΅¬μ§', 'μ λ¬Έμ§A', 'μ¬λ¬΄μ§μ/μ λ¬Έμ§B', 'μμ°κΈ°μ μ§', 'λ³μ μ§'])
    with col4:
        select4 = st.radio('βοΈ **κ²Έμ§ μμ μ²λ¦¬ λ°©μ μ ν**', ['κ²Έμ§μμ κ°μ¬λ³ ν¬ν¨', 'κ²Έμ§μμ μ λ΄μΈ μμ μ²λ¦¬'])

    st.markdown("---")

    st.error("μ°¨νΈ νλ¨μ μΌκ°ν νμ΄νλ₯Ό ν΄λ¦­νλ©΄ μ°¨νΈ ννκ° λ³κ²½λ©λλ€.")
    col1, col2  = st.columns([1, 1])
    with col1:
        gdf1 = gdf1.loc[(gdf1["νμ¬"].isin(select1))&((gdf1["κ³ μ©νν"].isin(select2))&(gdf1["μ¬μμ ν"].isin(select3)))]
        vz_νμ¬λ³μ΄μλ³λ(gdf1)
        
    with col2:
        gdf2 = gdf1.loc[(gdf1["νμ¬"].isin(select1))&((gdf1["κ³ μ©νν"].isin(select2))&(gdf1["μ¬μμ ν"].isin(select3)))]
        if select4 == 'κ²Έμ§μμ κ°μ¬λ³ ν¬ν¨':
            vz_νμ¬λ³μμλ³λ(gdf2)
        else: 
            vz_νμ¬λ³μμλ³λ_κ²Έμ§μ_μ λ΄μΈ(gdf2)

    st.markdown("---")

    with st.expander("βοΈ **μ¬λ¬΄/μ€κ³/μ°κ΅¬/μ λ¬Έ/μ¬λ¬΄μ§μ μμΈ λ³΄κΈ° (μ§κΈ, μ°λ Ή, μ±λ³)**"):
        
        col41, col42 = st.columns([1, 1])
        
        with col41:
            select5_41 =st.multiselect('**νμ¬ μ ν1 (λ³΅μ μ ν κ°λ₯)**', ['HG', 'HDI', 'HCE'], ['HG'])
            
            if len(select5_41) == 0:
                st.text("νμ¬λ₯Ό μ νν΄μ£ΌμΈμ.")
            else:
                tab1, tab2, tab3 = st.tabs(["**μ§κΈ κ΅¬μ‘°**", "**μ°λ Ή κ΅¬μ‘°**", "**μ±λ³ κ΅¬μ‘°**"])
                
                with tab1:
                    st.markdown("L_μ§κΈ κ΅¬μ‘°")
                    μ§κΈλ°μ€νλ‘―_df = μ¬λ¬΄μ°κ΅¬μ§κΈνλ¬νλ‘―_df(select5_41)
                    st.plotly_chart(μ¬λ¬΄μ°κ΅¬μ§κΈλ³νλ¬νλ‘―(μ§κΈλ°μ€νλ‘―_df), theme="streamlit", use_container_width=True)
                    
                with tab2:
                    st.markdown("L_μ°λ Ή κ΅¬μ‘°")
                    μ°λ Ήλλ°μ€νλ‘―_df = μ¬λ¬΄μ°κ΅¬μ°λ Ήλλ°μ€νλ‘―_df(select5_41)
                    st.plotly_chart(μ°λ Ήλ°μ€νλ‘―(μ°λ Ήλλ°μ€νλ‘―_df), theme="streamlit", use_container_width=True)

                with tab3:
                    st.markdown("L_μ±λ³ κ΅¬μ‘°")
                    μ±λ³_df1 = μ¬λ¬΄μ°κ΅¬μ±λ³_df(select5_41)
                    st.plotly_chart(μ±λ³κ΅¬μ‘°(μ±λ³_df1), theme="streamlit", use_container_width=True)

        with col42:
            select5_42 =st.multiselect('**νμ¬ μ ν2 (λ³΅μ μ ν κ°λ₯)**', ['HG', 'HDI', 'HCE'], ['HDI'])
            
            if len(select5_42) == 0:
                st.text("νμ¬λ₯Ό μ νν΄μ£ΌμΈμ.")
            else:
                tab1, tab2, tab3 = st.tabs(["**μ§κΈ κ΅¬μ‘°**", "**μ°λ Ή κ΅¬μ‘°**", "**μ±λ³ κ΅¬μ‘°**"])
                
                with tab1:
                    st.markdown("R_μ§κΈ κ΅¬μ‘°")
                    μ§κΈλ°μ€νλ‘―_df = μ¬λ¬΄μ°κ΅¬μ§κΈνλ¬νλ‘―_df(select5_42)
                    st.plotly_chart(μ¬λ¬΄μ°κ΅¬μ§κΈλ³νλ¬νλ‘―(μ§κΈλ°μ€νλ‘―_df), theme="streamlit", use_container_width=True)
                    
                with tab2:
                    st.markdown("R_μ°λ Ή κ΅¬μ‘°")
                    μ°λ Ήλλ°μ€νλ‘―_df = μ¬λ¬΄μ°κ΅¬μ°λ Ήλλ°μ€νλ‘―_df(select5_42)
                    st.plotly_chart(μ°λ Ήλ°μ€νλ‘―(μ°λ Ήλλ°μ€νλ‘―_df), theme="streamlit", use_container_width=True)

                with tab3:
                    st.markdown("R_μ±λ³ κ΅¬μ‘°")
                    μ±λ³_df2 = μ¬λ¬΄μ°κ΅¬μ±λ³_df(select5_42)
                    st.plotly_chart(μ±λ³κ΅¬μ‘°(μ±λ³_df2), theme="streamlit", use_container_width=True)
        
        
    st.markdown("---")

    st.subheader("βοΈ **μ‘°μ§ κ·Έλ£Ήλ³ μΈμνν© (μμ°/λ³μ  μ μΈ)**")
    st.success("μμ λ³λ‘ νμ¬κ° ***λμΌ/μ μ¬ μ‘°μ§κ° μΈμ/μ§κΈ κ·λͺ¨***λ₯Ό λΉκ΅ν  μ μμ΅λλ€.")
    col11, col22, col33  = st.columns([1, 1, 1])
    with col11:
        col1_1, col1_2, col1_3 = st.columns([1, 1, 1])
        with col1_1:
            comp1 = st.selectbox('**νμ¬ μ ν1**', ['HG', 'HDI', 'HCE'])
        with col1_2:
            t1 = st.selectbox('**κΈ°μ€μΌμ μ ν1**', ['t20230101', 't20220101', 't20210801'])
        with col1_3:
            νμ_μ ν1 = st.checkbox('**κ°/λΉμ¨ νμ μ ν1**')
        st.markdown("---")
        st.plotly_chart(create_sun_chart(df, comp1, t1, νμ_μ ν1), theme="streamlit", use_container_width=True)
        
    with col22:
        col2_1, col2_2, col2_3 = st.columns([1, 1, 1])
        with col2_1:
            comp2 = st.selectbox('**νμ¬ μ ν2**', ['HDI', 'HCE', 'HG'])
        with col2_2:
            t2 = st.selectbox('**κΈ°μ€μΌμ μ ν2**', ['t20230101', 't20220101', 't20210801'])
        with col2_3:
            νμ_μ ν2 = st.checkbox('**κ°/λΉμ¨ νμ μ ν2**')
        st.markdown("---")
        st.plotly_chart(create_sun_chart(df, comp2, t2, νμ_μ ν2), theme="streamlit", use_container_width=True)
        
    with col33:
        col3_1, col3_2, col3_3 = st.columns([1, 1, 1])
        with col3_1:
            comp3 = st.selectbox('**νμ¬ μ ν3**', ['HCE', 'HDI', 'HG'])
        with col3_2:
            t3= st.selectbox('**κΈ°μ€μΌμ μ ν3**', ['t20230101', 't20220101', 't20210801'])
        with col3_3:
            νμ_μ ν3 = st.checkbox('**κ°/λΉμ¨ νμ μ ν3**')  
        st.markdown("---")
        st.plotly_chart(create_sun_chart(df, comp3, t3, νμ_μ ν3), theme="streamlit", use_container_width=True)

    st.markdown("---")


    with st.expander("βοΈ **λΆκΈ°λ³ μ‘°μ§λ³ μΈμλ³λ νν© (Racing Chart)**"):
        
        st.info("μΈμ λ³λ ν¨κ³Όλ₯Ό κ·Ήμ μΌλ‘ νννκΈ° μν΄ ***μμμ  λ³λμ***μΌλ‘ ννλμ΄ μμ΅λλ€. μ€μ λ μμ°μ λ³λμλλ€.")
        col41, col42 = st.columns([2, 1])
        with col41:
            col411, col412 = st.columns([1, 1])
            with col411:
                νμ¬μ ν41 = st.selectbox('**νμ¬ μ ν41**', ['HG', 'HDI', 'HCE'])
            with col412:
                Speed = st.selectbox('**μλ μ ν** (μ«μκ° μμμλ‘ λΉ λ¦)', [2, 3, 4, 5])
            CHART = vz_racing_chart1(gdf3, νμ¬μ ν41, Speed)
            html(CHART, width=4000, height=500)
        with col42:
            st.text("κ³΅λ")
            
    st.markdown("---")
    st.markdown("end of the page - last updates on Mar 8th")
################################################################

λμμ§κΈ = ["HL1", "HL2", "HL3(1)", "HL3(2)", "HL3(3)"]


def μ¬λ¬΄μ€κ³μ°κ΅¬μλ?¬(df, νμ¬, μμκΈ°μ€μμ , ν΄μ¬μμ , μ±μ©μμ , μΉκΈμμ ):
    
    global random_state
    global λμμ§κΈ
    
    # taget_df λ§λ€κΈ°
    base_df = df.loc[(df["νμ¬"] == νμ¬) & (df["μ¬μμ ν"].isin(["μ¬λ¬΄κΈ°μ μ§", "μ€κ³μ°κ΅¬μ§"]))& (df["μ§κΈ"].isin(λμμ§κΈ))]
    # print(f"-------------{νμ¬} base_df: {base_df.shape}-----------------")

    start_df = df.loc[(df["νμ¬"] == νμ¬)&(df["κΈ°μ€μΌμ"] == μμκΈ°μ€μμ ) & (df["μ¬μμ ν"].isin(["μ¬λ¬΄κΈ°μ μ§", "μ€κ³μ°κ΅¬μ§"]))]
    print(f"-------------{νμ¬} start_df: {start_df.shape}---------------------")
    
    retire_df = μ¬λ¬΄μ€κ³μ°κ΅¬ν΄μ§(start_df, ν΄μ¬μμ )
    print(f"-------------{νμ¬} retire_df: {retire_df.shape}---------------------")

    recruit_df = μ¬λ¬΄μ€κ³μ°κ΅¬μ±μ©(retire_df, νμ¬, μ±μ©μμ )
    print(f"-------------{νμ¬} recruit_df: {recruit_df.shape}---------------------")

    promotion_df = μ¬λ¬΄μ€κ³μ°κ΅¬μΉκΈ(recruit_df, μΉκΈμμ )
    print(f"-------------{νμ¬} promotion_df: {promotion_df.shape}---------------------")

    total_df = pd.concat([base_df, retire_df, recruit_df, promotion_df], axis=0)
    # print(f"-------------{νμ¬} total_df: {total_df.shape}---------------------")
    
    return total_df
    



def story_of_future():
    st.markdown("**:blue[μ€κ³μ°κ΅¬μ§/μ¬λ¬΄κΈ°μ μ§] μΈλ ₯μ΄μ κ³ν**")
    
    # 2023λ μλ?¬λ μ΄μ
    HG_df1 = μ¬λ¬΄μ€κ³μ°κ΅¬μλ?¬(df, "HG", "t20230101", "t20230401", "t20230801", "t20240101")
    HDI_df1 = μ¬λ¬΄μ€κ³μ°κ΅¬μλ?¬(df, "HDI", "t20230101", "t20230401", "t20230801", "t20240101")
    HCE_df1 = μ¬λ¬΄μ€κ³μ°κ΅¬μλ?¬(df, "HCE", "t20230101", "t20230401", "t20230801", "t20240101")

    # 2024λ μλ?¬λ μ΄μ
    HG_df1 = μ¬λ¬΄μ€κ³μ°κ΅¬μλ?¬(HG_df1, "HG", "t20240101", "t20240401", "t20240801", "t20250101")
    HDI_df1 = μ¬λ¬΄μ€κ³μ°κ΅¬μλ?¬(HDI_df1, "HDI", "t20240101", "t20240401", "t20240801", "t20250101")
    HCE_df1 = μ¬λ¬΄μ€κ³μ°κ΅¬μλ?¬(HCE_df1, "HCE", "t20240101", "t20240401", "t20240801", "t20250101")
    
    # 2025λ μλ?¬λ μ΄μ
    HG_df1 = μ¬λ¬΄μ€κ³μ°κ΅¬μλ?¬(HG_df1, "HG", "t20250101", "t20250401", "t20250801", "t20260101")
    HDI_df1 = μ¬λ¬΄μ€κ³μ°κ΅¬μλ?¬(HDI_df1, "HDI", "t20250101", "t20250401", "t20250801", "t20260101")
    HCE_df1 = μ¬λ¬΄μ€κ³μ°κ΅¬μλ?¬(HCE_df1, "HCE", "t20250101", "t20250401", "t20250801", "t20260101")
    
    
    
    total_df = pd.concat([HG_df1, HDI_df1, HCE_df1], axis=0)
    
    κΈ°μ€μΌμλ€ = total_df.κΈ°μ€μΌμ.unique().tolist()
    select201 =st.multiselect('π **νμ¬λ₯Ό μ νν΄μ£ΌμΈμ (λ³΅μ μ ν κ°λ₯)**', ['HG', 'HDI', 'HCE'], ['HG'])
    select202 =st.multiselect('π **μ¬μμ ν (λ³΅μ μ ν κ°λ₯)**', ['μ€κ³μ°κ΅¬μ§', 'μ¬λ¬΄κΈ°μ μ§'], ['μ€κ³μ°κ΅¬μ§', 'μ¬λ¬΄κΈ°μ μ§'])

    
    total_df = total_df.loc[(total_df["νμ¬"].isin(select201))&(total_df["μ¬μμ ν"].isin(select202))]
    
    st.plotly_chart(chart1(κΈ°μ€μΌμλ€, total_df), theme="streamlit", use_container_width=True)
    
    gdf7 = create_ipyvizzu_gdf1(total_df)


    vz_μΈλ ₯μ΄μκ³ν(gdf7)



########################################################

def story_of_test():
    st.markdown("# νμ€νΈ νμ΄μ§ (κ³΅λ)")


################################################
with st.sidebar:
    st.header("**:red[HR] :blue[Data] Story**")
    sdv1 = st.selectbox('νμ΄μ§ μ ν', ["Present", "Future", "Test"])


if sdv1 == "Present":
    story_of_present()
elif sdv1 == "Future":
    story_of_future()
else:
    story_of_test()
    
    
    
