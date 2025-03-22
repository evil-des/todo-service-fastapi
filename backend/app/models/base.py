from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class DBModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
