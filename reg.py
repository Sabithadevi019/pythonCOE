import streamlit as st
st.title("Registration Form")
num=st.number_input("Enter a number")
name=st.text_input("Enter your name")
age=st.number_input("Enter your age")
Hobbies=st.selectbox("Select your Hobby",["Chess","Badminton","Reading","Drawing"])
gender=st.radio("Select your gender",["Male","Female"])
if gender=="Male":
    st.success("Male")
else:
    st.success("Female")
languages=st.selectbox("Select your language",["Telugu","English","Hindi"])
if languages=="English":
    st.success("English")
elif languages=="Hindi":
    st.success("Hindi")
else:
    st.success("English")
if st.button("Submit"):
    st.success("Successfully submitted")
if st.checkbox("agree"):
    st.success("Agreed to terms and conditions")