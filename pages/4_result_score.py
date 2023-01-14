
import streamlit as st

# Create a credit score variable
credit_score = 775

# Create a new page
st.header("Mala Credit Score")

# Display the credit score
st.write("Your mala credit score is:", credit_score)

# Add some congratulations
if credit_score >= 700:
    st.success("Congratulations! Your credit score is excellent.")
else:
    st.warning("Your credit score is good but you may want to improve it.")
    
st.write("🎉 🎉 🎉")
