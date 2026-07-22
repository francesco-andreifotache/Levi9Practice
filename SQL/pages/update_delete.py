import streamlit as st
from api_client import APIClient



st.title("✏️ Update & Delete")

# ====================================================
# UPDATE BOOK
# ====================================================

st.header("Update Book")

book_id = st.number_input(
    "Book ID",
    min_value=1,
    step=1
)

with st.form("update_book"):

    title = st.text_input("Title (optional)")
    upc = st.text_input("UPC (optional)")

    genre_id = st.text_input(
        "Genre ID (optional)"
    )

    author_id = st.text_input(
        "Author ID (optional)"
    )

    update_btn = st.form_submit_button(
        "Update Book"
    )

    if update_btn:

        payload = {}

        if title:
            payload["title"] = title

        if upc:
            payload["upc"] = upc

        if genre_id:
            payload["genre_id"] = int(genre_id)

        if author_id:
            payload["author_id"] = int(author_id)

        if not payload:
            st.warning(
                "Provide at least one field"
            )

        else:

            data, error = APIClient.put(
                f"/books/{book_id}",
                payload
            )

            if error:
                st.error(error)
            else:
                st.success("Book updated")
                st.json(data)

# ====================================================
# DELETE BOOK
# ====================================================

st.divider()

st.header("Delete Book")

delete_book_id = st.number_input(
    "Book ID to delete",
    min_value=1,
    step=1,
    key="delete_book"
)

confirm_book = st.checkbox(
    "I confirm deleting this book"
)

if st.button("Delete Book"):

    if not confirm_book:
        st.warning(
            "Confirmation required"
        )

    else:

        success, error = APIClient.delete(
            f"/books/{delete_book_id}"
        )

        if success:
            st.success(
                "Book deleted successfully"
            )
        else:
            st.error(error)

# ====================================================
# DELETE BOOK DETAIL
# ====================================================

st.divider()

st.header("Delete Book Detail")

detail_id = st.number_input(
    "Detail ID",
    min_value=1,
    step=1,
    key="detail_delete"
)

confirm_detail = st.checkbox(
    "I confirm deleting this detail"
)

if st.button("Delete Detail"):

    if not confirm_detail:
        st.warning(
            "Confirmation required"
        )

    else:

        success, error = APIClient.delete(
            f"/book-details/{detail_id}"
        )

        if success:
            st.success(
                "Book detail deleted"
            )
        else:
            st.error(error)