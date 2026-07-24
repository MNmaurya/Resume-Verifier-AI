import streamlit as st
from model import predict_resume #backend<-> frontent connection 

# Page config
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>💼 AI Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>ATS Score + Smart Shortlisting Prediction</p>", unsafe_allow_html=True)

st.divider()

# Input Section
st.subheader("📥 Enter Your Details")

skills = st.text_input(
    "💡 Enter your top 5 skills (comma separated)",
    "Python, SQL....."
)

col1, col2 = st.columns(2)

with col1:
    experience = st.slider("📅 Years of Experience", 0, 10, 2)

with col2:
    education = st.selectbox(
        "🎓 Education Level",
        [1,2,3],
        format_func=lambda x: "School" if x==1 else "Graduate" if x==2 else "Postgraduate"
    )

st.divider()

# Button
if st.button("🚀 Analyze Resume"):

    skill_match, matched_list, ats, result, probability, message = predict_resume(
        skills, experience, education
    )

    st.subheader("📊 Analysis Result")

    # Metrics row
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🧠 Skills Matched", skill_match)

    with col2:
        st.metric("📊 ATS Score", f"{int(ats)}/100")

    with col3:
        st.metric("📈 Selection Chance", f"{probability}%")

    # Progress bar
    st.progress(int(ats) / 100)

    st.divider()

    # Matched skills
    st.subheader("✅ Matched Skills")
    if matched_list:
        st.write(", ".join(matched_list))
    else:
        st.write("No relevant skills matched")

    st.divider()

    # Final prediction
    if result == 1:
        st.success("🎉 Resume Likely to be SHORTLISTED")
    else:
        st.error("⚠️ Resume Likely to be REJECTED")

    # Explanation
    st.info(message)