import streamlit as st
from api_client import APIClient

st.title("📖 Book Details Explorer")

# ==========================
# BOOK SEARCH
# ==========================

st.header("Search Book by ID")

book_id = st.number_input(
    "Book ID",
    min_value=1,
    step=1
)

if st.button("Load Book"):
    data, error = APIClient.get(f"/books/{book_id}")

    if error:
        st.error(f"❌ {error}")
    else:
        st.success("Book found")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**ID:**", data["id"])
            st.write("**Title:**", data["title"])
            st.write("**UPC:**", data["upc"])

        with col2:
            st.write("**Genre ID:**", data["genre_id"])
            st.write("**Author ID:**", data["author_id"])

# ==========================
# ALL BOOK DETAILS
# ==========================

st.divider()

st.header("All Book Details")

if st.button("Refresh Book Details"):
    st.session_state["reload_details"] = True

data, error = APIClient.get("/book-details")

if error:
    st.error(error)

elif data:
    st.dataframe(
        data,
        use_container_width=True
    )

else:
    st.info("No book details found")