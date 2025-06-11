import streamlit as st
import random

st.title("숫자 맞추기 게임")
st.write("1부터 100 사이의 숫자를 맞춰보세요!")

if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.message = "숫자를 입력하고 '제출' 버튼을 누르세요."

guess = st.number_input("숫자 입력", min_value=1, max_value=100, step=1)

if st.button("제출"):
    if guess < st.session_state.number:
        st.session_state.message = "너무 낮습니다! 더 큰 숫자를 입력해보세요."
    elif guess > st.session_state.number:
        st.session_state.message = "너무 높습니다! 더 작은 숫자를 입력해보세요."
    else:
        st.session_state.message = "정답입니다! 축하합니다."
        st.session_state.number = random.randint(1, 100)  # 게임 재시작
        st.session_state.message += " 새로운 숫자가 생성되었습니다. 다시 도전해보세요!"

st.write(st.session_state.message)

