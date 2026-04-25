import streamlit as st

st.title(":blue[Image Uploader:]",anchor=False)
st.divider()

# upload one image
st.header("One Image: ")
image = st.file_uploader("Upload image: ",
                         type=["jpg","png","jpeg","webp","avif"])

if(image):
    st.image(image)

st.divider()

st.header("Multiple image:")
images = st.file_uploader("Upload images: ",
                          type=["jpg","jpeg","png","avif","webp"],
                          accept_multiple_files=True,
                          key="uploader-1")

if(images):
    st.image(images)
    
st.divider()

## If there are multiple file uploaders, we must use unique key for each of them

st.header("Multiple image - show in colums:")
imageCols = st.file_uploader("Upload images: ",
                          type=["jpg","jpeg","png","avif","webp"],
                          accept_multiple_files=True,
                          key="uploader-2")

if(imageCols):
    cols = st.columns(len(imageCols))
    
    for i,singleImage in enumerate(imageCols):
        with cols[i]:
            st.image(singleImage)

st.divider()
st.header("Image from local directory:")
st.image("images/nature-1.jpg")

st.divider()
st.header("Image from internet via link:")
st.image("https://postquantum.com/wp-content/uploads/2018/12/Superconducting-Quantum-Computer-1536x977.jpg.webp")