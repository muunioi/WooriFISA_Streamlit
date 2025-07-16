### 차트 그리기 ####
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)

# Plotly Bar Chart
fig = px.bar(
    df,
    x="command",     # x축에 command
    y="rating",      # y축에 rating
    color="command", # command별 색깔 구분
    labels={"command": "x축 제목", "rating": "Rating"},
    title="Command Rating Bar Chart"
)

# # Streamlit에 출력: use_container_width=True - 현재 창 사이즈 그대로 출력하겠다
st.plotly_chart(fig, use_container_width=True)