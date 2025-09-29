import streamlit as st
import re
from nltk.tokenize import sent_tokenize
import nltk
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import streamlit as st
import whisper
import tempfile

# Κατέβασε το punkt μόνο αν χρειάζεται
nltk.download("punkt", quiet=True)




def transcribe_youtube_streamlit():
    # Παίρνουμε URL από τον χρήστη
    url = st.text_input("Please enter YouTube URL: ")

    # Ανάλυση URL για να πάρουμε το video_id
    parsed_url = urlparse(url)
    video_id = parse_qs(parsed_url.query).get('v')
    if video_id:
        video_id = video_id[0]  # παίρνουμε το πρώτο αποτέλεσμα
    else:
        raise ValueError("Δεν βρέθηκε video_id στο URL")

    # Κλήση στο API
    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id, languages=['el','en'])

    # Προσπέλαση με attributes
    full_text = "\n".join([item.text for item in transcript])
    st.write(full_text)


if st.button("Απομαγνητοφώνηση από youtube"):
        transcribe_youtube_streamlit()


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
