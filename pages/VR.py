import streamlit as st
import pandas as pd
import numpy as np

# Display the image as a header
header_image_url = "https://imgtr.ee/images/2023/09/22/e030c18384c9d684f0f26937bb337c59.jpeg`"


# Display the image as a header
header_image_url = "https://imgtr.ee/images/2023/09/22/e030c18384c9d684f0f26937bb337c59.jpeg"

# Use HTML and CSS to create a header with the image on the left and the name in the middle
st.markdown(
    f"""
    <style>
        .header {{
            display: flex;
            align-items: center;
            padding: 10px;
        }}
        .header img {{
            max-width: 120px;
            margin-right: 10px;
        }}
        .name {{
            display: flex;
            align-items: center;
            justify-content: center;
            height: 120px;
        }}
    </style>
    <div class="header">
        <img src="{header_image_url}" alt="Header Image">
        <div class="name">
            <h1>VR IT RESOURCES</h1>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Center-align the text below the header
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <p>👋 VR IT CRM PLATFORM!!</p>
    </div>
    """,
    unsafe_allow_html=True,
)


st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)


hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)


# ---------------------------
# Code to extract the sheet id

import streamlit as st

# Load the sheet ID from the Streamlit secret
sheet_url = st.secrets["public_gsheets_url"]

# Extract the sheet ID from the URL
sheet_id = sheet_url.split("/")[5]

# Print the extracted sheet ID
st.write(f"Sheet ID: {sheet_id}")
# ---------------------------