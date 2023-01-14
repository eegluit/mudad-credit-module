import streamlit as st
import re

st.set_page_config(page_title="User Form", page_icon=":guardsman:", layout="wide")

def show_form():

    with st.form("unique_form_key"):
        name = st.text_input("Enter your name:")
        email = st.text_input("Enter your email:")
        age = st.text_input("Enter your age:")
        gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
        # attachment = st.file_uploader("Upload your attachment:", type=["csv", "txt", "pdf"])
        if st.form_submit_button('Submit'):
            email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
            if email_pattern.match(email):
                if age.isnumeric():
                    st.success("Name: " + name)
                    st.success("Email: " + email)
                    st.success("Age: " + age)
                    st.success("Gender: " + gender)
                    
                    st.write("Thank you for submitting the form.")
                    st.markdown("<style> .stFormContainer{display: none;} </style>", unsafe_allow_html=True)
                else:
                    st.error("Invalid age")
            else:
                st.error("Invalid email address")

show_form()