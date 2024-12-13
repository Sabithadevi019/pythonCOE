import streamlit as st
st.title("Even and odd numbers")
n1=st.number_input("First number")
if st.button("number"):
    if n1%2==0:
        st.success("Number is Even")
    else:
        st.error("Number is Odd")