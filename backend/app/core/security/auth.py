from fastapi import HTTPException
from starlette import status

from dependecies.token import TokenDependency
from dependecies.user import UserServiceDependency
from models.user import User


async def get_current_user(
        token: TokenDependency,
        user_service: UserServiceDependency,
) -> User:
    if not (user := await user_service.get_user_or_none(db_id=token.user_id)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user
