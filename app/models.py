from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Variable(Base):
    __tablename__ = "variables"

    name: Mapped[str] = mapped_column(primary_key=True)
    value: Mapped[str] = mapped_column(default="")

    def __repr__(self) -> str:
        return f"{self.name!r} = {self.value!r}>"
