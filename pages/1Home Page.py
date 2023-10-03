import streamlit as st
import pandas as pd
import gspread
from google.oauth2 import service_account
from urllib.error import URLError
from streamlit_gsheets import GSheetsConnection
from streamlit_extras.app_logo import add_logo

# ------------------------------------------------------

# Load the Google Sheets URL from the Streamlit secret
sheet_url = st.secrets["private_gsheets_url"]

# ------------------------------------------------------
# Function to authenticate and return a Google Sheets client
def get_google_sheets_client():
    creds_info = st.secrets["gcp_service_account"]
    creds = service_account.Credentials.from_service_account_info(
        {
            "type": creds_info["type"],
            "project_id": creds_info["project_id"],
            "private_key_id": creds_info["private_key_id"],
            "private_key": creds_info["private_key"],
            "client_email": creds_info["client_email"],
            "client_id": creds_info["client_id"],
            "auth_uri": creds_info["auth_uri"],
            "token_uri": creds_info["token_uri"],
            "auth_provider_x509_cert_url": creds_info["auth_provider_x509_cert_url"],
            "client_x509_cert_url": creds_info["client_x509_cert_url"],
        },
        scopes=[
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ],
    )

    # Authenticate with gspread using the credentials
    gc = gspread.Client(auth=creds)
    gc.session.headers["Connection"] = "Keep-Alive"
    gc.login()
    
    return gc

# Function to load data from Google Sheets
@st.cache_data(ttl=600)
def load_data(url):
    try:
        # Get the Google Sheets client
        gc = get_google_sheets_client()

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

# ------------------------------------------------------
# Create a sidebar for navigation
st.sidebar.title("CRM Navigation")
selected_page = st.sidebar.radio("Select Page", ["Dashboard", "Vendor Management", "Employee Management"])

# Create a main content area
st.title("CRM Platform")

if selected_page == "Dashboard":
    st.subheader("Dashboard Content Goes Here")
elif selected_page == "Vendor Management":
    st.subheader("Vendor Management Content Goes Here")
else:
    st.subheader("Employee Management Content Goes Here")

# ------------------------------------------------------
# Colouring
# Set Streamlit theme with colorful styles
def set_colorful_theme():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #e1eaff; /* Background color */
            color: #333; /* Text color */
        }
        .sidebar .sidebar-content {
            background-color: #003f5c; /* Sidebar background color */
            color: #fff; /* Sidebar text color */
        }
        .st-ck {
            background-color: #58508d; /* Streamlit components background color */
            color: #fff; /* Streamlit components text color */
        }
        .st-dx {
            background-color: #bc5090; /* Streamlit components accent color */
            color: #fff; /* Streamlit components accent text color */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

set_colorful_theme()

# --------------------------------------------------
# Example: Add a search box for vendors and employees
if selected_page == "Vendor Management" and data is not None:
    search_term = st.text_input("Search Vendor")
    # Use "Account Name" for filtering
    filtered_vendors = data[data["Account Name"].str.contains(search_term, case=False)]
    st.dataframe(filtered_vendors)

if selected_page == "Employee Management" and data is not None:
    search_term_employee = st.text_input("Search Employee")
    # Use "Account Name" for filtering
    filtered_employees = data[data["Account Name"].str.contains(search_term_employee, case=False)]
    st.dataframe(filtered_employees)

# --------------------------------------------------
if selected_page == "Vendor Management" and data is not None:
    st.subheader("Add New Vendor")
    
    # Create input fields for vendor data
    vendor_name = st.text_input("Account Name")
    vendor_contact = st.text_input("Contact Number")

    # Add a button to submit the new vendor data
    if st.button("Add Vendor"):
        # Create a dictionary with the new data
        new_vendor = {"Account Name": vendor_name, "Contact Number": vendor_contact}
        
        # Append the new data to the DataFrame
        data = data.append(new_vendor, ignore_index=True)
        
        # Update the Google Sheets document with the new data
        try:
            gc = get_google_sheets_client()  # Get the Google Sheets client again
            worksheet = gc.open_by_url(sheet_url).get_worksheet(0)  # Open the worksheet
            worksheet.insert_rows([list(new_vendor.values())], value_input_option='USER_ENTERED')
            
            st.success("Vendor added successfully!")
        except Exception as e:
            st.error(f"Error adding vendor: {e}")

if selected_page == "Vendor Management" and data is not None:
    st.subheader("Add New Vendor")
    
    # Generate unique keys for the input fields
    vendor_name_key = "vendor_name_input"
    vendor_contact_key = "vendor_contact_input"
    
    # Create input fields for vendor data with unique keys
    vendor_name = st.text_input("Account Name", key=vendor_name_key)
    vendor_contact = st.text_input("Contact Number", key=vendor_contact_key)

    # Add a button to submit the new vendor data
    if st.button("Add Vendor"):
        # Create a list with the new data
        new_vendor = [vendor_name, vendor_contact]
        
        # Append the new data to the DataFrame
        data = data.append(pd.Series(new_vendor, index=data.columns), ignore_index=True)
        
        # Update the Google Sheets document with the new data
        try:
            gc = get_google_sheets_client()  # Get the Google Sheets client again
            worksheet = gc.open_by_url(sheet_url).get_worksheet(0)  # Open the worksheet

            # Append the new data to the worksheet (at the end)
            worksheet.append_rows([new_vendor], value_input_option='USER_ENTERED')
            
            st.success("Vendor added successfully!")
        except Exception as e:
            st.error(f"Error adding vendor: {e}")

