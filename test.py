import streamlit as st
import random

# -------------------------
# 데이터: 명언 ↔ 일러스트(고정, 고해상도 PNG)
# Noto Emoji 512px PNG (jsDelivr CDN)
# -------------------------
QUOTES_WITH_IMAGES = [
    ("하루하루가 새로운 기회다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f305.png"),  # 🌅 sunrise
    ("작은 걸음도 멈추지 않으면 큰 길이 된다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f463.png"),  # 👣 footprints
    ("할 수 있다고 믿는 순간, 이미 반은 이룬 것이다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f3d4.png"),  # 🏔️ snow-capped mountain
    ("오늘은 어제보다 더 빛날 수 있다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f31e.png"),  # 🌞 sun with face
    ("포기하지 않는 사람에게는 언제나 길이 있다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f6e3.png"),  # 🛣️ motorway
    ("작은 성취도 쌓이면 큰 기적이 된다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f331.png"),  # 🌱 seedling
]

# 페이지 설정 (가장 먼저)
st.set_page_config(
    page_title="오늘의 명언",
    page_icon="☀️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -------------------------
# 스타일: 연한 연두 그라데이션, 상단 로고형 헤더, 중앙 정렬, 여백 제거
# -------------------------
PAGE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Gaegu:wght@400;700&family=Quicksand:wght@500;700&display=swap');

:root { --bg1:#f7ffe8; --bg2:#eaffd0; --green:#2f5d2f; }
html, body { height: 100%; margin: 0; padding: 0; overflow-x: hidden; }

/* 배경 그라데이션 */
[data-testid="stAppViewContainer"] { background: linear-gradient(180deg, var(--bg1) 0%, var(--bg2) 100%); }
/* 기본 여백 제거 (흰 줄 방지) */
[data-testid="stAppViewContainer"] > .main { padding: 0 !important; }
.block-container { padding-top: 0 !important; padding-bottom: 0 !important; margin: 0 auto !important; }

/* 상단 로고 헤더 */
.app-header { width: 100%; display:flex; align-items:center; justify-content:center; padding: 18px 0 8px; }
.logo-wrap { display:inline-flex; align-items:center; gap:14px; }
.logo-emoji { font-size: 28px; line-height: 1; }
.logo-text { font-family: 'Jua', 'Gaegu', sans-serif; font-size: 40px; font-weight: 700; color: var(--green); letter-spacing: 1px; }

/* 본문 중앙 정렬 영역: 헤더 높이 고려 */
.center-wrap { min-height: calc(100vh - 90px); display:grid; place-items:center; }

/* 카드 (이미지 + 명언) */
.card { display:flex; flex-direction:column; align-items:center; gap:14px; text-align:center; }
.card-quote { font-size: 22px; font-weight: 800; color:#2f3b2f; font-family:'Jua', 'Gaegu', sans-serif; }

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

# 중복 방지로 새 인덱스 선택
def pick_new_index():
    if len(QUOTES_WITH_IMAGES) <= 1:
        return 0
    cur = st.session_state.idx
    nxt = random.randrange(len(QUOTES_WITH_IMAGES))
    while nxt == cur:
        nxt = random.randrange(len(QUOTES_WITH_IMAGES))
    return nxt

# -------------------------
# UI
# -------------------------
# 상단 로고형 헤더
st.markdown(
    '<div class="app-header"><div class="logo-wrap">'
    '<span class="logo-emoji">☀️</span>'
    '<span class="logo-text">오늘의 명언</span>'
    '<span class="logo-emoji">☁️</span>'
    '</div></div>',
    unsafe_allow_html=True,
)

# 본문 카드
st.markdown('<div class="center-wrap">', unsafe_allow_html=True)

quote, img_url = QUOTES_WITH_IMAGES[st.session_state.idx]
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown(f'<img class="card-img" src="{img_url}" alt="quote-illustration"/>', unsafe_allow_html=True)
st.markdown(f'<div class="card-quote">“{quote}”</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

if st.button("새로운 명언 보기 ✨"):
    st.session_state.idx = pick_new_index()

st.markdown('</div>', unsafe_allow_html=True)
