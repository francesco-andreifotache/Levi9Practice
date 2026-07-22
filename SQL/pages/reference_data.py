import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
import pandas as pd

from api_client import APIClient

st.title("Reference Data")

if st.button("🔄 Refresh"):
    st.rerun()

tab1, tab2, tab3 = st.tabs(["Genres", "Authors", "Tags"])

with tab1:
    genres, error = APIClient.get("/genres")

    if error:
        st.error(error)
    else:
        st.dataframe(pd.DataFrame(genres))

with tab2:
    authors, error = APIClient.get("/authors")

    if error:
        st.error(error)
    else:
        st.dataframe(pd.DataFrame(authors))

with tab3:
    tags, error = APIClient.get("/tags")

    if error:
        st.error(error)
    else:
        st.dataframe(pd.DataFrame(tags))