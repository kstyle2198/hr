import pandas as pd
import streamlit as st
from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step

st.set_page_config(page_title="회사비교", page_icon=":bar_chart:", layout="wide")

st.title("test12345")
st.markdown("---")

example_data = Data()
example_df = pd.read_csv(
    "testfile1.csv",
    dtype={"year": str},
    encoding='UTF8'
)
example_data.add_data_frame(example_df)

# Set the style of the charts in the story
example_style = Style(
    {
        "plot": {
            "yAxis": {
                "label": {
                    "fontSize": "1em",
                    "paddingRight": "1.2em",
                },
                "title": {"color": "#ffffff00"},
            },
            "xAxis": {
                "label": {
                    "angle": "2.5",
                    "fontSize": "1.1em",
                    "paddingRight": "0em",
                    "paddingTop": "1em",
                },
                "title": {"fontSize": "0.8em", "paddingTop": "2.5em"},
            },
        },
        "logo": {"width": "5em"},
    }
)

story = Story(data=example_data, style=example_style)
story.set_size(800, 600)


slide1 = Slide(
    Step(
        Config(
            {
                "channels": {
                    "y": {
                        "set": ["count"],
                    },
                    "x": {"set": ["year"]},
                    "color": "year",
                },
                "title": "연도별 직위별 인원",
            }
        ),
    )
)
slide2 = Slide(
    Step(
        Config(
            {
                "channels": {
                    "y": {
                        "set": ["count", "grade"],
                    },
                    "x": {"set": ["year"]},
                    "color": "grade",
                },
                "title": "연도별 직위별 인원",
            }
        ),
    )
)
slide3 = Slide(
    Step(
        Data.filter("record.grade == '상무'"),
        Config(
            {
                "channels": {
                    "y": {
                        "set": ["count", "grade"],
                    },
                    "x": {"set": ["year"]},
                    "color": "grade",
                },
                "title": "연도별 직위별 인원",
            }
        ),
    )
)
slide4 = Slide(
    Step(
        Data.filter("record.grade == '전무'"),
        Config(
            {
                "channels": {
                    "y": {
                        "set": ["count", "grade"],
                    },
                    "x": {"set": ["year"]},
                    "color": "grade",
                },
                "title": "연도별 직위별 인원",
            }
        ),
    )
)

# Add the slide to the story
story.add_slide(slide1)
story.add_slide(slide2)
story.add_slide(slide3)
story.add_slide(slide4)

story.set_feature("tooltip", True)
story.play()
