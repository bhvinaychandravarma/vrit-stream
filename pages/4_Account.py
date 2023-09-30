import streamlit as st
from streamlit.hello.utils import show_code
from urllib.error import URLError
import altair as alt
import pandas as pd
from streamlit_gsheets import GSheetsConnection


def account_public():
    st.header('Show Pulic Sample Data')
    # Public Google Sheet
    public_gsheets_url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"
    # Google Sheet Shared as "Anyone with a link"
    gsheets_url = "https://docs.google.com/spreadsheets/d/1r8D3RX_A8YM05o1MJW0Rib8eesRspbbiuvXex4IXY_I/edit?usp=sharing"
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)
    data = conn.read(spreadsheet=gsheets_url, usecols=[0, 1])
    st.dataframe(data)

# Private Access keys in secrets.toml
def account():
    st.header('Show Sample Data')
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)
    data = conn.read(worksheet="Account", usecols=[0, 1,2,3,4])
    st.dataframe(data)    



# st.set_page_config(page_title="Account Demo")
st.sidebar.header("Account Demo")

account()
show_code(account)
