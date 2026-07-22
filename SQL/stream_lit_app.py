import streamlit as st

from api_client import APIClient
from settings import (
    get_api_base_url,
    set_api_base_url
)

st.set_page_config(
    page_title="API Health",
    page_icon="🔌"
)

st.title("API Health + Setup")

st.write(
    "Configure the FastAPI URL and test the connection."
)

api_url = st.text_input(
    "API Base URL",
    value=get_api_base_url()
)

set_api_base_url(api_url)

if st.button("Test Connection"):

    result = APIClient.test_connection("/genres")

    if result.success:
        st.success(result.message)
    else:
        st.error(result.message)

