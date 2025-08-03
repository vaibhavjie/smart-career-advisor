import streamlit as st
from recommend import recommend_careers

st.set_page_config(page_title="Smart Career Advisor", page_icon="🎯")

st.title("🎯 Smart Career Path Advisor")
st.write("Enter your details to get career suggestions tailored to your profile.")

skills = st.text_input("🧠 Enter your technical/non-technical skills (comma-separated)")
interests = st.text_input("💡 Enter your interests")
education = st.selectbox("🎓 Your highest education qualification", 
                         ["High School", "Diploma", "Bachelor's", "Master's", "PhD"])

if st.button("Suggest Career"):
    user_input = skills + " " + interests + " " + education
    results = recommend_careers(user_input)

    st.subheader("🔍 Recommended Career Paths:")
    for res in results:
        st.markdown(f"""
        #### ✅ {res['career']}
        **Description:** {res['description']}  
        **Match Score:** {res['match_score']}%
        ---  
        """)
