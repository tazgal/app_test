import streamlit as st

st.write("Αυτή είναι μια δοκιμαστική εφαρμογή")

text = st.text_area("Enter text",height = 200)

if st.button("send to text"):
    st.write(f"{text}")
