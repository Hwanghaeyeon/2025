import streamlit as st
import random

# -------------------------
# 데이터: 명언 ↔ 일러스트(고정, 고해상도 PNG)
# Noto Emoji 512px PNG (jsDelivr CDN: 안정적, 빠름)
# -------------------------
QUOTES_WITH_IMAGES = [
    ("하루하루가 새로운 기회다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f305.png"),  # 🌅 sunrise
    ("작은 걸음도 멈추지 않으면 큰 길이 된다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f463.png"),  # 👣 footprints
    ("할 수 있다고 믿는 순간, 이미 반은 이룬 것이다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f3d4.png"),  # 🏔️ snow-capped mountain
    ("오늘은 어제보다 더 빛날 수 있다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f31e.png"),  # 🌞 sun with face
    ("포기하지 않는 사람에게는 언제나 길이 있다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f6e3.png"),  # 🛣️ motorway
    ("작은 성취도 쌓이면 큰 기적이 된다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f331.png"),  # 🌱 seedling
]

# 페이지 설정 (가장 먼저 선언)
st.set_page_config(
    page_title="오늘의 명언",
    page_icon="☀️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -------------------------
# 스타일: 연한 연두 그라데이션, 중앙 정렬, 여백(흰 줄) 제거
# -------------------------
PAGE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Quicksand:wght@500&display=swap');

:root { --bg1:#f7ffe8; --bg2:#eaffd0; --green:#3d6b2f; }
html, body { height: 100%; margin: 0; padding: 0; overflow-x: hidden; }
/* 배경 그라데이션 */
[data-testid="stAppViewContainer"] { background: linear-gradient(180deg, var(--bg1) 0%, var(--bg2) 100%); }
/* 상하 여백 제거 (흰 줄 방지) */
[data-testid="stAppViewContainer"] > .main { padding: 0 !important; }
.block-container { padding-top: 0 !important; padding-bottom: 0 !important; margin: 0 auto !important; }

/* 중앙 정렬 래퍼 */
.center-wrap { min-height: 100vh; display:grid; place-items:center; }

/* 카드 (배경 박스 없음, 이미지+문구만) */
.card { display:flex; flex-direction:column; align-items:center; gap:14px; text-align:center; }
.card-title { font-size: 32px; font-weight: 700; color: var(--green); font-family:'Quicksand', sans-serif; margin:0 0 6px 0; }
.card-quote { font-size: 22px; font-weight: 800; color:#2f3b2f; font-family:'Jua', sans-serif; }

/* 정사각 이미지: 둥근 모서리 + 그림자 */
.card-img { width: 320px; height: 320px; border-radius: 24px; box-shadow: 0 8px 20px rgba(0,0,0,.10); object-fit: cover; }

/* 버튼 */
.stButton > button { background:#aee1a3; color:#2f4f2f; font-size:18px; font-weight:700; border-radius:14px; padding:10px 20px; border:none; box-shadow:0 3px 8px rgba(0,0,0,.12); }
.stButton > button:hover { background:#8ccf87; color:#fff; }
</style>
"""

st.markdown(PAGE_CSS, unsafe_allow_html=True)

# -------------------------
# 상태: 현재 인덱스
# -------------------------
if "idx" not in st.session_state:
    st.session_state.idx = random.randrange(len(QUOTES_WITH_IMAGES))

# -------------------------
# UI
# -------------------------
st.markdown('<div class="center-wrap">', unsafe_allow_html=True)

q, img = QUOTES_WITH_IMAGES[st.session_state.idx]

st.markdown('<div class="card">', unsafe_allow_html=True)
# HTML로 직접 이미지 태그를 써서 class 적용 (정사각형 + 그림자)
st.markdown(f'<img class="card-img" src="{img}" alt="quote-illustration"/>', unsafe_allow_html=True)
st.markdown('<div class="card-title">오늘의 명언</div>', unsafe_allow_html=True)
st.markdown(f'<div class="card-quote">“{q}”</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

if st.button("새로운 명언 보기 ✨"):
    st.session_state.idx = random.randrange(len(QUOTES_WITH_IMAGES))

st.markdown('</div>', unsafe_allow_html=True)
# 페이지 제목 (로고 느낌)
st.markdown("""
    <div class="app-title">
        ☀️ 오늘의 명언 ☁️
    </div>
""", unsafe_allow_html=True)

# CSS 안에 추가
.page-title {
    font-family: 'Jua', sans-serif;
    font-size: 40px;
    font-weight: bold;
    color: #2f5d2f;
    text-align: center;
    margin-bottom: 40px;
}

