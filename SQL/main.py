from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from SQL.create_tables import Book, Genre, Author, BookDetail, Tag
from SQL.schemas import BookResponse, BookCreate, BookUpdate
from SQL.schemas import BookDetailResponse
from SQL.schemas import BookDetailCreate
from SQL.schemas import GenreResponse
from SQL.schemas import AuthorResponse
from SQL.schemas import TagResponse

app = FastAPI()

DATABASE_URL = "postgresql://postgres:admin@localhost/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/books", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()


@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book

@app.get(
    "/book-details",
    response_model=list[BookDetailResponse]
)
def get_book_details(db: Session = Depends(get_db)):
    return db.query(BookDetail).all()

@app.get(
    "/book-details/{detail_id}",
    response_model=BookDetailResponse
)
def get_book_detail(
    detail_id: int,
    db: Session = Depends(get_db)
):
    detail = db.query(BookDetail).filter(
        BookDetail.id == detail_id
    ).first()

    if not detail:
        raise HTTPException(
            status_code=404,
            detail="Book detail not found"
        )

    return detail

@app.post(
    "/book-details",
    response_model=BookDetailResponse,
    status_code=201
)
def create_book_detail(
    detail_data: BookDetailCreate,
    db: Session = Depends(get_db)
):

    book = db.query(Book).filter(
        Book.id == detail_data.book_id
    ).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    existing_detail = db.query(BookDetail).filter(
        BookDetail.book_id == detail_data.book_id
    ).first()

    if existing_detail:
        raise HTTPException(
            status_code=400,
            detail="Book already has details"
        )

    detail = BookDetail(
        book_id=detail_data.book_id,
        rating=detail_data.rating,
        price=detail_data.price,
        availability=detail_data.availability
    )

    db.add(detail)
    db.commit()
    db.refresh(detail)

    return detail

from fastapi import HTTPException

@app.delete("/book-details/{detail_id}", status_code=204)
def delete_book_detail(
    detail_id: int,
    db: Session = Depends(get_db)
):

    detail = db.query(BookDetail).filter(
        BookDetail.id == detail_id
    ).first()

    if not detail:
        raise HTTPException(
            status_code=404,
            detail="Book detail not found"
        )

    db.delete(detail)
    db.commit()

    return



@app.post("/books", response_model=BookResponse, status_code=201)
def create_book(
    book_data: BookCreate,
    db: Session = Depends(get_db)
):

    genre = db.query(Genre).filter(
        Genre.id == book_data.genre_id
    ).first()

    if not genre:
        raise HTTPException(
            status_code=404,
            detail="Genre not found"
        )

    author = db.query(Author).filter(
        Author.id == book_data.author_id
    ).first()

    if not author:
        raise HTTPException(
            status_code=404,
            detail="Author not found"
        )

    existing_book = db.query(Book).filter(
        Book.upc == book_data.upc
    ).first()

    if existing_book:
        raise HTTPException(
            status_code=400,
            detail="UPC already exists"
        )

    book = Book(
        title=book_data.title,
        upc=book_data.upc,
        genre_id=book_data.genre_id,
        author_id=book_data.author_id
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    return book


@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book_data: BookUpdate,
    db: Session = Depends(get_db)
):

    book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    updates = book_data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(book, key, value)

    db.commit()
    db.refresh(book)

    return book


@app.delete("/books/{book_id}", status_code=204)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
):

    book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    detail = db.query(BookDetail).filter(
        BookDetail.book_id == book_id
    ).first()

    if detail:
        db.delete(detail)

    db.delete(book)

    db.commit()

    return

@app.get(
    "/genres",
    response_model=list[GenreResponse]
)
def get_genres(db: Session = Depends(get_db)):
    return db.query(Genre).all()

@app.get(
    "/authors",
    response_model=list[AuthorResponse]
)
def get_authors(db: Session = Depends(get_db)):
    return db.query(Author).all()

@app.get(
    "/tags",
    response_model=list[TagResponse]
)
def get_tags(db: Session = Depends(get_db)):
    return db.query(Tag).all()
