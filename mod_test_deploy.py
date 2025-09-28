import streamlit as st
import webbrowser

st.write("Αυτή είναι μια δοκιμαστική εφαρμογή")

text = st.text_area("Enter text",height = 200)

if st.button("send to text"):
    st.write(f"{text}")

st.link_button("Άνοιξε Ριζοσπάστη", "https://www.rizospastis.gr")
