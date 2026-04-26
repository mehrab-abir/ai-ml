import streamlit as st

st.header("Calculator")
st.divider()

col1, col2 = st.columns(2)

num1 = col1.number_input("Number 1:",value=None)
num2 = col2.number_input("Number 2:",value=None)

op, btn = st.columns(2)

operation = op.selectbox("Select operation: ",
             ("+","-","/","*"))

enterBtn = st.button("Enter",type="primary")

if enterBtn:
    if(operation == '+'):
        st.markdown(f"**= {num1+num2}**")
    elif(operation == '-'):
        st.markdown(f"**= {num1-num2}**")
    elif(operation == '/'):
        try:
            result = num1/num2
        except ZeroDivisionError:
            st.error("Divider can not be zero")
        else:
            st.markdown(f"**= {result}**")
    else:
        st.markdown(f"**= {num1*num2}**")