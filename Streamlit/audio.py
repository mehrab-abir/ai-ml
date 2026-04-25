import streamlit as st

st.title(":blue[Audio Uploader:]",anchor=False)
st.divider()

st.audio("audios/game_of_thrones.mp3",loop=True)

audio = st.file_uploader("Upload audio: ",
                         type=["mp3","aac"])

if(audio):
    st.audio(audio)