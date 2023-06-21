import time

from fastapi import Depends, FastAPI
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

from app.crud import create, delete, list_all, read, update
from app.db import SessionLocal, engine
from app.models import Base
from app.schemas import BookSchema

app = FastAPI()

for i in range(5):
    try:
        Base.metadata.create_all(bind=engine)
        break
    except OperationalError:
        time.sleep(i + 1)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.post("/create")
async def create_book(schema: BookSchema, db: Session = Depends(get_db)):
    book = create(db, schema)

    if book is None:
        return {"message": "Book already exists"}
    else:
        return book


@app.get("/read/{isbn}")
async def read_book(isbn: str, db: Session = Depends(get_db)):
    book = read(db, isbn)

    if book is None:
        return {"message": "Book not found"}
    else:
        return book


@app.post("/update")
async def update_book(schema: BookSchema, db: Session = Depends(get_db)):
    book = update(db, schema)

    if book is None:
        return {"message": "Book not found"}
    else:
        return book


@app.post("/delete/{isbn}")
async def delete_book(isbn: str, db: Session = Depends(get_db)):
    book = delete(db, isbn)

    if book is None:
        return {"message": "Book not found"}
    else:
        return book


@app.get("/list")
async def list_all_books(db: Session = Depends(get_db)):
    return list_all(db)
