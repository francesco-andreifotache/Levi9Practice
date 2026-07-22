import streamlit as st


def get_default_api_base_url() -> str:
    """Get the default API base URL."""
    return "http://127.0.0.1:8000"


def get_api_base_url() -> str:
    """Get the current API base URL from session state."""

    # Initialize session state for API configuration if it doesn't exist
    if "api_base_url" not in st.session_state:
        st.session_state.api_base_url = get_default_api_base_url()

    return st.session_state.api_base_url


def set_api_base_url(url: str) -> None:
    """Set the API base URL in session state."""
    st.session_state.api_base_url = url
