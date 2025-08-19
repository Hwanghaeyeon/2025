import streamlit as st
import random

# 명언 리스트
quotes = [
    "하루하루가 새로운 기회다.",
    "작은 걸음도 멈추지 않으면 큰 길이 된다.",
    "할 수 있다고 믿는 순간, 이미 반은 이룬 것이다.",
    "오늘은 어제보다 더 빛날 수 있다.",
    "포기하지 않는 사람에게는 언제나 길이 있다."
]

# 귀여운 분위기의 이미지 URL 리스트 (정사각형 느낌)
images = [
    "https://picsum.photos/400?random=1",
    "https://picsum.photos/400?random=2",
    "https://picsum.photos/400?random=3",
    "https://picsum.photos/400?random=4",
    "https://picsum.photos/400?random=5"
]

# 랜덤으로 명언과 이미지 선택
quote = random.choice(quotes)
image_url = random.choice(images)

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 명언", page_icon="☀️", layout="centered")

# 배경 색상 & 분위기 CSS
page_bg = """
<style>
.stApp {
    background-color: #eaffd0; /* 연두색 배경 */
    background-image: linear-gradient(to top, #eaffd0, #ffffff);
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
}
.quote-text {
    font-size: 20px;
    font-weight: bold;
    color: #333333;
    margin-top: 15px;
}
.title {
    font-size: 32px;
    font-weight: bold;
    color: #3d6b2f;
    text-align: center;
    margin-bottom: 30px;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# 제목
st.markdown('<div class="title">☁️ 오늘의 명언 ☀️</div>', unsafe_allow_html=True)

# 명언 박스
st.markdown('<div class="quote-box">', unsafe_allow_html=True)
st.image(image_url, width=300)
st.markdown(f'<div class="quote-text">“{quote}”</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

