import pandas as pd
import numpy as np
import pickle
import streamlit as st
import random




with open("pickle_df1.pickle", 'rb') as filename:
    df = pickle.load(filename)


회사정렬 = ['HG', 'HDI', 'HCE', 'HCM']
기준일자정렬 = ['t20210801', 't20211001', 't20220101', 't20220401', 't20220701', 't20221001', 't20230101']
고용형태정렬 = ['임원', '직원']
사원유형정렬 = ["정규임원", "전문위원", "계약임원", "상근임원", "비상근임원", "퇴임임원", "설계연구직", "사무기술직", "생산기술직", "전문직A", "사무지원/전문직B", "별정직", "일반계약직", "정년후계약직", "파견후계약직", "고용외국인", "파견직"]
직급정렬 = ["부회장급","사장급","부사장급","전무급","상무급","HL3(3)","HL3(2)","HL3(1)","HL2","HL1","HS","S3","S2","S1","사원급"]
연령대정렬 = [60, 50, 40, 30, 20]



def create_summary_df(df):
    gdf3 = df.groupby(["기준일자", "회사", "고용형태", "사원유형"])[["임시키"]].count().reset_index()
    return gdf3
    

@st.cache_data
def create_ipyvizzu_gdf(df):
    gdf = df.groupby(["기준일자", "회사", "고용형태", "사원유형", "성별","그룹핑", "연령", "Level1", "Level2", "겸직임원체크"])[["임시키"]].count().reset_index()
    gdf['기준일자']= pd.Categorical(gdf['기준일자'], categories=기준일자정렬, ordered=True)
    gdf['회사']= pd.Categorical(gdf['회사'], categories=회사정렬, ordered=True)
    gdf['고용형태']= pd.Categorical(gdf['고용형태'], categories=고용형태정렬, ordered=True)
    gdf['사원유형']= pd.Categorical(gdf['사원유형'], categories=사원유형정렬, ordered=True)
    # gdf['연령대']= pd.Categorical(gdf['연령대'], categories=연령대정렬, ordered=True)
    # gdf['직급']= pd.Categorical(gdf['직급'], categories=직급정렬, ordered=True)
    gdf.sort_values(by=["기준일자","사원유형","고용형태","회사"], inplace=True)
    gdf["기준일자"] = gdf["기준일자"].astype("str")
    gdf["회사"] = gdf["회사"].astype("str")
    gdf["고용형태"] = gdf["고용형태"].astype("str")
    gdf["사원유형"] = gdf["사원유형"].astype("str")
    # gdf["직급"] = gdf["직급"].astype("str").sort_values(ascending=True)
    # gdf["승급년차"] = gdf["직급"].astype("str").sort_values(ascending=True)
    # gdf["연령대"] = gdf["연령대"].astype("str")
    gdf.rename(columns={'임시키':'인원'}, inplace=True)
    return gdf

@st.cache_data
def 사무연구직급펀넬플롯_df(회사):
    대상기간 = ['t20210801', 't20220101', 't20230101']
    대상사원유형 = ["사무기술직", "설계연구직", "전문직A", "사무지원/전문직B"]
    gdf = df.loc[(df["회사"].isin(회사))&(df["기준일자"].isin(대상기간))&(df["사원유형"].isin(대상사원유형))]
    gdf = gdf.groupby(['직급', '기준일자','사원유형'])[["임시키"]].count().reset_index()
    gdf['직급']= pd.Categorical(gdf['직급'], categories=직급정렬, ordered=True)

    return gdf

@st.cache_data
def 사무연구연령대박스플롯_df(회사):
    대상기간 = ['t20210801', 't20220101', 't20230101']
    대상사원유형 = ["사무기술직", "설계연구직", "전문직A", "사무지원/전문직B"]
    gdf = df.loc[(df["회사"].isin(회사))&(df["기준일자"].isin(대상기간))&(df["사원유형"].isin(대상사원유형))]
    gdf = gdf.groupby(['연령', '기준일자','사원유형','직급'])[["임시키"]].count().reset_index()
    return gdf

@st.cache_data
def 사무연구성별_df(회사):
    대상기간 = ['t20210801', 't20220101', 't20230101']
    대상사원유형 = ["사무기술직", "설계연구직", "전문직A", "사무지원/전문직B"]
    gdf = df.loc[(df["회사"].isin(회사))&(df["기준일자"].isin(대상기간))&(df["사원유형"].isin(대상사원유형))]
    gdf = gdf.groupby(['직급', '기준일자','성별'])[["임시키"]].count().reset_index()
    gdf['직급']= pd.Categorical(gdf['직급'], categories=직급정렬, ordered=True)

    return gdf
    
기준일자정렬 = ['t20210801', 't20211001', 't20220101', 't20220401', 't20220701', 't20221001', 't20230101']
rangeindex1 = [1, 2, 3, 4, 5,  6, 7]

@st.cache_data
def racing_df1(df):
    기준일자정렬 = ['t20210801', 't20211001', 't20220101', 't20220401', 't20220701', 't20221001', 't20230101']
    rangeindex1 = [1, 2, 3, 4, 5, 6, 7]
    df = df[df["고용형태"]=="직원"]
    gdf2 = df[['기준일자', '회사','그룹핑', 'Level1', 'Level2', '인원']]
    gdf2.reset_index(drop=True, inplace=True)
    gdf2.index = pd.RangeIndex(start=0, stop=len(gdf2['기준일자']), step=1)
    gdf2['시간순서'] = gdf2['기준일자'].copy()
    gdf2['기준일자'].replace(기준일자정렬, rangeindex1, inplace=True)
    gdf2['기준일자'].reset_index(inplace=False)
    return gdf2
    
    
##############################################################################################3


회사정렬1 = ['HG', 'HDI', 'HCE']
기준일자정렬1 = ['t20210801', 't20211001', 't20220101', 't20220401', 't20220701', 't20221001', 't20230101', 't20230401', 't20230801', 't20240101', 't20240401', 't20240801', 't20250101',
           't20250401', 't20250801', 't20260101']
고용형태정렬1 = ['직원']
사원유형정렬1 = ["사무기술직", "설계연구직"]
직급정렬1 = ["HL3(3)","HL3(2)","HL3(1)","HL2","HL1"]
연령대정렬1 = [60, 50, 40, 30, 20]



@st.cache_data
def create_ipyvizzu_gdf1(df):
    gdf = df.groupby(["기준일자", "회사", "고용형태", "사원유형", "성별","그룹핑", "연령", "Level1", "Level2"])[["임시키"]].count().reset_index()
    gdf['기준일자']= pd.Categorical(gdf['기준일자'], categories=기준일자정렬1, ordered=True)
    gdf['회사']= pd.Categorical(gdf['회사'], categories=회사정렬1, ordered=True)
    gdf['고용형태']= pd.Categorical(gdf['고용형태'], categories=고용형태정렬1, ordered=True)
    gdf['사원유형']= pd.Categorical(gdf['사원유형'], categories=사원유형정렬1, ordered=True)
    # gdf['연령대']= pd.Categorical(gdf['연령대'], categories=연령대정렬, ordered=True)
    # gdf['직급']= pd.Categorical(gdf['직급'], categories=직급정렬, ordered=True)
    gdf.sort_values(by=["기준일자","사원유형","고용형태","회사"], inplace=True)
    gdf["기준일자"] = gdf["기준일자"].astype("str")
    gdf["회사"] = gdf["회사"].astype("str")
    gdf["고용형태"] = gdf["고용형태"].astype("str")
    gdf["사원유형"] = gdf["사원유형"].astype("str")
    # gdf["직급"] = gdf["직급"].astype("str").sort_values(ascending=True)
    # gdf["승급년차"] = gdf["직급"].astype("str").sort_values(ascending=True)
    # gdf["연령대"] = gdf["연령대"].astype("str")
    gdf.rename(columns={'임시키':'인원'}, inplace=True)
    return gdf



###############시뮬레이션 조건#####################
random_state = 43
대상회사 = "HG"
시뮬레이션연도 = 2023
직급별퇴사율 = [0.05, 0.05, 0.05, 0.05, 0.01]     # HL1, HL2, HL3(1), HL3(2), HL3(3)
채용인원비율들 = [0.3, 0.3, 0.1, 0.02]   # HL1, HL2, HL3(1), HL3(2)
직급별승진율 = [0.2, 0.15, 0.15, 0.1]
남녀선택 = ["남성","남성","여성","남성","남성","여성","남성","남성","여성","남성"]  # 7:3
채용대상직급 = ["HL1", "HL2", "HL3(1)", "HL3(2)"]


def get_뉴승급년차(승급년도):
    global 시뮬레이션연도
    try:
        if 승급년도 is None:
            return 0
        else:
            return 시뮬레이션연도 - int(승급년도) + 1
    except:
        pass
    
# 해 넘어가는 함수 (연령 +1)
def get_새해연령(age):
    return int(age) + 1

# 연령대 함수
def add_age_range(age):
    return int(np.floor(age/10)*10)

def 사무설계연구퇴직(df1, 기준일자):
    global random_state
    global 직급별퇴사율
    # 타겟 df 잡기
    target_df1 = df1.copy()
#     print(f"퇴사전 총원 : {len(target_df1.index)}")

    
    # 정년퇴직자 날리기
    print(f"정년퇴직: {len(target_df1[target_df1['연령'] == 60])}")
    target_df1 = target_df1[target_df1["연령"] != 60]
    
    # 퇴사율 가정에 다른 직급별 퇴사인원
    사원퇴사인원 = int(np.round(len(target_df1.loc[(target_df1["직급"]=="HL1")].index) *직급별퇴사율[0],0))
    대리퇴사인원 = int(np.round(len(target_df1.loc[(target_df1["직급"]=="HL2")].index) * 직급별퇴사율[1],0))
    과장퇴사인원 = int(np.round(len(target_df1.loc[(target_df1["직급"]=="HL3(1)")].index) * 직급별퇴사율[2],0))
    차장퇴사인원 = int(np.round(len(target_df1.loc[(target_df1["직급"]=="HL3(2)")].index) * 직급별퇴사율[3],0))
    부장퇴사인원 = int(np.round(len(target_df1[target_df1["직급"]=="HL3(3)"].index) * 직급별퇴사율[4],0))
#     print(f"퇴사인원 - 사원:{사원퇴사인원}, 대리:{대리퇴사인원}, 과장퇴사:{과장퇴사인원}, 차장퇴사:{차장퇴사인원}, 부장퇴사:{부장퇴사인원}")
    
    # 실제 퇴사인원 index 랜덤으로 잡아내기
    사원퇴사자 = target_df1.loc[(target_df1['직급']=='HL1')|(target_df1['직급']=='HS')].sample(n=사원퇴사인원, random_state=random_state)
    대리퇴사자 = target_df1.loc[(target_df1['직급']=='HL2')].sample(n=대리퇴사인원, random_state=random_state)
    과장퇴사자 = target_df1.loc[(target_df1["직급"]=="HL3(1)")].sample(n=과장퇴사인원, random_state=random_state)
    차장퇴사자 = target_df1.loc[(target_df1["직급"]=="HL3(2)")].sample(n=차장퇴사인원, random_state=random_state)
    부장퇴사자 = target_df1[target_df1["직급"]=="HL3(3)"].sample(n=부장퇴사인원, random_state=random_state)
#     print(f"2차 검산 - 사원퇴사:{len(사원퇴사자.index)}, 대리퇴사:{len(대리퇴사자.index)}, 과장퇴사:{len(과장퇴사자.index)}, 차장퇴사:{len(차장퇴사자.index)}, 부장퇴사:{len(부장퇴사자.index)}")
    
    # 드랍할 인덱스 정리
    drop_index = []
    drop_index.extend(사원퇴사자.index)
    drop_index.extend(대리퇴사자.index)
    drop_index.extend(과장퇴사자.index)
    drop_index.extend(차장퇴사자.index)
    drop_index.extend(부장퇴사자.index)
    print(f"의원퇴사 인원 ; {len(drop_index)}")
    
    #퇴사자명단
    retired_names = []
    retired_names.extend(사원퇴사자.성명)
    retired_names.extend(대리퇴사자.성명)
    retired_names.extend(과장퇴사자.성명)
    retired_names.extend(차장퇴사자.성명)
    retired_names.extend(부장퇴사자.성명)
#     print(retired_names)
    
    # 기준일자 갱신
    target_df1.drop("기준일자", axis=1, inplace=True)
    target_df1["기준일자"] = 기준일자    
    
    
    # 인덱스 드랍
    target_df1 = target_df1.drop(drop_index)
#     print(f"퇴사후 총원 : {len(target_df1.index)}")
    
    return target_df1   


def 사무설계연구채용(df1, 회사, 채용시점):
    global random_state
    global 채용인원비율들
    global 채용대상직급
    채용_df = df1.copy()
    사원유형가방 = ["사무기술직", "설계연구직", "사무기술직", "설계연구직", "설계연구직"]


    mother_df = pd.DataFrame(columns=['임시키','기준일자','회사','고용형태', '사원유형', '직급','성명','연령','그룹핑','승급년도','성별','승급년차','연령대','Level1','Level2'])
    
    for 직급, 채용인원비율 in zip(채용대상직급, 채용인원비율들):
    
        연령범위 = 채용_df[채용_df["직급"] == 직급]["연령"].quantile([.0, .5]).values.tolist()
#         print(f"연령범위 quantile([.0, .5]) : {연령범위}")
        승급년도범위 = 채용_df[채용_df["직급"] == 직급]["승급년도"].value_counts()[:3].index.tolist()
#         print(f"승급년도범위 value_counts()[:3] : {승급년도범위}")
        그룹핑범위 = 채용_df[채용_df["직급"] == 직급]["그룹핑"].tolist()
    #     print(f"그룹핑범위: {그룹핑범위}")
        채용인원 = int(np.round(len(채용_df[채용_df["직급"]==직급])*채용인원비율))
#         print(f"{직급} 채용인원: {채용인원}")
        
        data = {'임시키': [np.random.random() for 인원 in range(int(채용인원))],
            '기준일자': [채용시점 for 인원 in range(int(채용인원))],
            '회사': [회사 for 인원 in range(int(채용인원))],
            '고용형태': ["직원"for 인원 in range(int(채용인원))],
            '사원유형': [random.choice(사원유형가방) for 인원 in range(int(채용인원))],
            '직급': [직급 for 인원 in range(int(채용인원))],
            '성명': ["홍길동" for 인원 in range(int(채용인원))],
            '연령': [np.random.randint(연령범위[0], 연령범위[1]) for 인원 in range(int(채용인원))],
            '그룹핑': [random.choice(그룹핑범위) for 인원 in range(int(채용인원))],
            '승급년도': [random.choice(승급년도범위) for 인원 in range(int(채용인원))],
            '성별': [random.choice(남녀선택) for 인원 in range(int(채용인원))]}
        t_df = pd.DataFrame.from_dict(data)
        t_df["승급년차"] = t_df["승급년도"].apply(get_뉴승급년차)
        t_df["연령대"] =  t_df["연령"].apply(add_age_range)
        t_df["Level1"] =  t_df["그룹핑"].str.split("_").str[0]
        t_df["Level2"] =  t_df["그룹핑"].str.split("_").str[1]
        
        mother_df = pd.concat([mother_df, t_df], axis=0)
    print(f"채용인원: {len(mother_df['기준일자'])}")
    recruit_df = pd.concat([채용_df, mother_df], axis=0)
    recruit_df.drop(columns = "기준일자")
    recruit_df["기준일자"] = 채용시점
#     print(f"채용후 shape : {recruit_df.shape}")

    return recruit_df

def 사무설계연구승급(df1, 승급기준일):
    global 직급별승진율

    target_df3 = df1.copy()
    
    승급기준일 = 승급기준일    # 예시 "t20230101"
    새승급년도 = 승급기준일[1:5]
#     print(f"승급기준일: {승급기준일}, 승급년도: {새승급년도}")

    
    대리승진대상 = target_df3.loc[(target_df3["직급"] == "HL1")&(target_df3["승급년차"] >= 4)]["임시키"].tolist()
    과장승진대상 = target_df3.loc[(target_df3["직급"] == "HL2")&(target_df3["승급년차"] >= 4)]["임시키"].tolist()
    차장승진대상 = target_df3.loc[(target_df3["직급"] == "HL3(1)")&(target_df3["승급년차"] >= 5)]["임시키"].tolist()
    부장승진대상 = target_df3.loc[(target_df3["직급"] == "HL3(2)")&(target_df3["승급년차"] >= 5)]["임시키"].tolist()
#     print(f"표준년한 이상 승진대상 - 대리: {len(대리승진대상)} 과장: {len(과장승진대상)}, 차장: {len(차장승진대상)} 부장: {len(부장승진대상)}")
    
    대리승진인원 = np.round(len(대리승진대상) * float(직급별승진율[0]))
    과장승진인원 = np.round(len(과장승진대상) * float(직급별승진율[1]))
    차장승진인원 = np.round(len(차장승진대상) * float(직급별승진율[2]))
    부장승진인원 = np.round(len(부장승진대상) * float(직급별승진율[3]))
    
#     print(f"승진율 적용 승진인원 - 대리: {대리승진인원} 과장: {과장승진인원}, 차장: {차장승진인원} 부장: {부장승진인원}")
    
    대리승진자 = [random.choice(대리승진대상) for i in range(int(대리승진인원))]
    과장승진자 = [random.choice(과장승진대상) for i in range(int(과장승진인원))]
    차장승진자 = [random.choice(차장승진대상) for i in range(int(차장승진인원))]
    부장승진자 = [random.choice(부장승진대상) for i in range(int(부장승진인원))]
    
    승진자임시키 = []
    승진자임시키.extend(대리승진자)
    승진자임시키.extend(과장승진자)
    승진자임시키.extend(차장승진자)
    승진자임시키.extend(부장승진자)
#     print(승진자임시키)
    
    
    승진자명단 = []
    승진자명단.extend(target_df3.loc[(target_df3["임시키"].isin(대리승진자)),"성명"].tolist())
    승진자명단.extend(target_df3.loc[(target_df3["임시키"].isin(과장승진자)),"성명"].tolist())
    승진자명단.extend(target_df3.loc[(target_df3["임시키"].isin(차장승진자)),"성명"].tolist())
    승진자명단.extend(target_df3.loc[(target_df3["임시키"].isin(부장승진자)),"성명"].tolist())
#     print(승진자명단)
    
    #승급자 직급 및 승급일자 업데이트 
    target_df3.loc[target_df3["임시키"].isin(대리승진자), "직급"] = "HL2"
    target_df3.loc[target_df3["임시키"].isin(대리승진자), "승급년도"] = 새승급년도
    target_df3.loc[target_df3["임시키"].isin(과장승진자), "직급"] = "HL3(1)"
    target_df3.loc[target_df3["임시키"].isin(과장승진자), "승급년도"] = 새승급년도
    target_df3.loc[target_df3["임시키"].isin(차장승진자), "직급"] = "HL3(2)"
    target_df3.loc[target_df3["임시키"].isin(차장승진자), "승급년도"] = 새승급년도
    target_df3.loc[target_df3["임시키"].isin(부장승진자), "직급"] = "HL3(3)"
    target_df3.loc[target_df3["임시키"].isin(부장승진자), "승급년도"] = 새승급년도
    
    # 승급시킨후, 기준일자 갱신 (연령+1, 승급년차 +1)
    target_df3.drop("기준일자", axis=1)
    target_df3["기준일자"] = 승급기준일
    
    target_df3["연령"] = target_df3["연령"].apply(get_새해연령)
    
    target_df3.drop("승급년차", axis=1)
    target_df3["승급년차"] = target_df3["승급년도"].apply(get_뉴승급년차)
    직급정렬1 = ["HL3(3)","HL3(2)","HL3(1)","HL2","HL1"]

    target_df3['직급']= pd.Categorical(target_df3['직급'], categories=직급정렬1, ordered=True)
    target_df3.sort_values(by=["기준일자","직급","사원유형","고용형태","회사"], inplace=True)
    return target_df3
    











############################################################################################  
if __name__ == "__main__":
    t_df = create_ipyvizzu_gdf(df)
    # print(df.columns)

    # print(df[df["회사"]=="HG"]["기준일자"].unique())

    # print(t_df[t_df["회사"]=="HDI"]["기준일자"].unique())
    gdf1 = create_ipyvizzu_gdf(df)
    print(racing_df1(gdf1).info())













