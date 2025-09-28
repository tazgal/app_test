import streamlit as st
import webbrowser
import re
from nltk.tokenize import sent_tokenize

st.write("Αυτή είναι μια δοκιμαστική εφαρμογή")

text = st.text_area("Enter text",height = 200)

if st.button("send to text"):
    st.write(f"{text}")

st.link_button("Άνοιξε Ριζοσπάστη", "https://www.rizospastis.gr")

if st.button("βρες ημερομηνίες"):
    extract_date_sentences(text)


def extract_date_sentences(text):
    """
    Παίρνει κείμενο και τυπώνει τις προτάσεις που περιέχουν ημερομηνίες.
    Υποστηρίζει μορφές όπως: 12 Ιανουαρίου 2023 ή 21/06/2023
    """
   
    # regex για ημερομηνίες (π.χ. 12 Ιανουαρίου 2023)
    greek_months = "Ιανουαρίου|Φεβρουαρίου|Μαρτίου|Απριλίου|Μαΐου|Ιουνίου|Ιουλίου|Αυγούστου|Σεπτεμβρίου|Οκτωβρίου|Νοεμβρίου|Δεκεμβρίου"
    date_pattern_1 = re.compile(rf"\b\d{{1,2}}\s({greek_months})\s\d{{4}}\b")
    
    # regex για μορφή 21/06/2023
    date_pattern_2 = re.compile(r"\b\d{1,2}/\d{1,2}/\d{4}\b")

    date_pattern_3 = re.compile(r"\b\d{1,2}/\d{1,2}")
    
    # χωρισμός σε προτάσεις
    sentences = sent_tokenize(text, language="english")  # λειτουργεί και για ελληνικό κείμενο
    
    # έλεγχος και τύπωμα
    for sentence in sentences:
        if date_pattern_1.search(sentence) or date_pattern_2.search(sentence) or date_pattern_3.search(sentence):
            st.write("\n", sentence)
