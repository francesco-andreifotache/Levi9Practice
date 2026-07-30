from fastapi import FastAPI
import httpx

app = FastAPI()

API_BASE = "http://127.0.0.1:8000"


@app.post("/mcp/tools/get_books_by_author")
def get_books_by_author(author_name: str):

    r = httpx.get(
        f"{API_BASE}/books/author/{author_name}"
    )

    return r.json()


@app.post("/mcp/tools/get_books_by_rating")
def get_books_by_rating(rating: int):

    r = httpx.get(
        f"{API_BASE}/books/rating/{rating}"
    )

    return r.json()


@app.get("/health")
def health():
    return {"status": "ok"}