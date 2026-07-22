from pydantic import BaseModel, ConfigDict, Field


class BookResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    upc: str
    genre_id: int
    author_id: int


class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=300)
    upc: str = Field(..., min_length=1, max_length=20)
    genre_id: int
    author_id: int


class BookUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=300)
    upc: str | None = Field(None, min_length=1, max_length=20)
    genre_id: int | None = None
    author_id: int | None = None

class BookDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    book_id: int
    rating: int
    price: float
    availability: int

class BookDetailCreate(BaseModel):
    book_id: int
    rating: int = Field(..., ge=1, le=5)
    price: float = Field(..., ge=0)
    availability: int = Field(..., ge=0)

class GenreResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class AuthorResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    country: str | None = None


class TagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str