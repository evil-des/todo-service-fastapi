from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_session


SessionDependency = Annotated[AsyncSession, Depends(get_session)]
