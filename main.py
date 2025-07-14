import streamlit as st

st.set_page_config(page_title="MBTI 직업 추천", page_icon="🧠")

st.title("🧠 MBTI 기반 직업 추천기")
st.write("당신의 MBTI 유형을 선택하면, 어울리는 직업 3가지를 추천해드립니다!")

# MBTI 목록
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# MBTI별 직업 추천 데이터
mbti_jobs = {
    "ISTJ": ["회계사", "경찰관", "공무원"],
    "ISFJ": ["간호사", "사회복지사", "초등교사"],
    "INFJ": ["상담사", "작가", "심리학자"],
    "INTJ": ["전략기획가", "데이터 과학자", "기술 컨설턴트"],
    "ISTP": ["기계공학자", "파일럿", "응급구조사"],
    "ISFP": ["패션디자이너", "사진작가", "물리치료사"],
    "INFP": ["예술가", "시인", "상담교사"],
    "INTP": ["연구원", "개발자", "이론물리학자"],
    "ESTP": ["기업가", "세일즈 매니저", "이벤트 기획자"],
    "ESFP": ["배우", "가수", "방송인"],
    "ENFP": ["광고기획자", "작가", "창업가"],
    "ENTP": ["마케팅 전문가", "발명가", "정치인"],
    "ESTJ": ["경영 관리자", "군인", "프로젝트 매니저"],
    "ESFJ": ["초등교사", "간호사", "호텔리어"],
    "ENFJ": ["HR 매니저", "교육 컨설턴트", "정신과 의사"],
    "ENTJ": ["CEO", "변호사", "전략 컨설턴트"]
}

# 사용자 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

# 추천 버튼
if st.button("추천 직업 보기"):
    jobs = mbti_jobs.get(selected_mbti, [])
    if jobs:
        st.subheader(f"💼 {selected_mbti} 유형에 어울리는 직업")
        for job in jobs:
            st.markdown(f"- {job}")
    else:
        st.warning("직업 정보가 없습니다.")
