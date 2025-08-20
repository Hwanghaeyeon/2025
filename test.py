import streamlit as st
import random

# 명언과 관련 이미지 매핑 (일러스트 느낌 고정 이미지)
quotes_with_images = [
    ("하루하루가 새로운 기회다.", "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f305.png"),
    ("작은 걸음도 멈추지 않으면 큰 길이 된다.", "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f463.png"),
    ("할 수 있다고 믿는 순간, 이미 반은 이룬 것이다.", "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/26f0.png"),
    ("오늘은 어제보다 더 빛날 수 있다.", "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/2600.png"),
    ("포기하지 않는 사람에게는 언제나 길이 있다.", "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f6e3.png"),
    ("마음의 평화가 가장 큰 행복이다.", "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f33f.png")
]

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 명언", page_icon="☀️", layout="centered")

# 배경 색상 & 분위기 CSS
page_bg = """
<style>
.stApp {
    background-color: #eaffd0; /* 연두색 배경 */
    background-image: linear-gradient(to top, #eaffd0, #ffffff);
    height: 100vh;
    margin: 0;
    padding: 0;
}

.quote-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: #ffffffcc;
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.1);
    width: 400px;
    text-align: center;
    margin: auto;
}

.title {
    font-family: 'Jua', 'Gaegu', cursive;
    font-size: 36px;
    font-weight: bold;
    color: #2f5d2f;
    text-align: center;
    margin-bottom: 20px;
}

.quote-text {
    font-size: 20px;
    font-weight: bold;
    color: #333333;
    margin-top: 15px;
}

.card-img {
    width: 300px;
    height: 300px;
    object-fit: cover;
    border-radius: 15px;
    margin-bottom: 15px;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# 세션 상태에 현재 명언 저장
if "current_quote" not in st.session_state:
    st.session_state.current_quote, st.session_state.current_image = random.choice(quotes_with_images)

# 버튼: 새로운 명언
if st.button("새로운 명언 보기 ✨"):
    prev_quote = st.session_state.current_quote
    while True:
        new_quote, new_image = random.choice(quotes_with_images)
        if new_quote != prev_quote:
            st.session_state.current_quote, st.session_state.current_image = new_quote, new_image
            break

# 명언 박스 중앙 표시
st.markdown('<div class="quote-box">', unsafe_allow_html=True)
st.markdown('<div class="title">☀️ 오늘의 명언 ☁️</div>', unsafe_allow_html=True)
st.image(st.session_state.current_image, width=300)
st.markdown(f'<div class="quote-text">“{st.session_state.current_quote}”</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
