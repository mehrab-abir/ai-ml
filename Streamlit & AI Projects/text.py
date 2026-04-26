import streamlit as st

st.title("Hello, Streamlit ")

st.header("This is a header")

st.subheader("This is a sub-header",divider=True)

st.text("This is some text")

st.markdown("This is a markdown text, can be :green[colorized], **bold text**, *italic text* etc.")

st.markdown(":orange-background[Text with a Background]")