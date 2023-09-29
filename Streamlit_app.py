import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Load the Google Sheets URL from the Streamlit secret
sheet_url = st.secrets["public_gsheets_url"]

# Function to load data from Google Sheets
@st.cache_data(ttl=600)
def load_data(url):
    try:
        # Authenticate with Google Sheets using service account credentials
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
        gc = gspread.authorize(creds)
        
        # Open the Google Sheets document
        sheet = gc.open_by_url(url)
        
        # Read the data from the first worksheet
        worksheet = sheet.get_worksheet(0)
        data = worksheet.get_all_records()
        
        return pd.DataFrame(data)
    except Exception as e:
        st.error(f"Error loading data: {e}")

# Load and display the data from Google Sheets
data = load_data(sheet_url)

st.write("Data from Google Sheets:")
st.dataframe(data)