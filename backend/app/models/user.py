import asyncio
from datetime import datetime
from typing import Optional, TYPE_CHECKING

from sqlalchemy import BigInteger, event, ForeignKey, String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import DBModel
from models.mixins import CreatedAtMixin


if TYPE_CHECKING:
    from models.task import Task


class User(DBModel, CreatedAtMixin):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(200))
    password: Mapped[str] = mapped_column(String)
    tasks: Mapped[list["Task"]] = relationship(back_populates="user")
