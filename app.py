import streamlit as st
from recommender import recommend

st.set_page_config(page_title="Movie Recommendation System")

st.title("🎬 Movie Recommendation System")

movie = st.text_input("Enter Movie Name")

if st.button("Recommend"):
    results = recommend(movie)

    st.subheader("Recommended Movies")
    for i, m in enumerate(results, start=1):
        st.write(f"{i}. {m}")
