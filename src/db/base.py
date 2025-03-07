from sqlalchemy import Integer
from sqlalchemy.orm import(
    DeclarativeBase,
    declared_attr,
    Mapped,
    mapped_column,
)

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"
