import streamlit as st
import random

# 명언과 귀여운 일러스트(정사각형, OpenMoji PNG) 고정 매핑
quotes_with_images = [
    ("하루하루가 새로운 기회다.", "https://openmoji.org/data/color/png/1F305.png"),  # 🌅 sunrise
    ("작은 걸음도 멈추지 않으면 큰 길이 된다.", "https://openmoji.org/data/color/png/1F463.png"),  # 👣 footprints
    ("할 수 있다고 믿는 순간, 이미 반은 이룬 것이다.", "https://openmoji.org/data/color/png/1F3D4.png"),  # 🏔️ snow-capped mountain
    ("오늘은 어제보다 더 빛날 수 있다.", "https://openmoji.org/data/color/png/1F31E.png"),  # 🌞 sun with face
    ("포기하지 않는 사람에게는 언제나 길이 있다.", "https://openmoji.org/data/color/png/1F6E3.png"),  # 🛣️ motorway
    ("작은 성취도 쌓이면 큰 기적이 된다.", "https://openmoji.org/data/color/png/1F331.png"),  # 🌱 seedling
]

# 페이지 기본 설정 (가장 먼저)
st.set_page_config(page_title="오늘의 명언", page_icon="☀️", layout="centered", initial_sidebar_state="collapsed")

# CSS: 연한 연두 배경(포근), 중앙 정렬, 흰색 줄 제거, 귀여운 이모티콘 장식, 폰트
page_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Quicksand:wght@500&display=swap');
:root { --bg1:#f7ffe8; --bg2:#eaffd0; --green:#3d6b2f; }
html, body { height: 100%; margin: 0; padding: 0; overflow-x: hidden; }
/* 전체 배경: 연두 그라데이션 */
.stApp { background: linear-gradient(180deg, var(--bg1) 0%, var(--bg2) 100%); }
/* 스트림릿 기본 여백 제거 */
[data-testid="stAppViewContainer"] > .main { padding: 0; }
.block-container { padding-top: 0; padding-bottom: 0; margin: 0 auto; }
/* 중앙 정렬 래퍼 */
.app-wrap { min-height: 100vh; display:flex; flex-direction:column; align-items:center; justify-content:center; }
/* 제목 & 이모지 라인 */
.title { font-size: 34px; font-weight: 700; color: var(--green); text-align:center; margin: 0 0 8px 0; font-family:'Quicksand', sans-serif; }
.emoji-line { text-align:center; opacity: .85; font-size: 22px; letter-spacing: 6px; margin-bottom: 18px; }
/* 카드: 배경 박스 없이 심플하게 */
.quote-card { display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; gap: 12px; }
.quote-img { border-radius: 22px; box-shadow: 0 6px 18px rgba(0,0,0,.08); }
.quote-text { font-size: 22px; font-weight: 700; color:#2f3b2f; font-family:'Jua', sans-serif; }
/* 버튼 */
.stButton > button { background:#aee1a3; color:#2f4f2f; font-size:18px; font-weight:700; border-radius:14px; padding:10px 20px; border:none; box-shadow:0 3px 8px rgba(0,0,0,.12); }
.stButton > button:hover { background:#8ccf87; color:#fff; }
</style>
"""

st.markdown(page_css, unsafe_allow_html=True)

# 세션 상태: 현재 인덱스 보관
if "idx" not in st.session_state:
    st.session_state.idx = random.randrange(len(quotes_with_images))

# 콜백: 새 명언 뽑기
def pick_new():
    st.session_state.idx = random.randrange(len(quotes_with_images))

# 레이아웃 시작
st.markdown('<div class="app-wrap">', unsafe_allow_html=True)

st.markdown('<div class="title">☁️ 오늘의 명언 ☀️</div>', unsafe_allow_html=True)
st.markdown('<div class="emoji-line">☁️  🌱  ☀️  ☁️  🌱  ☀️</div>', unsafe_allow_html=True)

# 카드 섹션
q, img = quotes_with_images[st.session_state.idx]
st.markdown('<div class="quote-card">', unsafe_allow_html=True)
st.image(img, width=300, output_format="PNG")
st.markdown(f'<div class="quote-text">“{q}”</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 버튼
if st.button("새로운 명언 보기 ✨"):
    pick_new()
    st.experimental_rerun()

st.markdown('</div>', unsafe_allow_html=True)
