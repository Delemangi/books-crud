from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Book(Base):
    __tablename__ = "books"

    isbn: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    publication_year: Mapped[int]
    genre: Mapped[str]
    price: Mapped[float]

    def __repr__(self) -> str:
        return f"{self.title!r} ({self.isbn!r})"
