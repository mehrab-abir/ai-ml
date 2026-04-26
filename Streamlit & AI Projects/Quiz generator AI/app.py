import streamlit as st

st.header("Note Summary and Quiz Generator")
st.subheader("Upload images and have AI make quizzes for you")
st.divider()

with st.sidebar:
    images = st.file_uploader("Upload upto 3 images of your content: ",
                              type=["jpg","jpeg","png"],
                              accept_multiple_files=True)

    if images:
        if(len(images) > 3):
            st.error("Maximum 3 images allowed")
        else:
            st.markdown(":blue[uploaded images:]")
            cols = st.columns(len(images))
            for i,img in enumerate(images):
                with cols[i]:
                    st.image(img)
    
    difficulty = st.selectbox("Choose difficulty level of the quiz:",
                              ("Easy","Medium","Hard"),
                              index=None)

    btn = st.button("Generate Quiz",type="primary")
    
if btn:
    if not images:
        st.error("You must upload at least 1 image")
    if difficulty is None:
        st.error("Select a difficulty level")
        
    if images and difficulty:
        with st.container(border=True):
            st.subheader("Summarized Note:")
            st.write("Note text here....")
        
        with st.container(border=True):
            st.subheader(f"Quiz (Difficulty: {difficulty})")
            st.write("Quiz here....")
            
    
    
    