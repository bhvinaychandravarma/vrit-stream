import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Define the Google Sheets URL of your spreadsheet
url = "https://docs.google.com/spreadsheets/d/1RtFzgofq0fDR524zKxjNYishHvwJB5rwEINAvA7eg5g/edit?usp=sharing"

# Connect to the Google Sheets document
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

# Read data from the Google Sheets spreadsheet
data = conn.read(spreadsheet=url, usecols=[0, 1])

# Display the data in a DataFrame
st.write("Data from Google Sheets:")
st.dataframe(data)
