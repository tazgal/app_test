import streamlit as st
import re
from nltk.tokenize import sent_tokenize
import nltk

# Κατέβασε το punkt μόνο αν χρειάζεται
nltk.download("punkt", quiet=True)

def extract_date_sentences(text):
    """Εμφανίζει προτάσεις που περιέχουν ημερομηνίες."""
    greek_months = ("Ιανουαρίου|Φεβρουαρίου|Μαρτίου|Απριλίου|Μαΐου|Ιουνίου|"
                    "Ιουλίου|Αυγούστου|Σεπτεμβρίου|Οκτωβρίου|Νοεμβρίου|Δεκεμβρίου")
    date_pattern_1 = re.compile(rf"\b\d{{1,2}}\s({greek_months})\s\d{{4}}\b")
    date_pattern_2 = re.compile(r"\b\d{1,2}/\d{1,2}/\d{4}\b")
    date_pattern_3 = re.compile(r"\b\d{1,2}/\d{1,2}\b")

    sentences = sent_tokenize(text, language="english")
    for sentence in sentences:
        if (date_pattern_1.search(sentence) or
            date_pattern_2.search(sentence) or
            date_pattern_3.search(sentence)):
            st.write("•", sentence)

st.write("Αυτή είναι μια δοκιμαστική εφαρμογή")

text = st.text_area("Enter text", height=200)

if st.button("send to text"):
    st.write(text)

st.link_button("Άνοιξε Ριζοσπάστη", "https://www.rizospastis.gr")

if st.button("βρες ημερομηνίες"):
    extract_date_sentences(text)
