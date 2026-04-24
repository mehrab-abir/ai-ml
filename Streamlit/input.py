import streamlit as st

st.title("User input:")
st.divider()

name = st.text_input("Enter Name:",placeholder="Your Name...")
age = st.number_input("Age:",placeholder="Your Age...",value=None)

# print(type(age)) # type of number_input is float by default

pressed = st.button("Confirm",type="primary")

if(pressed):
    st.write(f"Name: {name}, Age: {int(age)}")
    
st.divider()

st.header("Add two numbers: ")

num1 = st.number_input("Number 1: ",value=None)
num2 = st.number_input("Number 2: ",value=None)

addBtn = st.button("Add",type="secondary")

if addBtn:
    st.write(f"Result: {num1+num2}")