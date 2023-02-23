import pandas as pd
import numpy as np
import streamlit as st
from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step
import pickle


st.set_page_config(page_title="회사비교", page_icon=":shark", layout="wide")

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
st.title("Human Capital Insight")
st.markdown("---")


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
story.set_size(width=600, height=400)
story.play()



col1, col2 = st.columns(2)
with col1:
    option1 = st.selectbox(
        '회사를 선택해주세요.',
        ('','HG', 'HDI', 'HCE'))
    print(option1)
with col2:
    option2 = st.selectbox(
        '고용형태를 선택해주세요.',
        ('','임원', '직원'))

st.markdown("---")
# st.dataframe(data=df, use_container_width=True)

if option1:
    gdf1 = df[df["회사"] == option1].groupby(["회사","고용형태", "사원유형", "직급"])[["임시키"]].count()
    gdf2 = df[df["회사"] == option1].groupby(['기준일자','회사','고용형태','사원유형']).agg({'임시키':'count', '연령': ['mean', 'std']}).round(1)
    gdf2.fillna("", inplace=True)
    pvdf = pd.pivot_table(df[df["회사"]==option1], index=['고용형태','사원유형'], values=['임시키'], columns = ["기준일자"], aggfunc='count')

else:
    gdf1 = df.groupby(["회사","고용형태", "사원유형", "직급"])[["임시키"]].count()
    gdf2 = df.groupby(['기준일자','회사','고용형태','사원유형']).agg({'임시키':'count', '연령': ['mean', 'std']}).round(1)
    gdf2.fillna("", inplace=True)
    pvdf = pd.pivot_table(df, index=['고용형태','사원유형'], values=['임시키'], columns = ["기준일자"], aggfunc='count')



st.markdown("---")
st.dataframe(data=gdf1, use_container_width=True)
st.markdown("---")
st.dataframe(data=pvdf, use_container_width=True)


pd.pivot_table(df[df["회사"]==option1], index=['고용형태','사원유형'], values=['임시키'], columns = ["기준일자"], aggfunc='count')










# # Set the style of the charts in the story
# example_style = Style(
#     {
#         "plot": {
#             "yAxis": {
#                 "label": {
#                     "fontSize": "1em",
#                     "paddingRight": "1.2em",
#                 },
#                 "title": {"color": "#ffffff00"},
#             },
#             "xAxis": {
#                 "label": {
#                     "angle": "2.5",
#                     "fontSize": "1.1em",
#                     "paddingRight": "0em",
#                     "paddingTop": "1em",
#                 },
#                 "title": {"fontSize": "0.8em", "paddingTop": "2.5em"},
#             },
#         },
#         "logo": {"width": "5em"},
#     }
# )

# story = Story(data=example_data, style=example_style)
# story.set_size(800, 600)


# slide1 = Slide(
#     Step(
#         Config(
#             {
#                 "channels": {
#                     "y": {
#                         "set": ["count"],
#                     },
#                     "x": {"set": ["year"]},
#                     "color": "year",
#                 },
#                 "title": "연도별 직위별 인원",
#             }
#         ),
#     )
# )
# slide2 = Slide(
#     Step(
#         Config(
#             {
#                 "channels": {
#                     "y": {
#                         "set": ["count", "grade"],
#                     },
#                     "x": {"set": ["year"]},
#                     "color": "grade",
#                 },
#                 "title": "연도별 직위별 인원",
#             }
#         ),
#     )
# )
# slide3 = Slide(
#     Step(
#         Data.filter("record.grade == '상무'"),
#         Config(
#             {
#                 "channels": {
#                     "y": {
#                         "set": ["count", "grade"],
#                     },
#                     "x": {"set": ["year"]},
#                     "color": "grade",
#                 },
#                 "title": "연도별 직위별 인원",
#             }
#         ),
#     )
# )
# slide4 = Slide(
#     Step(
#         Data.filter("record.grade == '전무'"),
#         Config(
#             {
#                 "channels": {
#                     "y": {
#                         "set": ["count", "grade"],
#                     },
#                     "x": {"set": ["year"]},
#                     "color": "grade",
#                 },
#                 "title": "연도별 직위별 인원",
#             }
#         ),
#     )
# )

# # Add the slide to the story
# story.add_slide(slide1)
# story.add_slide(slide2)
# story.add_slide(slide3)
# story.add_slide(slide4)

# story.set_feature("tooltip", True)
# story.play()
