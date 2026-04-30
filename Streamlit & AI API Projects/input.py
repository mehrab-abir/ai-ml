import streamlit as st

st.title("User input:",anchor=False)
st.divider()

name = st.text_input("Enter Name:",placeholder="Your Name...")
age = st.number_input("Age:",placeholder="Your Age...",value=None)

# print(type(age)) # type of number_input is float by default

pressed = st.button("Confirm",type="primary")

if(pressed):
    st.write(f"Name: {name}, Age: {int(age)}")
    
st.divider()

st.header(":green[Selection Box:]",anchor=False)
selected = st.selectbox("Your Profession: ",
                        ("Student","Engineer","Doctor","Govt. Employee"),
                        index=None,
                        accept_new_options=True
                    )
# index=None --> no value will be selected by default
# accept_new_options=True --> let user enter other options
if selected:
    st.write("Profession Selected: ",selected)
    
    
st.divider()

st.header("Add two numbers: ",anchor=False)

num1 = st.number_input("Number 1: ",value=None)
num2 = st.number_input("Number 2: ",value=None)

addBtn = st.button("Add",type="secondary")

if addBtn:
    st.write(f"Result: {num1+num2}")
    