import streamlit as st
import random

# -------------------------
# 데이터: 명언 ↔ 일러스트(고정, 고해상도 PNG)
# Noto Emoji 512px PNG (jsDelivr CDN)
# -------------------------
QUOTES_WITH_IMAGES = [
    ("하루하루가 새로운 기회다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f305.png"),  # 🌅 sunrise
    ("작은 걸음도 멈추지 않으면 큰 길이 된다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f463.png"),  # 👣 footprints
    ("할 수 있다고 믿는 순간, 이미 반은 이룬 것이다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f3d4.png"),  # 🏔️ mountain
    ("오늘은 어제보다 더 빛날 수 있다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f31e.png"),  # 🌞 sun
    ("포기하지 않는 사람에게는 언제나 길이 있다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f6e3.png"),  # 🛣️ road
    ("작은 성취도 쌓이면 큰 기적이 된다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f331.png"),  # 🌱 seedling
    ("새로운 도전은 나를 성장하게 한다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f3c3.png"),  # 🏃 running
    ("행복은 늘 가까이에 있다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f33c.png"),  # 🌼 blossom
    ("매일 조금씩 나아가는 것이 중요하다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f34f.png"),  # 🍏 green apple
    ("마음을 열면 세상이 더 밝게 보인다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f31f.png"),  # 🌟 star
    # 새롭게 추가: 하루를 힘차게, 행복하게
    ("오늘의 작은 행복을 놓치지 마세요.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f338.png"),  # 🌸 cherry blossom
    ("웃음은 하루를 밝게 만드는 최고의 약이다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f600.png"),  # 😀 grinning face
    ("긍정적인 마음이 좋은 하루를 만든다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f331.png"),  # 🌱 seedling
    ("매일의 시작은 새로운 가능성으로 가득 차 있다.", "https://cdn.jsdelivr.net/gh/googlefonts/noto-emoji@main/png/512/emoji_u1f305.png")   # 🌅 sunrise
]

# 페이지 설정
st.set_page_config(
    page_title="오늘의 명언",
    page_icon="☀️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -------------------------
# 스타일
# -------------------------
PAGE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Gaegu:wght@400;700&family=Quicksand:wght@500;700&display=swap');

:root { --bg1:#f7ffe8; --bg2:#eaffd0; --green:#2f5d2f; }
html, body { height: 100%; margin: 0; padding: 0; overflow-x: hidden; }
[data-testid="stAppViewContainer"] { background: linear-gradient(180deg, var(--bg1) 0%, var(--bg2) 100%); }
[data-testid="stAppViewContainer"] > .main { padding: 0 !important; }
.block-container { padding-top: 0 !important; padding-bottom: 0 !important; margin: 0 auto !important; }
.center-wrap { min-height: 100vh; display:grid; place-items:center; }
.card { display:flex; flex-direction:column; align-items:center; gap:14px; text-align:center; }
.card-quote { font-size: 22px; font-weight: 800; color:#2f3b2f; font-family:'Jua', 'Gaegu', sans-serif; }
.card-img { width: 320px; height: 320px; border-radius: 24px; box-shadow: 0 8px 20px rgba(0,0,0,.10); object-fit: cover; }
.card-title { font-family: 'Jua', 'Gaegu', sans-serif; font-size: 36px; font-weight: 700; color: var(--green); letter-spacing: 1px; }
.stButton > button { background:#aee1a3; color:#2f4f2f; font-size:18px; font-weight:700; border-radius:14px; padding:10px 20px; border:none; box-shadow:0 3px 8px rgba(0,0,0,.12); }
.stButton > button:hover { background:#8ccf87; color:#fff; }
</style>
"""

st.markdown(PAGE_CSS, unsafe_allow_html=True)

# -------------------------
# 상태 관리
# -------------------------
if "idx" not in st.session_state:
    st.session_state.idx = random.randrange(len(QUOTES_WITH_IMAGES))

def pick_new_index():
    if len(QUOTES_WITH_IMAGES) <= 1:
        return 0
    cur = st.session_state.idx
    nxt = random.randrange(len(QUOTES_WITH_IMAGES))
    while nxt == cur:
        nxt = random.randrange(len(QUOTES_WITH_IMAGES))
    return nxt

# -------------------------
# UI: 카드 중앙에
# -------------------------
st.markdown('<div class="center-wrap">', unsafe_allow_html=True)

quote, img_url = QUOTES_WITH_IMAGES[st.session_state.idx]
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown(f'<div class="card-title">☀️ 오늘의 명언 ☁️</div>', unsafe_allow_html=True)
st.markdown(f'<img class="card-img" src="{img_url}" alt="quote-illustration"/>', unsafe_allow_html=True)
st.markdown(f'<div class="card-quote">“{quote}”</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

if st.button("새로운 명언 보기 ✨"):
    st.session_state.idx = pick_new_index()

st.markdown('</div>', unsafe_allow_html=True)
