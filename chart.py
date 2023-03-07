import pandas as pd
import numpy as np
import streamlit as st
from ipyvizzustory import Story, Slide, Step
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget
import pickle
import plotly.express as px
import random
import datetime
import plotly.figure_factory as ff
from repo import *

@st.cache_data
def vz_style():
    my_style = Style(
        {
            "plot": {
                "yAxis": {
                    "label": {
                        "fontSize": "1em",
                        "paddingRight": "1.5em",
                    },
                    "title": {"color": "#ffffff00"},
                },
                "xAxis": {
                    "label": {
                        "angle": "0",
                        "fontSize": "1.1em",
                        "paddingRight": "0em",
                        "paddingTop": "1em",
                    },
                    "title": {"fontSize": "0.2em", "paddingTop": "2.5em", "backgroundColor": "#A0A0A0"},
                },
                "marker": {"colorPalette": "#3DAE2BFF #00833EFF #00A19BFF #0075A9FF #003764FF"},
            },
            "legend": {"width": 150, "backgroundColor": "#FFFDE7"},
            "logo": {"width": "5em"},
            "fontSize": 12
        }
    )
    return my_style

@st.cache_data
def vz_회사별총원변동(df):
    data1 = Data()
    data1.add_data_frame(df)
    my_style = vz_style()
    # story1 = Story(data = data1)
    story1 = Story(data = data1, style = my_style)
    title = "회사별 총인원 현황"

    slide1 = Slide(
        Step(
            Config({"x": ["기준일자"], "y": ["회사","인원"], "label":"인원","color":"회사",
                    "title": title,
                "geometry": "rectangle",}),
        )
    )
    story1.add_slide(slide1)

    slide1 = Slide(
        Step(
            Config({"x": ["기준일자"], "y": ["회사","인원"], "label":"인원","color":"회사",
                    "title": title,
                "geometry": "area",}),
        )
    )
    story1.add_slide(slide1)


    slide1 = Slide(
        Step(
            Config({"x": ["기준일자"], "y": ["회사","인원"], "label":"인원","color":"회사",
                    "title": title,
                "geometry": "area",
                    "split": True,}),)
    )
    story1.add_slide(slide1)

    slide1 = Slide(
        Step(
            Config({"x": ["회사","기준일자"], "y": ["인원"], "label":"인원","color":"회사",
                    "title": title,
                "geometry": "rectangle",}),)
    )
    story1.add_slide(slide1)
    
    slide1 = Slide(
        Step(
            Config({"x": ["회사","기준일자"], "y": ["인원", "사원유형"], "label":"인원","color":["회사","사원유형"],
                    "title": title,
                "geometry": "rectangle",}),)
    )
    story1.add_slide(slide1)


    story1.set_feature("tooltip", True)
    story1.set_size(width=800, height=500)
    story1.play()
    
@st.cache_data
def vz_회사별임원변동(df):
    gdf = df
    gdf = gdf[gdf["고용형태"] == "임원"]
    data1 = Data()
    data1.add_data_frame(gdf)
    my_style = vz_style()
    # story1 = Story(data = data1)
    story1 = Story(data = data1, style = my_style)
    title = "임원현황 (겸직임원 각자 카운트)"

    slide1 = Slide(
        Step(
            Config({"x": ["기준일자"], "y": ["회사","인원"], "label":"인원","color":"회사",
                    "title": title,
                "geometry": "rectangle",}),
        )
    )
    story1.add_slide(slide1)

    slide1 = Slide(
        Step(
            Config({"x": ["기준일자"], "y": ["회사","인원"], "label":"인원","color":"회사",
                    "title": title,
                "geometry": "area",}),
        )
    )
    story1.add_slide(slide1)


    slide1 = Slide(
        Step(
            Config({"x": ["기준일자"], "y": ["회사","인원"], "label":"인원","color":"회사",
                    "title": title,
                "geometry": "area",
                    "split": True,}),)
    )
    story1.add_slide(slide1)

    slide1 = Slide(
        Step(
            Config({"x": ["회사","기준일자"], "y": ["인원"], "label":"인원","color":"회사",
                    "title": title,
                "geometry": "rectangle",}),)
    )
    story1.add_slide(slide1)
    
    slide1 = Slide(
        Step(
            Config({"x": ["회사","기준일자"], "y": ["인원", "사원유형"], "label":"인원","color":["회사", "사원유형"],
                    "title": title,
                "geometry": "rectangle",}),)
    )
    story1.add_slide(slide1)


    story1.set_feature("tooltip", True)
    story1.set_size(width=800, height=500)
    story1.play()
    
@st.cache_data
def vz_회사별임원변동_겸직은_제뉴인(df):
    gdf = df
    gdf = gdf.loc[(gdf["고용형태"] == "임원")&(gdf["겸직임원체크"] == 0)]
    data1 = Data()
    data1.add_data_frame(gdf)
    my_style = vz_style()
    story1 = Story(data = data1, style = my_style)
    # story1 = Story(data = data1)

    title = "임원현황 (겸직임원 제뉴인 카운트)"

    slide1 = Slide(
        Step(
            Config({"x": ["기준일자"], "y": ["회사","인원"], "label":"인원","color":"회사",
                    "title": title,
                "geometry": "rectangle",}),
        )
    )
    story1.add_slide(slide1)

    slide1 = Slide(
        Step(
            Config({"x": ["기준일자"], "y": ["회사","인원"], "label":"인원","color":"회사",
                    "title": title,
                "geometry": "area",}),
        )
    )
    story1.add_slide(slide1)


    slide1 = Slide(
        Step(
            Config({"x": ["기준일자"], "y": ["회사","인원"], "label":"인원","color":"회사",
                    "title": title,
                "geometry": "area",
                    "split": True,}),)
    )
    story1.add_slide(slide1)

    slide1 = Slide(
        Step(
            Config({"x": ["회사","기준일자"], "y": ["인원"], "label":"인원","color":"회사",
                    "title": title,
                "geometry": "rectangle",}),)
    )
    story1.add_slide(slide1)
    
    slide1 = Slide(
        Step(
            Config({"x": ["회사","기준일자"], "y": ["인원", "사원유형"], "label":"인원","color":["회사", "사원유형"],
                    "title": title,
                "geometry": "rectangle",}),)
    )
    story1.add_slide(slide1)


    story1.set_feature("tooltip", True)
    story1.set_size(width=800, height=500)
    story1.play()
    
    
    
@st.cache_data
def 사무연구직급별펀넬플롯(df):
    y = df.직급.tolist()
    x = df.임시키.tolist()
    기준일자 = df.기준일자.tolist()
    사원유형 = df.사원유형.tolist()

    fig = px.funnel(df, x=x, y=y, facet_col=기준일자, facet_col_wrap=0, color = 사원유형, hover_name = y, opacity=0.9, 
                    category_orders= {'y': ["S1","S2","S3","HS","HL1", "HL2", "HL3(1)", "HL3(2)", "HL3(3)"]})  #text = portions, 
    fig.update_layout(legend_traceorder="reversed", width=1500, height=400)
    return fig

@st.cache_data
def 연령박스플롯(df):
    total_df = df
    total_gdf = total_df.groupby(['기준일자','직급','연령'])[["임시키"]].count().reset_index().round()
    fig = px.box(total_gdf, x="직급", y="연령", facet_col="기준일자", color="직급", boxmode = 'overlay', category_orders= {'직급': ["사원급", "S1","S2", "S3","HS","HL1", "HL2", "HL3(1)", "HL3(2)", "HL3(3)"]})
    fig.update_layout(legend_traceorder="reversed", width=1500, height=400)
    return fig


@st.cache_data
def 성별구조(df):
    y = df.직급.tolist()
    x = df.임시키.tolist()
    기준일자 = df.기준일자.tolist()
    성별 = df.성별.tolist()

    fig = px.funnel(df, x=x, y=y, facet_col=기준일자, facet_col_wrap=0, color = 성별, hover_name = y, opacity=0.9,
                category_orders= {'y': ["S1","S2","S3","HS","HL1", "HL2", "HL3(1)", "HL3(2)", "HL3(3)"]}) #text = portions, 
    fig.update_layout(legend_traceorder="reversed", width=1500, height=400)
    return fig
    
    
    
    
    # total_df = df
    # total_gdf = total_df.groupby(['기준일자','직급','성별'])[["인원"]].sum().reset_index().round()
    # fig = px.funnel(df, x=x, y=y, facet_col=기준일자, facet_col_wrap=0, color = 사원유형, hover_name = y, opacity=0.7, 
    #                 category_orders= {'y': ["HL1", "HL2", "HL3(1)", "HL3(2)", "HL3(3)"]})  #text = portions, 
    # # total_gdf.rename(columns={'임시키':'인원'}, inplace=True)
    
    # # fig = px.bar(total_gdf, x="직급", y=["인원", "성별"], facet_col="기준일자", color="성별", text_auto=True)
    # fig.update_layout(legend_traceorder="reversed", width=1500, height=400)
    # return fig


def convert_to_order(val):
    if val == 1:
        return 't20210801'
    elif val == 2:
        return 't20211001'
    elif val == 3:
        return 't20220101'
    elif val == 4:
        return 't20220401'
    elif val == 5:
        return 't20220701'
    elif val == 6:
        return 't20221001'
    else:
        return 't20230101'

def vz_racing_chart1(df, 회사):
    
    gdf = df[df["회사"]==회사]
    data = Data()
    data.add_data_frame(gdf)
    
    config = {
        "channels": {
            "y": {
                "set": ["그룹핑"],
                },
            "x": {"set": ["인원"]},
            "label": {"set": ["인원"]},
            "color": {"set": ["그룹핑"]},
            },
        "sort": "byValue",
        }
    
    style = Style(
        {
            "plot": {
                "paddingLeft": 150,
                "paddingTop": 25,
                "yAxis": {
                    "color": "#ffffff00",
                    "label": {"paddingRight": 10},
                    },
                "xAxis": {
                    "title": {"color": "#ffffff00"},
                    "label": {
                        "color": "#ffffff00",
                        "numberFormat": "grouped",
                        },
                    },
                "marker": {
                    "colorPalette": "#b74c20FF #c47f58FF #1c9761FF"
                    + " #ea4549FF #875792FF #3562b6FF"
                    + " #ee7c34FF #efae3aFF"
                    },
                },
            }
        )
    
    chart = Chart(display=DisplayTarget.MANUAL)
    chart.animate(data, style)
    
    for year in range(1, 7):
        t1 = convert_to_order(year)
        config["title"] = f"{회사} 분기별 조직별 인원변동 현황 - {t1}"
        chart.animate(
            Data.filter(f"parseInt(record.기준일자) == {year}"),
            Config(config),
            duration=3,
            x={"easing": "linear", "delay": 0},
            y={"delay": 0},
            show={"delay": 0},
            hide={"delay": 0},
            title={"duration": 0, "delay":0},
        )
        chart.show()

@st.cache_data
def create_sun_chart(df, 회사, 기준일자):
    gdf = df.groupby(["기준일자", "회사", "고용형태", "사원유형", "성별","그룹핑","직급", "연령", "Level1", "Level2", "겸직임원체크"])[["임시키"]].count().reset_index()
    gdf.rename(columns={'임시키':'인원'}, inplace=True)
    gdf = gdf.loc[(gdf["회사"] == 회사) & (gdf["기준일자"] == 기준일자) & (gdf["고용형태"] == "직원")& (gdf["사원유형"] != "생산기술직")& (gdf["사원유형"] != "별정직")]
    fig = px.sunburst(gdf, path=['Level1', 'Level2', '직급'], values='인원', color='Level1')
    fig.update_traces(textinfo="label+value")
    # fig.update_traces(textinfo="label+percent parent")
    fig.update_layout(autosize=False)
    return fig







