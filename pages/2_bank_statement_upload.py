
import streamlit as st
import pandas as pd

import os
import tabula

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "pdf"])

# Check if a file was uploaded
if uploaded_file:
    # Do something with the file, e.g. read and display its contents
    _, file_extension = os.path.splitext(uploaded_file.name)
    if file_extension == '.csv':
        df = pd.read_csv(uploaded_file)
        st.write(df)
    elif file_extension == '.xlsx':
        df = pd.read_excel(uploaded_file)
        st.write(df)
    elif file_extension == '.pdf':
        # st.pdf_viewer(uploaded_file)
        df = tabula.read_pdf(uploaded_file, pages='all')[0]
        tabula.convert_into(uploaded_file, "convertedpdf.csv", output_format="csv", pages='all')
        df2 = pd.read_csv('convertedpdf.csv', error_bad_lines=False)

        st.write(df2)

    else:
        st.warning("Please upload a valid file type i.e csv, excel or pdf")

