import streamlit as st
import speech_recognition as sr
from datetime import datetime


st.image("meeting.jpeg", width=500)


recognizer = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        st.write("Listening...")

        while st.session_state["listening"]:
            try:
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()
                
                st.session_state["total_speech"] += " " + text
                st.write(text)

            except sr.UnknownValueError:
                st.write("Could not understand audio, please try again.")

if "listening" not in st.session_state:
    st.session_state["listening"] = False

if "total_speech" not in st.session_state:
    st.session_state["total_speech"] = ""


if st.session_state["listening"]:
    if st.button("Stop Listening"):
        st.session_state["listening"] = False
else:
    if st.button("Start Listening"):
        st.session_state["listening"] = True
        recognize_speech()




st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


st.markdown(
     """
 ### Meeting Transcripted:
    
"""
)
st.write(st.session_state["total_speech"])

