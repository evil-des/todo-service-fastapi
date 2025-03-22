from typing import Any, Optional

from sqlalchemy import exists, func, select, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload, aliased

from models.user import User
from repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(User, session)

    async def get_by_username(self, username: str) -> Optional[User]:
        stmt = select(self.model).where(self.model.username == username)
        scalar = await self.session.scalars(stmt)
        return scalar.one_or_none()
