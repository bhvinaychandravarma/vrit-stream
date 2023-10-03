import streamlit as st

# Title
st.title("VR IT Resources")

# Define the URL of the website you want to display
website_url = "https://www.vritresources.com"  # Replace with the URL of the website you want to display

# Use the iframe component to embed the website
st.components.v1.iframe(website_url, width=900, height=500, scrolling=True)
