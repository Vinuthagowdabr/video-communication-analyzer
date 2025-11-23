import streamlit as st
import whisper
import yt_dlp
import os
import textstat
import re
import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize

# ---------------- UI DESIGN ----------------
st.set_page_config(page_title="Video Communication Analyzer", layout="centered")

st.markdown("""
<style>
.stApp {background-color: #f4f6fa;}
.center-text {text-align: center;}
.box {
    background-color: #e8f5e9;
    padding: 20px;
    border-radius: 10px;
    margin-top: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='center-text'>🎯 Video to Text & Summary App</h1>", unsafe_allow_html=True)

# ---------------- INPUT ----------------
video_url = st.text_input("📌 Enter YouTube Video URL:", placeholder="https://youtu.be/example")

# ---------------- DOWNLOAD AUDIO ----------------
def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "audio.mp3"

# ---------------- TRANSCRIBE ----------------
def transcribe(audio_file):
    model = whisper.load_model("tiny")
    result = model.transcribe(audio_file)
    return result["text"]

# ---------------- ADVANCED CLEANING FOR HIGH CLARITY ----------------
def improve_clarity(text):
    # 1) Remove filler words
    fillers = ["you know", "actually", "basically", "literally", "like", "kinda", "sort of", "so"]
    for word in fillers:
        text = re.sub(rf'\b{word}\b', '', text, flags=re.IGNORECASE)

    # 2) Convert long paragraphs → short sentences
    sentences = sent_tokenize(text)
    short_sentences = [s.strip() for s in sentences if 5 < len(s.split()) < 18]
    improved = ". ".join(short_sentences)
    
    return improved

# ---------------- SUMMARIZE ----------------
def summarize_text(text, max_sentences=3):
    sentences = sent_tokenize(text)
    return " ".join(sentences[:max_sentences])

# ---------------- RUN ----------------
if st.button("🚀 Analyze Video"):
    if not video_url:
        st.warning("⚠️ Please enter a valid video URL!")
    else:
        st.info("📥 Downloading audio...")
        audio_path = download_audio(video_url)

        st.info("🎧 Converting audio to text...")
        transcript = transcribe(audio_path)

        st.subheader("📝 Full Transcript")
        with st.expander("Click to View Transcript"):
            st.write(transcript)

        # IMPROVE CLARITY
        better_text = improve_clarity(transcript)
        score = textstat.flesch_reading_ease(better_text)

        # ----- DISPLAY SCORE -----
        st.subheader("🌟 Clarity Score ")
        st.markdown(f"""
        <div class="box">
            <h2>🔍 Clarity Score: <b>{round(score, 2)}%</b></h2>
        </div>
        """, unsafe_allow_html=True)

        

        # --- Summary ---
        st.subheader("🧠 Summary")
        st.write(summarize_text(better_text))

        # --- Final Success Message ---
        st.markdown("""
        <div style='
            background-color: #d5f5d8;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #1b5e20;
            box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.2);
        '>
            🎉 Analysis Completed Successfully!
        </div>
        """, unsafe_allow_html=True)

