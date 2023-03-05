import pandas as pd
import numpy as np
import streamlit as st
from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step
import pickle
import plotly.express as px
import random
import datetime
import plotly.figure_factory as ff


st.set_page_config(page_title="HR-DataStory", page_icon=":shark", layout="wide")
random_state = 43

with open("pickle_df1.pickle", 'rb') as filename:
    df = pickle.load(filename)

def add_age_range(age):
    return int(np.floor(age/10)*10)

회사정렬 = ['HG', 'HDI', 'HCE', 'HCM']
기준일자정렬 = ['t20210801', 't20211001', 't20220101', 't20220401', 't20220701', 't20221001', 't20230101']
고용형태정렬 = ['임원', '직원']
사원유형정렬 = ["정규임원", "전문위원", "계약임원", "상근임원", "비상근임원", "퇴임임원", "설계연구직", "사무기술직", "생산기술직", "전문직A", "전문직","전문직B", "사무지원직", "별정직A", "별정직B","별정직", "일반계약직", "정년후계약직", "파견후계약직", "고용외국인", "파견직"]
직급정렬 = ["부회장급","사장급","부사장급","전무급","상무급","HL3(3)","HL3(2)","HL3(1)","HL2","HL1","HS","S3","S2","S1","사원급" ]


  
df["연령대"] = df["연령"].apply(add_age_range)
gdf = df.groupby(["기준일자", "회사","고용형태", "사원유형", "직급","그룹핑"])[["임시키"]].count().reset_index()
gdf['기준일자']= pd.Categorical(gdf['기준일자'], categories=기준일자정렬, ordered=True)
gdf['회사']= pd.Categorical(gdf['회사'], categories=회사정렬, ordered=True)
gdf['고용형태']= pd.Categorical(gdf['고용형태'], categories=고용형태정렬, ordered=True)
gdf['사원유형']= pd.Categorical(gdf['사원유형'], categories=사원유형정렬, ordered=True)
gdf['직급']= pd.Categorical(gdf['직급'], categories=직급정렬, ordered=True)
gdf.sort_values(by=["기준일자","직급","사원유형","고용형태","회사"], inplace=True)
gdf["기준일자"] = gdf["기준일자"].astype("str")
gdf["회사"] = gdf["회사"].astype("str")
gdf["고용형태"] = gdf["고용형태"].astype("str")
gdf["사원유형"] = gdf["사원유형"].astype("str")
gdf["직급"] = gdf["직급"].astype("str")
gdf.rename(columns={'임시키':'인원'}, inplace=True)


################################################################
st.title(":red[HR] :blue[Data] Story")
st.markdown("---")

st.markdown("본 페이지는 테스트 개발 중입니다.")


#############################################################################################3

def ipyvizzu1():

    data = Data()
    data.add_data_frame(gdf)
    story = Story(data = data)

    slide1 = Slide(
        Step(
            Config({"x": ["기준일자"], "y": ["회사","인원"], "label":"인원","color":"회사",
                    "title": "Slide1 - 건설기계 3사 분기별 인원변동 (Stack)"}),
        )
    )
    story.add_slide(slide1)

    slide2 = Slide(
        Step(
            Config({"x": ["기준일자","회사"], "y": ["인원"], "label":"인원","color":"회사",
                    "title": "Slide2 - 건설기계 3사 분기별 인원변동 (Unstack)"}),
        )
    )
    story.add_slide(slide2)

    slide3 = Slide(
        Step(
            Config({"x": ["회사","기준일자"], "y": ["인원"], "label":"인원","color":"회사",
                    "title": "Slide3 - 건설기계 3사 분기별 인원변동 (Unstack)"}),
        )
    )
    story.add_slide(slide3)


    slide4 = Slide(
        Step(
            Data.filter("record.회사 == 'HG'"),
            Config({"x": ["기준일자"], "y": ["고용형태","인원"], "label":"인원","color":"고용형태",
                    "title": "Slide4 - 현대제뉴인 분기별 인원변동"}),
        )
    )
    story.add_slide(slide4)

    slide5 = Slide(
        Step(
            Data.filter("record.회사 == 'HG' && record.고용형태 == '임원'"),
            Config({"x": ["기준일자"], "y": ["직급","인원"], "label":"인원","color":"직급",
                    "title": "Slide5 - 현대제뉴인 분기별 인원변동 - 임원",
                }),
        )
    )
    story.add_slide(slide5)

    slide6 = Slide()
    slide6.add_step(Step(
            Data.filter("record.회사 == 'HG'"),
            Config({"x": ["기준일자"], "y": ["고용형태","인원"], "label":"인원","color":"고용형태",
                    "title": "Slide6-1 - 현대제뉴인 분기별 인원변동"}),
        ))

    slide6.add_step(Step(
            Data.filter("record.회사 == 'HG' && record.고용형태 == '직원'"),
            Config({"x": ["기준일자"], "y": ["사원유형","인원"], "label":"인원","color":"사원유형",
                    "title": "Slide6-2- 현대제뉴인 분기별 인원변동 - 직원 - 사원유형"}),
        ))
    story.add_slide(slide6)

    slide7 = Slide(
            Step(
            Data.filter("record.회사 == 'HG' && record.고용형태 == '직원' && record.기준일자 == 't20210801'"),
            Config.polarStackedColumn(
            {
                "angle": "그룹핑",
                "radius": "인원",
                "stackedBy": "사원유형",
                "title": "Slide7 - 조직/사원유형별 인원현황(21년 8월)",
            }))
    )
    story.add_slide(slide7)

    slide8 = Slide(
            Step(
            Data.filter("record.회사 == 'HG' && record.고용형태 == '직원' && record.기준일자 == 't20220101'"),
            Config.polarStackedColumn(
            {
                "angle": "그룹핑",
                "radius": "인원",
                "stackedBy": "사원유형",
                "title": "Slide8 - 조직/사원유형별 인원현황(22년 1월)",
            }))
    )
    story.add_slide(slide8)


    slide9 = Slide(
            Step(
            Data.filter("record.회사 == 'HG' && record.고용형태 == '직원' && record.기준일자 == 't20220701'"),
            Config.polarStackedColumn(
            {
                "angle": "그룹핑",
                "radius": "인원",
                "stackedBy": "사원유형",
                "title": "Slide9 - 조직/사원유형별 인원현황(22년 7월)",
            }))
    )
    story.add_slide(slide9)


    slide10 = Slide(
            Step(
            Data.filter("record.회사 == 'HG' && record.고용형태 == '직원' && record.기준일자 == 't20230101'"),
            Config.polarStackedColumn(
            {
                "angle": "그룹핑",
                "radius": "인원",
                "stackedBy": "사원유형",
                "title": "Slide10 - 조직/사원유형별 인원현황(23년 1월)",
            }))
    )
    story.add_slide(slide10)

    story.set_feature("tooltip", True)
    story.set_size(width=800, height=500)
    story.play()

def iv_분기별총원변동현황():
    data1 = Data()
    data1.add_data_frame(gdf)
    story1 = Story(data = data1)

    slide1 = Slide(
        Step(
            Config({"x": ["기준일자"], "y": ["회사","인원"], "label":"인원","color":"회사",
                    "title": "건설기계 3사 분기별 총원 변동현황",
                "geometry": "rectangle",}),
        )
    )
    story1.add_slide(slide1)

    slide1 = Slide(
        Step(
            Config({"x": ["기준일자"], "y": ["회사","인원"], "label":"인원","color":"회사",
                    "title": "건설기계 3사 분기별 총원 변동현황",
                "geometry": "area",}),
        )
    )
    story1.add_slide(slide1)


    slide1 = Slide(
        Step(
            Config({"x": ["기준일자"], "y": ["회사","인원"], "label":"인원","color":"회사",
                    "title": "건설기계 3사 분기별 총원 변동현황",
                "geometry": "area",
                    "split": True,}),)
    )
    story1.add_slide(slide1)

    slide1 = Slide(
        Step(
            Config({"x": ["회사","기준일자"], "y": ["인원"], "label":"인원","color":"회사",
                    "title": "건설기계 3사 분기별 총원 변동현황",
                "geometry": "rectangle",}),)
    )
    story1.add_slide(slide1)


    story1.set_feature("tooltip", True)
    story1.set_size(width=800, height=500)
    story1.play()


###########################################################################################################################
tab1, tab2, tab3 = st.tabs(["비주1", "비주2", "비주3"])
with tab1:
    with st.container():
        iv_분기별총원변동현황()

with tab2:
    ipyvizzu1()

with tab3:
    print("공란")




###########################################################################################################################
def make_single_df(회사, 기준일자, 고용형태, 사원유형):
    global df
    
    base_df = df[df["기준일자"] == 기준일자]
    single_df = base_df.loc[(base_df["회사"] == 회사)&(base_df["고용형태"]==고용형태)&(base_df["사원유형"]==사원유형)]
    # print(f"{사원유형} 인원 : {len(single_df.index)}")
    
    return single_df

def create_target_df(회사, 시작기준일):
    single_df_사무기술직 = make_single_df(회사, 시작기준일, "직원", "사무기술직")
    single_df_설계연구직 = make_single_df(회사, 시작기준일, "직원", "설계연구직")
    target_df = pd.concat([single_df_사무기술직, single_df_설계연구직], axis=0).reset_index(drop=True, inplace=False)
    # print(f"target_df shape: {target_df.shape}")
    return target_df

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

def 퇴직시뮬(기준일자, 사원퇴사율, 대리퇴사율, 과장퇴사율, 차장퇴사율, 부장퇴사율):
    global random_state
    global target_df
    # 타겟 df 잡기
    target_df1 = target_df.copy()
    
    # 정년퇴직자 날리기
    target_df1 = target_df1[target_df1["연령"] != 60]
    
    # 퇴사율 가정에 다른 직급별 퇴사인원
    사원퇴사인원 = int(np.round(len(target_df1.loc[(target_df1["직급"]=="HL1")].index) *사원퇴사율,0))
    대리퇴사인원 = int(np.round(len(target_df1.loc[(target_df1["직급"]=="HL2")].index) * 대리퇴사율,0))
    과장퇴사인원 = int(np.round(len(target_df1.loc[(target_df1["직급"]=="HL3(1)")].index) * 과장퇴사율,0))
    차장퇴사인원 = int(np.round(len(target_df1.loc[(target_df1["직급"]=="HL3(2)")].index) * 차장퇴사율,0))
    부장퇴사인원 = int(np.round(len(target_df1[target_df1["직급"]=="HL3(3)"].index) * 부장퇴사율,0))
    
    # 실제 퇴사인원 index 랜덤으로 잡아내기
    사원퇴사자 = target_df1.loc[(target_df1['직급']=='HL1')|(target_df1['직급']=='HS')].sample(n=사원퇴사인원, random_state=random_state)
    대리퇴사자 = target_df1.loc[(target_df1['직급']=='HL2')].sample(n=대리퇴사인원, random_state=random_state)
    과장퇴사자 = target_df1.loc[(target_df1["직급"]=="HL3(1)")].sample(n=과장퇴사인원, random_state=random_state)
    차장퇴사자 = target_df1.loc[(target_df1["직급"]=="HL3(2)")].sample(n=차장퇴사인원, random_state=random_state)
    부장퇴사자 = target_df1[target_df1["직급"]=="HL3(3)"].sample(n=부장퇴사인원, random_state=random_state)
    
    # 드랍할 인덱스 정리
    drop_index = []
    drop_index.extend(사원퇴사자.index)
    drop_index.extend(대리퇴사자.index)
    drop_index.extend(과장퇴사자.index)
    drop_index.extend(차장퇴사자.index)
    drop_index.extend(부장퇴사자.index)
    
    #퇴사자명단
    retired_names = []
    retired_names.extend(사원퇴사자.성명)
    retired_names.extend(대리퇴사자.성명)
    retired_names.extend(과장퇴사자.성명)
    retired_names.extend(차장퇴사자.성명)
    retired_names.extend(부장퇴사자.성명)
    
    # 기준일자 갱신
    target_df1.drop("기준일자", axis=1, inplace=True)
    target_df1["기준일자"] = 기준일자    
    
    # 인덱스 드랍
    target_df1 = target_df1.drop(drop_index)

    return target_df1   

def recruit_one(채용인원비율, 기준일자, 회사, 고용형태, 사원유형, 직급):
    global target_df
    채용_df = target_df.copy()

    random.seed(random_state)
    np.random.seed(random_state) 
    
    연령범위 = 채용_df[채용_df["직급"] == 직급]["연령"].quantile([.0, .5]).values.tolist()
    승급년도범위 = 채용_df[채용_df["직급"] == 직급]["승급년도"].value_counts()[:3].index.tolist()
    그룹핑범위 = 채용_df[채용_df["직급"] == 직급]["그룹핑"].tolist()
    채용인원 = int(np.round(len(채용_df[채용_df["직급"]==직급])*채용인원비율))    

    data = {'임시키': [np.random.random() for 인원 in range(int(채용인원))],
            '기준일자': [기준일자 for 인원 in range(int(채용인원))],
            '회사': [회사 for 인원 in range(int(채용인원))],
            '고용형태': [고용형태 for 인원 in range(int(채용인원))],
            '사원유형': [사원유형 for 인원 in range(int(채용인원))],
            '직급': [직급 for 인원 in range(int(채용인원))],
            '성명': ["홍길동" for 인원 in range(int(채용인원))],
            '연령': [np.random.randint(연령범위[0], 연령범위[1]) for 인원 in range(int(채용인원))],
            '그룹핑': [random.choice(그룹핑범위) for 인원 in range(int(채용인원))],
            '승급년도': [random.choice(승급년도범위) for 인원 in range(int(채용인원))],
            '성별': [random.choice(남녀선택) for 인원 in range(int(채용인원))]
           
           }
    df = pd.DataFrame.from_dict(data)
    return df

def 채용시뮬(기준일자, 회사):
    global target_df1
    
    target_df2 = target_df1.copy()
    target_df2.drop(["기준일자"], axis=1, inplace=True)
    target_df2["기준일자"] = 기준일자
    
    HL1채용 = recruit_one(사무직급채용율[0], 기준일자, 회사, "직원", "사무기술직", "HL1")
    HL1채용["승급년차"] =  HL1채용["승급년도"].apply(get_뉴승급년차)
    HL1채용["연령대"] =  HL1채용["연령"].apply(add_age_range)
    HL1채용["Level1"] =  HL1채용["그룹핑"].str.split("_").str[0]
    HL1채용["Level2"] =  HL1채용["그룹핑"].str.split("_").str[1]

    
    HL2채용 = recruit_one(사무직급채용율[1], 기준일자, 회사, "직원", "사무기술직", "HL2")
    HL2채용["승급년차"] =  HL2채용["승급년도"].apply(get_뉴승급년차)
    HL2채용["연령대"] =  HL2채용["연령"].apply(add_age_range)
    HL2채용["Level1"] =  HL2채용["그룹핑"].str.split("_").str[0]
    HL2채용["Level2"] =  HL2채용["그룹핑"].str.split("_").str[1]
    
    
    HL3_1채용 = recruit_one(사무직급채용율[2],기준일자, 회사, "직원", "사무기술직", "HL3(1)")
    HL3_1채용["승급년차"] =  HL3_1채용["승급년도"].apply(get_뉴승급년차)
    HL3_1채용["연령대"] =  HL3_1채용["연령"].apply(add_age_range)
    HL3_1채용["Level1"] =  HL3_1채용["그룹핑"].str.split("_").str[0]
    HL3_1채용["Level2"] =  HL3_1채용["그룹핑"].str.split("_").str[1]

    
    HL3_2채용 = recruit_one(사무직급채용율[3], 기준일자, 회사, "직원", "사무기술직", "HL3(2)")
    HL3_2채용["승급년차"] =  HL3_2채용["승급년도"].apply(get_뉴승급년차)
    HL3_2채용["연령대"] =  HL3_2채용["연령"].apply(add_age_range)
    HL3_2채용["Level1"] =  HL3_2채용["그룹핑"].str.split("_").str[0]
    HL3_2채용["Level2"] =  HL3_2채용["그룹핑"].str.split("_").str[1]


    HL1채용_설 = recruit_one(설계연구직급채용율[0], 기준일자, 회사, "직원", "설계연구직", "HL1")
    HL1채용_설["승급년차"] =  HL1채용_설["승급년도"].apply(get_뉴승급년차)
    HL1채용_설["연령대"] =  HL1채용_설["연령"].apply(add_age_range)
    HL1채용_설["Level1"] =  HL1채용_설["그룹핑"].str.split("_").str[0]
    HL1채용_설["Level2"] =  HL1채용_설["그룹핑"].str.split("_").str[1]

    HL2채용_설 = recruit_one(설계연구직급채용율[1], 기준일자, 회사, "직원", "설계연구직", "HL2")
    HL2채용_설["승급년차"] =  HL2채용_설["승급년도"].apply(get_뉴승급년차)
    HL2채용_설["연령대"] =  HL2채용_설["연령"].apply(add_age_range)
    HL2채용_설["Level1"] =  HL2채용_설["그룹핑"].str.split("_").str[0]
    HL2채용_설["Level2"] =  HL2채용_설["그룹핑"].str.split("_").str[1]

    HL3_1채용_설 = recruit_one(설계연구직급채용율[2],기준일자, 회사, "직원", "설계연구직", "HL3(1)")
    HL3_1채용_설["승급년차"] =  HL3_1채용_설["승급년도"].apply(get_뉴승급년차)
    HL3_1채용_설["연령대"] =  HL3_1채용_설["연령"].apply(add_age_range)
    HL3_1채용_설["Level1"] =  HL3_1채용_설["그룹핑"].str.split("_").str[0]
    HL3_1채용_설["Level2"] =  HL3_1채용_설["그룹핑"].str.split("_").str[1]

    HL3_2채용_설 = recruit_one(설계연구직급채용율[3],기준일자, 회사, "직원", "설계연구직", "HL3(2)")
    HL3_2채용_설["승급년차"] =  HL3_2채용_설["승급년도"].apply(get_뉴승급년차)
    HL3_2채용_설["연령대"] =  HL3_2채용_설["연령"].apply(add_age_range)
    HL3_2채용_설["Level1"] =  HL3_2채용_설["그룹핑"].str.split("_").str[0]
    HL3_2채용_설["Level2"] =  HL3_2채용_설["그룹핑"].str.split("_").str[1]

    채용_df = pd.concat([HL1채용, HL2채용, HL3_1채용, HL3_2채용, HL1채용_설, HL2채용_설, HL3_1채용_설, HL3_2채용_설], axis=0)
    
    target_df3 = pd.concat([target_df2, 채용_df], axis=0)
    
    return target_df3

def 승급시뮬(승급기준일, 대리승진율, 과장승진율, 차장승진율, 부장승진율):
    global target_df1
    target_df3 = target_df1.copy()
    
    승급기준일 = 승급기준일    # 예시 "t20230101"
    새승급년도 = 승급기준일[1:5]

    
    대리승진대상 = target_df3.loc[(target_df3["직급"] == "HL1")&(target_df3["승급년차"] >= 4)]["임시키"].tolist()
#     print(f"대리승진대상: {대리승진대상}")
    과장승진대상 = target_df3.loc[(target_df3["직급"] == "HL2")&(target_df3["승급년차"] >= 4)]["임시키"].tolist()
    차장승진대상 = target_df3.loc[(target_df3["직급"] == "HL3(1)")&(target_df3["승급년차"] >= 5)]["임시키"].tolist()
    부장승진대상 = target_df3.loc[(target_df3["직급"] == "HL3(2)")&(target_df3["승급년차"] >= 5)]["임시키"].tolist()
    
    대리승진인원 = np.round(len(대리승진대상) * float(대리승진율))
    과장승진인원 = np.round(len(과장승진대상) * float(과장승진율))
    차장승진인원 = np.round(len(차장승진대상) * float(차장승진율))
    부장승진인원 = np.round(len(부장승진대상) * float(부장승진율))
        
    대리승진자 = [random.choice(대리승진대상) for i in range(int(대리승진인원))]
    과장승진자 = [random.choice(과장승진대상) for i in range(int(과장승진인원))]
    차장승진자 = [random.choice(차장승진대상) for i in range(int(차장승진인원))]
    부장승진자 = [random.choice(부장승진대상) for i in range(int(부장승진인원))]
    
    승진자임시키 = []
    승진자임시키.extend(대리승진자)
    승진자임시키.extend(과장승진자)
    승진자임시키.extend(차장승진자)
    승진자임시키.extend(부장승진자)    
    
    승진자명단 = []
    승진자명단.extend(target_df3.loc[(target_df3["임시키"].isin(대리승진자)),"성명"].tolist())
    승진자명단.extend(target_df3.loc[(target_df3["임시키"].isin(과장승진자)),"성명"].tolist())
    승진자명단.extend(target_df3.loc[(target_df3["임시키"].isin(차장승진자)),"성명"].tolist())
    승진자명단.extend(target_df3.loc[(target_df3["임시키"].isin(부장승진자)),"성명"].tolist())
    
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

    return target_df3


# 시뮬레이션 조건 세팅
시뮬레이션연도 = 2023

직급별퇴사율 = [0.05, 0.05, 0.05, 0.05, 0.01]     # HL1, HL2, HL3(1), HL3(2), HL3(3)
사무직급채용율 = [0.2, 0.1, 0.05, 0.02]   # HL1, HL2, HL3(1), HL3(2)
설계연구직급채용율 = [0.2, 0.1, 0.05, 0.02]   # HL1, HL2, HL3(1), HL3(2)
직급별승진율 = [0.2, 0.15, 0.15, 0.1]
남녀선택 = ["남성","남성","여성","남성","남성","여성","남성","남성","여성","남성"]  # 7:3

############################################################################################################################

col1, col2 = st.columns(2)
with col1:
    option1 = st.selectbox(
        '회사를 선택해주세요.',
        ('HG', 'HDI', 'HCE'))
    print(option1)
with col2:
    option2 = st.selectbox(
        '시뮬레이션시작점.',
        ('t20230101', ""))

st.markdown("---")

대상회사 = option1
시뮬레이션시작점 = option2
print(대상회사)

df = df[df["회사"] == 대상회사]
target_df = create_target_df(대상회사, 시뮬레이션시작점)
target_df1 = 퇴직시뮬("t20230601", 직급별퇴사율[0], 직급별퇴사율[1], 직급별퇴사율[2], 직급별퇴사율[3], 직급별퇴사율[4])
target_df2 = 채용시뮬("t20230701", 대상회사)
target_df3 = 승급시뮬("t20240101", 직급별승진율[0], 직급별승진율[1], 직급별승진율[2], 직급별승진율[3])
과거_df = df.loc[(df["고용형태"] == "직원") & ((df["사원유형"] == "사무기술직") | (df["사원유형"] == "설계연구직"))]
미래_df = pd.concat([target_df1, target_df2, target_df3], axis=0)
df = pd.concat([과거_df, 미래_df], axis=0)
gdf0 = target_df.groupby(['직급', '기준일자','사원유형'])[["임시키"]].count().reset_index()
gdf1 = target_df1.groupby(['직급', '기준일자','사원유형'])[["임시키"]].count().reset_index()
gdf2 = target_df2.groupby(['직급', '기준일자','사원유형'])[["임시키"]].count().reset_index()
gdf3 = target_df3.groupby(['직급', '기준일자','사원유형'])[["임시키"]].count().reset_index()
gdf = pd.concat([gdf0, gdf1, gdf2, gdf3], axis=0)


def 분기별인원변동():
    fig = px.bar(gdf, x="기준일자", y="임시키", barmode="group",opacity=0.6)
    fig.update_layout(width=1400, height=400)
    return fig

def 분기별직급별인원변동():
    fig = px.bar(gdf, x="직급", y="임시키", color="기준일자", barmode="group",hover_data=['기준일자','사원유형','임시키'],opacity=0.6,category_orders= {'직급': ["HS", "HL1", "HL2", "HL3(1)", "HL3(2)", "HL3(3)"]})
    fig.update_layout(legend_traceorder="reversed", width=1400, height=400)
    return fig


st.subheader(f"**:red[{option1}]** 분기별 인원 변동")
tab1, tab2 = st.tabs(["분기별 인원변동", "분기별/직급별 인원변동"])
with tab1:
    st.plotly_chart(분기별인원변동(), theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(분기별직급별인원변동(), theme="streamlit", use_container_width=True)


st.markdown("---")


def 직급계층현황():
    data = gdf
    y = data.직급.tolist()
    print(y)
    x = data.임시키.tolist()
    print(x)
    print(sum(x))

    # portions = [f"{np.round(i/sum(x)*100, 1)}%" for i in x]
    기준일자 = data.기준일자.tolist()
    사원유형 = data.사원유형.tolist()

    fig = px.funnel(data, x=x, y=y, facet_col=기준일자, facet_col_wrap=0, color = 사원유형, hover_name = y, opacity=0.7, 
                    category_orders= {'y': ["HL1", "HL2", "HL3(1)", "HL3(2)", "HL3(3)"]})  #text = portions, 
    fig.update_layout(legend_traceorder="reversed", width=1500, height=400)
    return fig

def 연령대계층현황():
    pass

st.subheader(f"**:red[{option1}]** 분기별 직급/연령대 박스플롯")
tab1, tab2 = st.tabs(["직급계층", "연령대계층"])
with tab1:
    st.plotly_chart(직급계층현황(), theme="streamlit", use_container_width=True)

with tab2:
    st.markdown("만들다 말았음")
    # st.plotly_chart(연령대계층현황(), theme="streamlit", use_container_width=True)


st.markdown("---")


def 승급년차박스플롯():
    total_df = pd.concat([target_df, target_df1,target_df2, target_df3], axis=0)
    total_gdf = total_df.groupby(['기준일자','직급','승급년차'])[["임시키"]].count().reset_index().round()
    fig = px.box(total_gdf, x="직급", y="승급년차", facet_col="기준일자", color="직급", category_orders= {'직급': ["HS","HL1", "HL2", "HL3(1)", "HL3(2)", "HL3(3)"]})
    fig.update_layout(legend_traceorder="reversed", width=1500, height=500)
    return fig

def 연령박스플롯():
    total_df = pd.concat([target_df, target_df1,target_df2, target_df3], axis=0)
    total_gdf = total_df.groupby(['기준일자','직급','연령'])[["임시키"]].count().reset_index().round()
    fig = px.box(total_gdf, x="직급", y="연령", facet_col="기준일자", color="직급", boxmode = 'overlay', category_orders= {'직급': ["HS","HL1", "HL2", "HL3(1)", "HL3(2)", "HL3(3)"]})
    fig.update_layout(legend_traceorder="reversed", width=1500, height=500)
    return fig


st.subheader(f"**:red[{option1}]** 분기별 박스 플롯 변동")
tab1, tab2 = st.tabs(["**분기별 직급-승급년차**", "**분기별 직급-연령**"])
with tab1:
    st.plotly_chart(승급년차박스플롯(), theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(연령박스플롯(), theme="streamlit", use_container_width=True)



def 선플라워1():
    total_df = pd.concat([target_df, target_df1,target_df2, target_df3], axis=0)
    total_gdf = total_df.groupby(['기준일자','그룹핑','Level1', 'Level2','직급','연령','성별','연령대'])[["임시키"]].count().reset_index().round()
    fig = px.sunburst(total_gdf[total_gdf["기준일자"]=="t20240101"], path=['Level1', 'Level2', '직급'], values='임시키', color='Level1')
    return fig

def 선플라워2():
    total_df = pd.concat([target_df, target_df1,target_df2, target_df3], axis=0)
    total_gdf = total_df.groupby(['기준일자','그룹핑','Level1', 'Level2','직급','연령','성별','연령대'])[["임시키"]].count().reset_index().round()
    fig = px.sunburst(total_gdf[total_gdf["기준일자"]=="t20240101"], path=['Level1', 'Level2', '연령대'], values='임시키', color='연령대')
    return fig

def 선플라워3():
    total_df = pd.concat([target_df, target_df1,target_df2, target_df3], axis=0)
    total_gdf = total_df.groupby(['기준일자','그룹핑','Level1', 'Level2','직급','연령','성별','연령대'])[["임시키"]].count().reset_index().round()
    fig = px.sunburst(total_gdf[total_gdf["기준일자"]=="t20240101"], path=['Level1', 'Level2', '성별'], values='임시키', color='성별')
    return fig



st.markdown("---")
st.subheader(f"**:red[{option1}]** 조직별 선플라워 차트 - 24년 1월 1일 (예상)")
col1, col2, col3 = st.columns(3)
with col1:
    st.plotly_chart(선플라워1(), theme="streamlit", use_container_width=True)

with col2:
    st.plotly_chart(선플라워2(), theme="streamlit", use_container_width=True)   

with col3:
    st.plotly_chart(선플라워3(), theme="streamlit", use_container_width=True)

st.markdown("---")
