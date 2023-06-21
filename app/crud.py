from sqlalchemy.orm import Session
from . import models
from . import schemas


def create(db: Session, schema: schemas.BookSchema):
    """
    Create a book.

    Args:
        db (Session): The database session object.
        schema (BookSchema): The book schema.

    Returns:
        Book | None: The created book, unless one with the same ISBN already exists.
    """

    existing_book = read(db, schema.isbn)

    if existing_book is not None:
        return None

    book = models.Book(
        isbn=schema.isbn,
        title=schema.title,
        author=schema.author,
        publication_year=schema.publication_year,
        genre=schema.genre,
        price=schema.price,
    )
    db.add(book)
    db.commit()
    db.refresh(book)

    return book


def read(db: Session, isbn: str):
    """
    Read a book.

    Args:
        db (Session): The database session object.
        isbn (str): The ISBN of the book.

    Returns:
        Book | None: The book, if it exists.
    """

    return db.query(models.Book).filter(models.Book.isbn == isbn).first()


def update(db: Session, schema: schemas.BookSchema):
    """
    Update a book.

    Args:
        db (Session): The database session object.
        schema (BookSchema): The book schema.

    Returns:
        Book | None: The book, if it exists.
    """

    book = read(db, schema.isbn)

    if book is None:
        return None

    book.title = schema.title
    book.author = schema.author
    book.publication_year = schema.publication_year
    book.genre = schema.genre
    book.price = schema.price

    db.commit()
    db.refresh(book)

    return book


def delete(db: Session, isbn: str):
    """
    Delete a book.

    Args:
        db (Session): The database session object.
        isbn (str): The ISBN of the book.

    Returns:
        Book | None: The book, if it exists.
    """

    book = read(db, isbn)

    if book is None:
        return None

    db.delete(book)
    db.commit()

    return book


def list_all(db: Session):
    """
    Get all books.

    Args:
        db (Session): The database session object.

    Returns:
        list[Book]: The list of all books.
    """

    return db.query(models.Book).all()
