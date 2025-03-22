from typing import Optional, TYPE_CHECKING

from sqlalchemy import ForeignKey, String, ARRAY, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import DBModel
from models.mixins import CreatedAtMixin, UpdatedAtMixin

from enums.task import TaskStatus

if TYPE_CHECKING:
    from models.user import User


class Task(DBModel, CreatedAtMixin, UpdatedAtMixin):
    __tablename__ = "tasks"

    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(600))
    status: Mapped[TaskStatus] = mapped_column(
        default=TaskStatus.NOT_COMPLETED,
        server_default=str(TaskStatus.NOT_COMPLETED),
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(
        back_populates="tasks",
        lazy="joined",
    )
