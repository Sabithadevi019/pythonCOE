import streamlit as st
salary=st.number_input("Enter your salary")
b1=st.number_input("Enter your b1")
b2=st.number_input("Enter your b2")
b3=st.number_input("Enter your b3")
total=b1+b2+b3
if st.button("total"):
    st.text(total)
if st.button("percentage"):
    st.text(total*100/salary)

