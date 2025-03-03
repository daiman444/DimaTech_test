from sqlalchemy import(
    Boolean,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import(
    Mapped,
    mapped_column,
    relationship,
)

from db.base import Base


class User(Base):
    name: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        unique=True,
    )
    pass_hash: Mapped[str] = mapped_column(
        String(64),
        nullable=False
    )
    is_admin: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    # relations
    invoices: Mapped[list["Invoice"]] = relationship(
        back_populates="user",
        cascade="all, delete",
    )


class Invoice(Base):
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    balance: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    # relations
    user: Mapped["User"] = relationship(
        back_populates="invoices",
    )
    payments: Mapped[list["Payment"]] = relationship(
        back_populates="invoice",
        cascade="all, delete",
    )


class Payment(Base):
    invoice_id: Mapped[int] = mapped_column(
        ForeignKey("invoices.id"),
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    amount: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    # relations
    invoices: Mapped["Invoice"] = relationship(
        back_populates="payments",
    )
