from typing import Any, Optional, Sequence

from sqlalchemy import exists, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from enums.task import TaskStatus
from models.task import Task
from repositories.base import BaseRepository


class TaskRepository(BaseRepository[Task]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Task, session)

    async def get_by_user_id(self, user_id: int) -> Optional[Task]:
        stmt = select(self.model).where(self.model.user_id == user_id)
        scalar = await self.session.scalars(stmt)
        return scalar.one_or_none()

    async def put_by_user_id(self, user_id: int, obj_in: dict[str, Any]) -> Task:
        if not (obj := await self.get_by_user_id(user_id)):
            return await self.create(obj_in)
        return await self.update(obj, obj_in)

    async def count(self, user_id: int) -> int:
        stmt = (
            select(func.count(Task.id))
            .where(Task.user_id == user_id)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def get_by_status(
            self,
            user_id: int,
            status: TaskStatus,
    ) -> Optional[Sequence[Task]]:
        stmt = (
            select(self.model)
            .where(Task.user_id == user_id)
            .where(Task.status == status)
        )
        result = await self.session.execute(stmt)
        return result.scalar_all()
