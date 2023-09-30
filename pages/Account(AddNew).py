import streamlit as st
from streamlit.hello.utils import show_code
from urllib.error import URLError
import altair as alt
import pandas as pd
from streamlit_gsheets import GSheetsConnection



# Private Access keys in secrets.toml
def account():
    st.header('Create New')
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)
    df = conn.read(worksheet="Account", usecols=list(range(2)))
    with st.form(key="my_form"):
        st.write("Inside the form")
        accountId = st.text_input("Account ID")
        accountName = st.text_input("Account Name")
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
    if submitted:
        new_account = [{'Identifier': accountId,'Name': accountName}]
        updated_df = pd.DataFrame(new_account)
        # df = df.concat(updated_df)
        conn.update(worksheet="Account", data=updated_df)
        st.write(updated_df)
        st.success("Worksheet Updated 🤓")

# st.set_page_config(page_title="Account Demo")
st.sidebar.header("Account Demo")

account()
show_code(account)
