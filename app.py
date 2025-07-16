## 우리가 작성한 python 코드를 streamlit 에서 읽을 수 있도록!

# - https://cheat-sheets.streamlit.app/
# - https://docs.streamlit.io/library/cheatsheet
# - https://docs.streamlit.io/library/api-reference
# - https://imgur.com/

import streamlit as st
import pandas as pd
import numpy as np


# * optional kwarg unsafe_allow_html = True

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

print(ani_list)
st.code(ani_list) ## (텍스트) 값만 출력 #### > ["짱구는못말려","몬스터","릭앤모티"]
st.write(ani_list) ## index랑 같이 js 형태로 출력 ##### > [0:"짱구는못말려" 1:"몬스터" 2:"릭앤모티"]

for ani in ani_list:
    st.write(ani) ## 요건 값만 나오네 #### > 짱구는못말려 몬스터 릭앤모티

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)


# 입력
st.button('Demo')
st.data_editor(df)
st.checkbox('Option 1')
st.radio('Pick Country:', ['France','Germany'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter Article')
st.number_input('Enter required number')
st.text_area('Entered article text')
st.date_input('Select date')
st.time_input('Select Time')
st.file_uploader('File CSV uploader')
st.download_button('Download Source data', 'hello') ## 'hello' = data
st.camera_input('Click a Snap')
st.color_picker('Pick a color')

# 출력
st.text('Tushar-Aggarwal.com')
st.markdown('[Tushar-Aggarwal.com](https://tushar-aggarwal.com)')
st.caption('Success')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Supreme Applcations by Tushar Aggarwal')
st.write(['st', 'is <', 3]) # see *
st.title('Streamlit Magic Cheat Sheets')
st.header('Developed by Tushar Aggarwal')
st.subheader('visit tushar-aggarwal.com')
st.code('for i in range(8): print(i)')
st.image('https://i.imgur.com/t2ewhfH.png')
# * optional kwarg unsafe_allow_html = True


#####

## 입력을 변수로 받아서, 출력으로 전달!

st.markdown("### Streamlit 실습")

# 1. 버튼을 누르면 화면에 True 라고 코드를 리턴하는 간단한 동작/함수 작성

if st.button('are you tired?'):
    st.write("Ture")


# 2. 사진을 찍으면 다운로드 버튼으로 사진을 다운로드 받을 수 있게 작성
# uploaded_image = st.camera_input("사진을 찍어주세요")
# if uploaded_image:
#     st.image(uploaded_image, caption="📸 촬영한 이미지", use_column_width=True)
    
#     # 다운로드 버튼 생성
#     st.download_button(
#         label="이미지 다운로드",
#         data=uploaded_image.getvalue(),
#         file_name="captured_image.png",
#         mime="image/png"
#     )

# 2. 사진을 찍으면 다운로드 버튼으로 사진을 다운로드 받을 수 있게 작성
if image := st.camera_input('Click a Snap2'): # 사진을 찍기 전에는 들여쓰기 안의 코드를 실행하지 않습니다.
    st.download_button('다운로드', image, 'my.png')


