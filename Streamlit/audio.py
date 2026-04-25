import streamlit as st

st.title(":blue[Audio Uploader:]",anchor=False)
st.divider()

st.audio("audios/game_of_thrones.mp3",loop=True)