import streamlit as st
import re

st.set_page_config(page_title="User Form", page_icon=":guardsman:", layout="wide")

def show_form():
    st.title("Personal Information")
    with st.form("unique_form_key"):
        f_name = st.text_input("Enter your First name:")
        l_name = st.text_input("Enter your Last name:")
        gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
        email = st.text_input("Enter your email:")
        age = st.text_input("Enter your age:")
        profession = st.text_input("Enter your Profession: ")
        employer = st.text_input("Enter your Employer Name")
        employer_add = st.text_input("Enter your Employer's Address: ")
        base_salary = st.text_input("Enter your Monthly Base Salary: ")
        
        
        # attachment = st.file_uploader("Upload your attachment:", type=["csv", "txt", "pdf"])
        if st.form_submit_button('Submit'):
            email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
            if email_pattern.match(email):
                if age.isnumeric():
                    st.success("First Name: " + f_name)
                    st.success("Last Name: " + l_name)
                    st.success("Email: " + email)
                    st.success("Age: " + age)
                    st.success("Gender: " + gender)
                    st.success("Profession: " + profession)
                    st.success("Employer Name: " + employer)
                    st.success("Employer Address: " + employer_add)
                    st.success("Your Monthly Base Salary: " + base_salary)


                    
                    st.write("Thank you for submitting the form.")
                    st.markdown("<style> .stFormContainer{display: none;} </style>", unsafe_allow_html=True)
                else:
                    st.error("Invalid age")
            else:
                st.error("Invalid email address")

show_form()