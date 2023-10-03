import streamlit as st
import pandas as pd
import gspread
from google.oauth2 import service_account
from urllib.error import URLError
from streamlit_gsheets import GSheetsConnection

from streamlit_extras.app_logo import add_logo

# ------------------------------------------------------
# Always display the image without a checkbox
image_url = "https://imgtr.ee/images/2023/09/22/e030c18384c9d684f0f26937bb337c59.jpeg"  # You can change this URL to your desired image
add_logo(image_url)

# Display the image as a header
header_image_url = "https://imgtr.ee/images/2023/09/22/e030c18384c9d684f0f26937bb337c59.jpeg"

# Define the desired width and height for the image
image_width = 400  # Change to your preferred width in pixels
image_height = 100  # Change to your preferred height in pixels

# Use HTML and CSS to create a header with the custom-sized image on the left and the name in the middle
st.markdown(
    f"""
    <style>
        .header {{
            display: flex;
            align-items: center;
            padding: 0;
            margin: 0;
        }}
        .header img {{
            max-width: {image_width}px;
            max-height: {image_height}px;
            margin-right: 10px;
        }}
        .name {{
            display: flex;
            align-items: center;
            justify-content: center;
            height: {image_height}px;
        }}
    </style>
    <div class="header">
        <img src="{header_image_url}" alt="Header Image">
        <div class="name">
            <h1>VR IT RESOURCES LLC</h1>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Buttons to navigate to other pages displayed horizontally
st.markdown('<div class="button-container">', unsafe_allow_html=True)

if st.button("Account", key="Home"):
    # Content for the Home page
    st.write("Welcome to the Home page!")

if st.button("Employee", key="Contact"):
    # Content for the Contact page
    st.write("Contact Us: VR IT RESOURCES LLC")

if st.button("About", key="About"):
    # Content for the Google Site page (embed a WebView)
    st.components.v1.html(
        f'<iframe src="https://www.vritresources.com" width="100%" height="500px"></iframe>',
        width=800,
        height=600,
    )

st.markdown('</div>', unsafe_allow_html=True)  # Close the button-container div

# Center-align the text below the header
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <p>👋 VR IT CRM PLATFORM!!</p>
    </div>
    """,
    unsafe_allow_html=True,
)