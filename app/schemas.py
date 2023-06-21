from pydantic import BaseModel


class BookSchema(BaseModel):
    isbn: str
    title: str
    author: str
    publication_year: int
    genre: str
    price: float
