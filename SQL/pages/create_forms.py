import streamlit as st
from api_client import APIClient



st.title("➕ Create Books & Book Details")

# =====================================================
# CREATE BOOK
# =====================================================

st.header("Create Book")

with st.form("book_form"):

    title = st.text_input("Title")
    upc = st.text_input("UPC")
    genre_id = st.number_input(
        "Genre ID",
        min_value=1,
        step=1
    )
    author_id = st.number_input(
        "Author ID",
        min_value=1,
        step=1
    )

    submit_book = st.form_submit_button("Create Book")

    if submit_book:

        if not title.strip():
            st.error("Title is required")

        elif not upc.strip():
            st.error("UPC is required")

        else:

            payload = {
                "title": title,
                "upc": upc,
                "genre_id": int(genre_id),
                "author_id": int(author_id)
            }

            data, error = APIClient.post(
                "/books",
                payload
            )

            if error:
                st.error(error)
            else:
                st.success("✅ Book created successfully")
                st.json(data)

# =====================================================
# CREATE BOOK DETAIL
# =====================================================

st.divider()

st.header("Create Book Detail")

with st.form("detail_form"):

    book_id = st.number_input(
        "Book ID",
        min_value=1,
        step=1
    )

    rating = st.number_input(
        "Rating",
        min_value=1,
        max_value=5,
        step=1
    )

    price = st.number_input(
        "Price",
        min_value=0.0,
        step=0.01
    )

    availability = st.number_input(
        "Availability",
        min_value=0,
        step=1
    )

    submit_detail = st.form_submit_button(
        "Create Book Detail"
    )

    if submit_detail:

        payload = {
            "book_id": int(book_id),
            "rating": int(rating),
            "price": float(price),
            "availability": int(availability)
        }

        data, error = APIClient.post(
            "/book-details",
            payload
        )

        if error:
            st.error(error)
        else:
            st.success("✅ Book detail created successfully")
            st.json(data)