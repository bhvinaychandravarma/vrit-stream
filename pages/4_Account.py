import streamlit as st
from streamlit.hello.utils import show_code


from urllib.error import URLError

import altair as alt
import pandas as pd


def account():
    st.write('Begin')




st.set_page_config(page_title="Account Demo")
st.markdown("# Account Demo")
st.sidebar.header("Account Demo")
st.write("Accounts is in CONSTRUCTION")

account()
show_code(account)
