import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
        }
        .stButton > button {
            background-color: #27B7A6; /* Green */
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #27B7A6;
        }
        .stTextArea {
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Speech-to-Text function
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Say something...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            st.success(f"You said: {text}")
        except sr.UnknownValueError:
            st.error("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition service; {e}")

# Text-to-Speech function
def text_to_speech(text):
    if text:
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        st.audio("output.mp3", format="audio/mp3")

# Streamlit app layout
st.title("Speech-to-Text and Text-to-Speech App")

# Select mode
mode = st.selectbox("Choose a mode", ["Speech-to-Text", "Text-to-Speech"])

# Speech-to-Text Mode
if mode == "Speech-to-Text":
    st.header("Convert Speech to Text")
    if st.button("Start Recording"):
        with st.spinner("Listening..."):
            speech_to_text()

# Text-to-Speech Mode
if mode == "Text-to-Speech":
    st.header("Convert Text to Speech")
    user_input = st.text_area("Enter text to convert into speech:")
    if st.button("Convert to Speech"):
        with st.spinner("Converting..."):
            text_to_speech(user_input)
