import streamlit as st
from ipyvizzustory import Story, Slide, Step
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from prepare_df import *
import roughviz
import pydeck as pdk


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
                "marker": {"colorPalette": "#FB7185FF #818CF8FF #60A5FAFF #4ADE80FF #FACC15FF"},     #"#3DAE2BFF #00833EFF #00A19BFF #0075A9FF #003764FF"
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
    title = "임원현황 (겸직임원 각사 카운트)"

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
def vz_회사별임원변동_겸직은_HDX(df):
    gdf = df
    gdf = gdf.loc[(gdf["고용형태"] == "임원")&(gdf["겸직임원체크"] == 0)]
    data1 = Data()
    data1.add_data_frame(gdf)
    my_style = vz_style()
    story1 = Story(data = data1, style = my_style)
    # story1 = Story(data = data1)

    title = "임원현황 (겸직임원 HDX 카운트)"

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
def 연령구조펀넬플롯(df):
    y = df.연령대.tolist()
    x = df.임시키.tolist()
    기준일자 = df.기준일자.tolist()
    직급 = df.직급.tolist()
    fig = px.funnel(df, x=x, y=y, facet_col=기준일자, facet_col_wrap=0, color = 직급, hover_name = y, opacity=0.9,
                category_orders= {'y': ["20대","30대","40대","50대","60대"]}) #text = portions, 
    fig.update_layout(legend_traceorder="reversed", width=1500, height=400)
    return fig
    


@st.cache_data
def 성별구조펀넬플롯(df):
    y = df.직급.tolist()
    x = df.임시키.tolist()
    기준일자 = df.기준일자.tolist()
    성별 = df.성별.tolist()

    fig = px.funnel(df, x=x, y=y, facet_col=기준일자, facet_col_wrap=0, color = 성별, hover_name = y, opacity=0.9,
                category_orders= {'y': ["S1","S2","S3","HS","HL1", "HL2", "HL3(1)", "HL3(2)", "HL3(3)"]}) #text = portions, 
    fig.update_layout(legend_traceorder="reversed", width=1500, height=400)
    return fig




@st.cache_data
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
    elif val == 7:
        return 't20230101'
    elif val == 8:
        return 't20230401'
    else:
        return None
    

@st.cache_data
def create_sun_chart(df, 회사, 기준일자, 조건):
    gdf = df.groupby(["기준일자", "회사", "고용형태", "사원유형", "성별","그룹핑","직급", "연령", "Level1", "Level2", "겸직임원체크"])[["임시키"]].count().reset_index()
    gdf.rename(columns={'임시키':'인원'}, inplace=True)
    gdf = gdf.loc[(gdf["회사"] == 회사) & (gdf["기준일자"] == 기준일자) & (gdf["고용형태"] == "직원")& (gdf["사원유형"] != "생산기술직")& (gdf["사원유형"] != "별정직")]
    fig = px.sunburst(gdf, path=['Level1', 'Level2', '직급'], values='인원', color='Level1')
    if 조건:
        fig.update_traces(textinfo="label+percent parent")
    else:
        fig.update_traces(textinfo="label+value")
    fig.update_layout(autosize=False)
    return fig


@st.cache_data
def vz_racing_chart1(df, 회사, dura):
    
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
                "paddingLeft": 200,
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
    
    chart = Chart(display=DisplayTarget.MANUAL, width="70%", height="500px")
    chart.animate(data, style)
    
    for year in range(1, 9):
        t1 = convert_to_order(year)
        config["title"] = f"{회사} 인원변동 현황 - {t1}"
        chart.animate(
            Data.filter(f"parseInt(record.기준일자) == {year}"),
            Config(config),
            duration=dura,
            x={"easing": "linear", "delay": 0},
            y={"delay": 0},
            show={"delay": 0},
            hide={"delay": 0},
            title={"duration": 0, "delay":0},
        )
    return chart._repr_html_()


def roughviz_chart(df):
    df = df
    rough_vz = roughviz.bar(df["그룹핑"], df["인원"], axisRoughness = 0.7, axisStrokeWidth = 0.7, roughness=2.3, highlight="gray")
    return rough_vz

#####################################################################################################################
# @st.cache_data
# def chart1(기준일자들, df):
#     기준일자들 = 기준일자들

#     t_df = df[df["기준일자"].isin(기준일자들)]
#     gdf = t_df.groupby(["기준일자","회사"])[["임시키"]].count().reset_index()
#     gdf.rename(columns={'임시키':'인원'}, inplace=True)
#     fig = px.bar(gdf, x="기준일자", y=["인원"], color="회사", barmode="relative",opacity=0.6, text_auto=True, category_orders= {'인원': ["HL1", "HL2", "HL3(1)", "HL3(2)", "HL3(3)"]})
#     fig.update_layout(legend_traceorder="reversed", width=1400, height=400)
#     return fig


@st.cache_data
def vz_인력운영계획(df):
    data1 = Data()
    data1.add_data_frame(df)
    my_style = vz_style()
    story1 = Story(data = data1, style = my_style)
    story1.set_feature("tooltip", True)
    story1.set_size(width=1500, height=700)

    title = "설계연구직/사무기술직 인력운영 계획"

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
            Config({"x": ["기준일자"], "y": ["사원유형","인원"], "label":"인원","color":"사원유형",
                    "title": title + " (사원유형별)",
                    "geometry": "area",
                    "split": True}),
        )
    )
    story1.add_slide(slide1)
    
    slide1 = Slide(
        Step(
            Config({"x": ["연령대","인원"], "y": ["기준일자"], "label":"인원","color":"연령대",
                    "title": title + " (연령대별)",
                    "geometry": "rectangle",
                    "split": True,}),)
    )
    story1.add_slide(slide1)
    
    slide1 = Slide(
        Step(
            Config({"x": ["직급","인원"], "y": ["기준일자"], "label":["인원", "직급"],"color":"직급",
                    "title": title + " (직급별)",
                    "geometry": "rectangle",
                    "split": True,}),)
    )
    story1.add_slide(slide1)
    
    slide1 = Slide(
        Step(
            Config({"x": ["성별","직급", "인원"], "y": ["기준일자"], "label":["인원","직급"],"color":"성별",
                    "title": title + "(성별/직급별)",
                    "geometry": "rectangle",
                    "split": True,}),)
    )
    story1.add_slide(slide1)

    slide1 = Slide(
        Step(
            Config({"x": ["인원","Level1"], "y": ["기준일자"], "label":"인원","color":"Level1",
                    "title": title + " (Level1 조직별)",
                    "geometry": "rectangle",
                    "split": True,}),)
    )
    story1.add_slide(slide1)

    slide1 = Slide(
        Step(
            Config({"x": ["인원","그룹핑"], "y": ["기준일자"], "label":"인원","color":"그룹핑",
                    "title": title + " (Level1/Level2 조직별)",
                    "geometry": "rectangle",
                    "split": True,}),)
    )
    story1.add_slide(slide1)

    story1.play()
    
    

###################################################################################################################    
@st.cache_data
def pension_chart1(df, col):
    tdf = df
    fig = px.line(tdf,
        x = "기준일자",
        y = col,
        color = "약식명",
        markers=True,
        line_shape = 'linear',
        text = col
    )
    fig.update_traces(textposition='top center')
    
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)



@st.cache_data
def pension_chart2(df, lst):
    tdf = df
    fig = go.Figure()
    my_colors = ["red", "blue"]
    for idx, l in enumerate(lst):
        fig.add_trace(go.Scatter(x=tdf["기준일자"].tolist(), y=tdf[l].tolist(), mode='lines+markers+text', name=l, text = tdf[l].tolist(), line={"color":my_colors[idx]}))
    fig.update_traces(textposition='top center', marker_size=10, textfont={"family": "Arial", "size": 12, "color": "green"})
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
 
    

@st.cache_data
def location_chart(df, mode='light'):
    order1= {'기준일자':['t20210801', 't20211001', 't20220101', 't20220401', 't20220701', 't20221001', 't20230101', 't20230401']}
    px.set_mapbox_access_token(open("mapbox_token.py").read())
    fig = px.scatter_mapbox(df, lat="lat", lon="lon",  color="근무지", size="로그",
                            color_continuous_scale=px.colors.sequential, size_max=50, zoom=7,
                            center = {'lat':36.40, 'lon':128.10}, height=700, mapbox_style=mode,
                            labels = {'회사': 'company'}, category_orders=order1,
                            hover_name="근무지", opacity=0.5, hover_data=["기준일자", "인원"], text="회사")
    st.plotly_chart(fig, use_container_width=True)


@st.cache_data 
def loca_pydeck_chart(df):
       
    st.pydeck_chart(pdk.Deck(
        height= 800,
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.40,
            longitude=128.10,
            zoom=6,
            pitch=60,
            bearing=-5
        ),
        layers=[
            pdk.Layer(
                "ColumnLayer",
                data=df[df["회사"]=="HDX"],
                get_position=["lon", "lat"],
                get_elevation="로그",
                elevation_scale=30000,
                radius=8000,
                get_fill_color=[0, 0, 255],
                pickable=True,
                auto_highlight=True,
                opacity=0.9
            ),
            pdk.Layer(
                "ColumnLayer",
                data=df[df["회사"]=="HDI"],
                get_position=["lon", "lat"],
                get_elevation="로그",
                elevation_scale=30000,
                radius=8000,
                get_fill_color=[255, 51, 51],
                pickable=True,
                auto_highlight=True,
                opacity=0.9
            ),
            pdk.Layer(
                "ColumnLayer",
                data=df[df["회사"]=="HCE"],
                get_position=["lon", "lat"],
                get_elevation="로그",
                elevation_scale=30000,
                radius=8000,
                get_fill_color=[255, 255, 0],
                pickable=True,
                auto_highlight=True,
                opacity=0.9
            )
        ],
        tooltip={
            'html': '회사: {회사}<br> 사업장: {근무지}<br> 인원: {인원}',
            'style': {
                'color': 'white'
                }
            }
    ))