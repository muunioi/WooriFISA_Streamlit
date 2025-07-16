import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

goal = "텍스트를 입력받아서 해당 텍스트와 일치하는 이미지를 화면에 출력하는 검색창 만들기"

st.markdown("# Steramlit 실습 2")
st.markdown("> " + goal)

user_input = st.text_input("제목 입력하기")

if user_input in ani_list :
    st.image(img_list[ani_list.index(user_input)])
else :
    st.warning("일치하는 데이터가 없습니다")


# if tmp_input := st.text_input('에니메이션을 입력해주세요.'):
#     for i, el in enumerate(ani_list):
#         if tmp_input in el:
#             st.image(img_list[i])

#####
# ✅ :=
# - 윌러스 연산자(할당 표현식) : 변수에 값을 할당하면서 동시에 그 값을 사용하게 해줌
#
#####

