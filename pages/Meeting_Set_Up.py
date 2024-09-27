import streamlit as st
from datetime import datetime

st.markdown(
    """
    <h3 style='text-align: center;'>🤝   Meeting Set-Up</h3>
    """,
    unsafe_allow_html=True
)


if "participants" not in st.session_state:
    st.session_state.participants = []
if "start_time" not in st.session_state:
    st.session_state.start_time = None

username = st.text_input("Enter your name:")
if st.button("Add Participant"):
    if username and username not in st.session_state.participants:
        st.session_state.participants.append(username) 

meeting_name = st.text_input("Enter a description for the meeting:")


participant_name = st.text_input("Enter a participant's name (or leave blank to finish):")

if st.button("Add Another Participant"):
    if participant_name and participant_name not in st.session_state.participants:
        st.session_state.participants.append(participant_name)

if st.button("Start Meeting"):
    st.session_state.start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.success("Meeting has started!")


if st.button('Meeting Ends Now'):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.error("Meeting has ended!")

    start_time = st.session_state.start_time if st.session_state.start_time else "Not Set"
    
    st.write("Meeting Summary:")
    st.write(f"| **Description** | **Participants** | **Start Time** | **End Time** |")
    st.write(f"| {meeting_name}    | {', '.join(st.session_state.participants)} | {start_time} | {current_time} |")
    
    st.session_state.participants = []

if st.session_state.participants:
    st.write("Participants so far:", ', '.join(st.session_state.participants))
