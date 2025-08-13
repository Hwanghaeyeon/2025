import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="🍫 몽실몽실 간식 추천기", page_icon="🍪", layout="wide")

st.markdown(
    """
    <style>
    body {
        background-color: #fff8f0;
        font-family: 'Pretendard', sans-serif;
    }
    .title {
        text-align: center;
        color: #5a3e2b;
    }
    .snack-card {
        background-color: #fff3e6;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 2px 2px 12px rgba(90, 62, 43, 0.1);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True
)

# 데이터
snack_data = [
    {
        "이름": "허니버터칩",
        "종류": "과자",
        "맛": {"달콤함": 4, "짭짤함": 3},
        "식감": "바삭",
        "분위기": "간단간식",
        "인기점수": 95,
        "이미지": "https://i.imgur.com/n9pD4Ec.jpg"
    },
    {
        "이름": "몽쉘",
        "종류": "빵/케이크",
        "맛": {"달콤함": 5, "부드러움": 4},
        "식감": "촉촉",
        "분위기": "디저트",
        "인기점수": 90,
        "이미지": "https://i.imgur.com/QsEvVnV.jpg"
    },
    {
        "이름": "붕어빵",
        "종류": "빵/케이크",
        "맛": {"달콤함": 5, "부드러움": 5},
        "식감": "부드러움",
        "분위기": "겨울간식",
        "인기점수": 92,
        "이미지": "https://i.imgur.com/PRVQh0L.jpg"
    }
]

# 타이틀
st.markdown("<h1 class='title'>🍫 몽실몽실 간식 추천기</h1>", unsafe_allow_html=True)

# 입력
snack_type = st.selectbox("간식 종류 선택 🍩", ["전체", "과자", "빵/케이크", "아이스크림"])
taste_pref = st.text_input("원하는 맛 (예: 달콤, 짭짤, 부드러움)")

# 필터링
filtered_snacks = []
for snack in snack_data:
    if snack_type != "전체" and snack["종류"] != snack_type:
        continue
    if taste_pref and not any(taste_pref in k for k in snack["맛"].keys()):
        continue
    filtered_snacks.append(snack)

# 인기순 정렬
filtered_snacks = sorted(filtered_snacks, key=lambda x: x["인기점수"], reverse=True)

# 결과 표시
cols = st.columns(3)
for i, snack in enumerate(filtered_snacks):
    with cols[i % 3]:
        st.markdown("<div class='snack-card'>", unsafe_allow_html=True)
        st.image(snack["이미지"], use_column_width=True)
        st.subheader(snack["이름"])
        st.write(f"종류: {snack['종류']}")
        st.write(f"식감: {snack['식감']}")
        st.write(f"인기점수: {snack['인기점수']} / 100")
        st.write("맛 강도:")
        for taste, score in snack["맛"].items():
            st.progress(score / 5)
            st.write(f"{taste}: {score}/5")
        st.markdown("</div>", unsafe_allow_html=True)
