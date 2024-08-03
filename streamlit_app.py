import streamlit as st
import pandas as pd

# Title of the app
st.title('Data Display with Streamlit')

# Load data
file_path = 'E:\\Project\\automationpatch\\test.csv'  # Replace with your file path
data = pd.read_csv(file_path)  # Use read_csv for CSV files

# Display the data
st.write(data)
