
import streamlit as st
basic=st.number_input("Enter your basic salary:")
if st.button("gross"):
    if basic<10000:
        hra=(67/100)*basic
        da=(73/100)*basic
    elif basic<20000:
        hra=(69/100)*basic
        da=(76/100)*basic
    else:
        hra=(73/100)*basic
        da=(81/100)*basic
    gross=hra+da+basic
    st.text(gross)