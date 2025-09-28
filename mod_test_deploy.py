import streamlit as st
import webbrowser

st.write("Αυτή είναι μια δοκιμαστική εφαρμογή")

text = st.text_area("Enter text",height = 200)

if st.button("send to text"):
    st.write(f"{text}")

if st.button("open Ριζοσπάστη"):
    webbrowser.open_new_tab("https://www.rizospastis.gr")
