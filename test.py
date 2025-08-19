import streamlit as st
import random

# 명언과 관련 이미지 매핑
quotes_with_images = [
    ("하루하루가 새로운 기회다.", "https://source.unsplash.com/400x400/?sunrise"),
    ("작은 걸음도 멈추지 않으면 큰 길이 된다.", "https://source.unsplash.com/400x400/?path"),
    ("할 수 있다고 믿는 순간, 이미 반은 이룬 것이다.", "https://source.unsplash.com/400x400/?mountain"),
    ("오늘은 어제보다 더 빛날 수 있다.", "https://source.unsplash.com/400x400/?sun"),
    ("포기하지 않는 사람에게는 언제나 길이 있다.", "https://source.unsplash.com/400x400/?road")
]

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 명언", page_icon="☀️", layout="centered")

# 배경 색상 & 분위기 CSS (폰트 추가)
page_bg = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Quicksand:wght@500&display=swap');

.stApp {
    background-color: #eaffd0; /* 연두색 배경 */
    background-image: linear-gradient(to top, #eaffd0, #ffffff);
    font-family: 'Quicksand', 'Jua', sans-serif;
}
.quote-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: #ffffff;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    width: 400px;
    text-align: center;
    margin: auto;
    font-family: 'Jua', sans-serif;
}
.quote-text {
    font-size: 22px;
    font-weight: bold;
    color: #333333;
    margin-top: 15px;
    font-family: 'Jua', sans-serif;
}
.title {
    font-size: 34px;
    font-weight: bold;
    color: #3d6b2f;
    text-align: center;
    margin-bottom: 30px;
    font-family: 'Quicksand', sans-serif;
}
/* 버튼 스타일 */
div.stButton > button:first-child {
    background-color: #aee1a3;
    color: #2f4f2f;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    padding: 10px 20px;
    border: none;
    box-shadow: 0 3px 6px rgba(0,0,0,0.1);
    cursor: pointer;
    font-family: 'Quicksand', sans-serif;
}
div.stButton > button:hover {
    background-color: #8ccf87;
    color: white;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# 제목
st.markdown('<div class="title">☁️ 오늘의 명언 ☀️</div>', unsafe_allow_html=True)

# 세션 상태에 현재 명언 저장
if "current_quote" not in st.session_state:
    st.session_state["current_quote"], st.session_state["current_image"] = random.choice(quotes_with_images)

# 버튼: 새로운 명언
if st.button("새로운 명언 보기 ✨"):
    st.session_state["current_quote"], st.session_state["current_image"] = random.choice(quotes_with_images)

# 명언 박스 중앙 표시
st.markdown('<div class="quote-box">', unsafe_allow_html=True)
st.image(st.session_state["current_image"], width=300)
st.markdown(f'<div class="quote-text">“{st.session_state["current_quote"]}”</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st
import random
import time

# 명언과 관련 이미지 매핑 (랜덤 시그널 추가)
def get_image_url(query: str) -> str:
    return f"https://source.unsplash.com/400x400/?{query}&sig={int(time.time()*1000)}"

quotes_with_images = [
    ("하루하루가 새로운 기회다.", get_image_url("sunrise")),
    ("작은 걸음도 멈추지 않으면 큰 길이 된다.", get_image_url("path")),
    ("할 수 있다고 믿는 순간, 이미 반은 이룬 것이다.", get_image_url("mountain")),
    ("오늘은 어제보다 더 빛날 수 있다.", get_image_url("sun")),
    ("포기하지 않는 사람에게는 언제나 길이 있다.", get_image_url("road"))
]

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 명언", page_icon="☀️", layout="centered")

# ... (CSS 부분은 그대로 유지)

# 세션 상태에 현재 명언 저장
if "current_quote" not in st.session_state:
    st.session_state["current_quote"], st.session_state["current_image"] = random.choice(quotes_with_images)

# 버튼: 새로운 명언
if st.button("새로운 명언 보기 ✨"):
    st.session_state["current_quote"], st.session_state["current_image"] = random.choice(quotes_with_images)

# 명언 박스 중앙 표시
st.markdown('<div class="quote-box">', unsafe_allow_html=True)
st.image(st.session_state["current_image"], width=300)
st.markdown(f'<div class="quote-text">“{st.session_state["current_quote"]}”</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

