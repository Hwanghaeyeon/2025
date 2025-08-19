import streamlit as st
import random

# 명언과 귀여운 아이콘/일러스트 매핑
quotes_with_images = [
    ("하루하루가 새로운 기회다.", "https://img.icons8.com/color/96/sunrise.png"),
    ("작은 걸음도 멈추지 않으면 큰 길이 된다.", "https://img.icons8.com/color/96/footprints.png"),
    ("할 수 있다고 믿는 순간, 이미 반은 이룬 것이다.", "https://img.icons8.com/color/96/mountain.png"),
    ("오늘은 어제보다 더 빛날 수 있다.", "https://img.icons8.com/color/96/sun.png"),
    ("포기하지 않는 사람에게는 언제나 길이 있다.", "https://img.icons8.com/color/96/road.png")
]

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 명언", page_icon="☀️", layout="centered")

# 세션 상태 초기화
if "current_quote" not in st.session_state:
    st.session_state["current_quote"], st.session_state["current_image"] = random.choice(quotes_with_images)

# 버튼: 새로운 명언
if st.button("새로운 명언 보기 ✨"):
    st.session_state["current_quote"], st.session_state["current_image"] = random.choice(quotes_with_images)

# 명언 박스 중앙 표시
st.markdown(
    """
    <style>
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
    }
    .quote-text {
        font-size: 20px;
        font-weight: bold;
        color: #333333;
        margin-top: 15px;
        font-family: 'Jua', sans-serif;
    }
    .title {
        font-size: 32px;
        font-weight: bold;
        color: #3d6b2f;
        text-align: center;
        margin-bottom: 30px;
        font-family: 'Quicksand', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True
)

# 제목
st.markdown('<div class="title">☁️ 오늘의 명언 ☀️</div>', unsafe_allow_html=True)

st.markdown('<div class="quote-box">', unsafe_allow_html=True)
st.image(st.session_state["current_image"], width=150)  # 아이콘은 150px 정도로!
st.markdown(f'<div class="quote-text">“{st.session_state["current_quote"]}”</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
