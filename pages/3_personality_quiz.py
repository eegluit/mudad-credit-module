
import streamlit as st

# Question 1
question_1 = "I am energized by being around people."
options_1 = ["Strongly Agree", "Somewhat Agree", "Somewhat Disagree", "Strongly Disagree"]

# Question 2
question_2 = "I prefer to stick to a set schedule."
options_2 = ["Strongly Agree", "Somewhat Agree", "Somewhat Disagree", "Strongly Disagree"]

# Question 3
question_3 = "I am comfortable taking risks."
options_3 = ["Strongly Agree", "Somewhat Agree", "Somewhat Disagree", "Strongly Disagree"]

# Personality Test
st.title("Personality Test")

q1_answer = st.selectbox(question_1, options_1)
q2_answer = st.selectbox(question_2, options_2)
q3_answer = st.selectbox(question_3, options_3)

if st.button('Submit'):
    st.write("Your answers are:")
    st.write("Q1: " + q1_answer)
    st.write("Q2: " + q2_answer)
    st.write("Q3: " + q3_answer)
