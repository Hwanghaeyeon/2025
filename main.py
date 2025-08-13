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


import streamlit as st

# --------------------
# 페이지 기본 설정
# --------------------
st.set_page_config(page_title="🍫 몽실몽실 간식 추천기", page_icon="🍪", layout="wide")

# 감성 배경 이미지 적용 (카페 분위기)
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1511920170033-f8396924c348?auto=format&fit=crop&w=1350&q=80");
background-size: cover;
background-position: center;
background-attachment: fixed;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

.snack-card {
    background-color: rgba(255, 243, 230, 0.9);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 2px 2px 12px rgba(90, 62, 43, 0.2);
    text-align: center;
    margin-bottom: 20px;
}
h1, h2, h3, h4 {
    color: #5a3e2b;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# --------------------
# 간식 데이터
# --------------------
snack_data = [
    {"이름": "허니버터칩", "종류": "과자", "맛": {"달콤함": 4, "짭짤함": 3}, "식감": "바삭", "분위기": "간단간식", "인기점수": 95, "이미지": "https://i.imgur.com/n9pD4Ec.jpg"},
    {"이름": "몽쉘", "종류": "빵/케이크", "맛": {"달콤함": 5, "부드러움": 4}, "식감": "촉촉", "분위기": "디저트", "인기점수": 90, "이미지": "https://i.imgur.com/QsEvVnV.jpg"},
    {"이름": "붕어빵", "종류": "빵/케이크", "맛": {"달콤함": 5, "부드러움": 5}, "식감": "부드러움", "분위기": "겨울간식", "인기점수": 92, "이미지": "https://i.imgur.com/PRVQh0L.jpg"},
    {"이름": "바나나킥", "종류": "과자", "맛": {"달콤함": 3, "고소함": 4}, "식감": "바삭", "분위기": "간단간식", "인기점수": 85, "이미지": "https://i.imgur.com/tKm4A8v.jpg"},
    {"이름": "칙촉", "종류": "과자", "맛": {"달콤함": 5, "부드러움": 3}, "식감": "부드러움", "분위기": "디저트", "인기점수": 88, "이미지": "https://i.imgur.com/ObsmxUg.jpg"},
    {"이름": "누네띠네", "종류": "과자", "맛": {"달콤함": 4, "바삭함": 4}, "식감": "바삭", "분위기": "전통간식", "인기점수": 84, "이미지": "https://i.imgur.com/gqX65nD.jpg"},
    {"이름": "호떡", "종류": "빵/케이크", "맛": {"달콤함": 5, "고소함": 4}, "식감": "쫄깃", "분위기": "겨울간식", "인기점수": 93, "이미지": "https://i.imgur.com/Iw7J29o.jpg"},
    {"이름": "마카롱", "종류": "빵/케이크", "맛": {"달콤함": 5, "부드러움": 4}, "식감": "부드러움", "분위기": "디저트", "인기점수": 91, "이미지": "https://i.imgur.com/fM8WfHe.jpg"},
    {"이름": "빼빼로", "종류": "과자", "맛": {"달콤함": 4, "고소함": 3}, "식감": "바삭", "분위기": "선물간식", "인기점수": 89, "이미지": "https://i.imgur.com/3VHzjDh.jpg"},
    {"이름": "아이스크림 붕어싸만코", "종류": "아이스크림", "맛": {"달콤함": 5, "부드러움": 4}, "식감": "부드러움", "분위기": "여름간식", "인기점수": 94, "이미지": "https://i.imgur.com/KjZoGrE.jpg"},
    {"이름": "찰떡아이스", "종류": "아이스크림", "맛": {"달콤함": 4, "쫄깃함": 5}, "식감": "쫄깃", "분위기": "간단간식", "인기점수": 87, "이미지": "https://i.imgur.com/KmT44Cs.jpg"},
    {"이름": "약과", "종류": "전통간식", "맛": {"달콤함": 4, "고소함": 4}, "식감": "쫄깃", "분위기": "전통간식", "인기점수": 86, "이미지": "https://i.imgur.com/zEdc3fX.jpg"},
    {"이름": "꿀타래", "종류": "전통간식", "맛": {"달콤함": 4, "고소함": 3}, "식감": "부드러움", "분위기": "전통간식", "인기점수": 83, "이미지": "https://i.imgur.com/v6y8J7o.jpg"},
    {"이름": "찹쌀도넛", "종류": "빵/케이크", "맛": {"달콤함": 4, "고소함": 5}, "식감": "쫄깃", "분위기": "전통간식", "인기점수": 89, "이미지": "https://i.imgur.com/7cBy0Xm.jpg"},
    {"이름": "수박바", "종류": "아이스크림", "맛": {"달콤함": 4, "상큼함": 4}, "식감": "시원함", "분위기": "여름간식", "인기점수": 85, "이미지": "https://i.imgur.com/6Rj0Y1Z.jpg"}
]

# --------------------
# 타이틀
# --------------------
st.markdown("<h1 style='text-align:center;'>🍫 몽실몽실 간식 추천기</h1>", unsafe_allow_html=True)
st.write("따뜻한 카페에서 즐기듯, 원하는 간식 조건을 고르면 인기 있는 간식을 추천해드려요 ☕🍪")

# --------------------
# 입력창
# --------------------
col1, col2 = st.columns(2)
with col1:
    snack_type = st.selectbox("🍩 간식 종류", ["전체"] + sorted(list(set([s["종류"] for s in snack_data]))))
with col2:
    taste_pref = st.text_input("🍯 원하는 맛 키워드 (예: 달콤, 짭짤, 부드러움)")

# --------------------
# 필터링 + 인기순 정렬
# --------------------
filtered_snacks = []
for snack in snack_data:
    if snack_type != "전체" and snack["종류"] != snack_type:
        continue
    if taste_pref and not any(taste_pref in k for k in snack["맛"].keys()):
        continue
    filtered_snacks.append(snack)

filtered_snacks = sorted(filtered_snacks, key=lambda x: x["인기점수"], reverse=True)

# --------------------
# 결과 표시
# --------------------
if filtered_snacks:
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
                st.write(f"**{taste}**: {score}/5")
                st.progress(score / 5)
            st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("조건에 맞는 간식을 찾지 못했어요 😢")

