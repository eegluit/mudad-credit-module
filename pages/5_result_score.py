import pandas as pd
import streamlit as st


result = pd.read_csv('data.csv')
lr = result.index[-1]
last_row = result.tail(1)
st.dataframe(last_row)

credit_score = last_row['Final Marks'][lr]


# Create a credit score variable
# credit_score = 770

# Create a new page
st.title(":red[Mala Credit Score]")

# Display the credit score
st.write("Your mala credit score is:", credit_score)

# Add some congratulations
if credit_score >= 3:
    st.success("Congratulations! Your credit score is excellent.")
    st.write("🎉 🎉 🎉")
    st.snow()
else:
    st.warning("Your credit score is good but you may want to improve it.")
    

