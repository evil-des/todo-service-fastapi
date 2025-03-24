from typing import Optional, Sequence

from fastapi import HTTPException, WebSocket
from sqlalchemy.exc import IntegrityError
from starlette import status

from core.security.utils import verify_password, hash_password
from core.security.token import create_jwt_token
from dependecies.repository import UserRepositoryDependency
from models.user import User
from repositories.user import UserRepository
from schemas.token import TokenSchema
from schemas.user.forms import UserPutSchema, UserLoginSchema
from services.base import BaseService


class UserService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def get_users(self) -> Sequence[User]:
        return await self.user_repository.list()

    async def get_user_or_none(
            self,
            *,
            db_id: int = None,
            username: str = None,
    ) -> Optional[User]:
        if db_id and (user := await self.user_repository.get(db_id)):
            return user
        if username and (user := await self.user_repository.get_by_username(username)):
            return user
        return None

    async def put_user(
            self,
            put_schema: UserPutSchema,
            *,
            db_id: int = None,
            username: str = None,
    ) -> User:
        put_schema.password = hash_password(put_schema.password)

        if not (obj := await self.get_user_or_none(db_id=db_id, username=username)):
            return await self.user_repository.create(
                put_schema.model_dump(
                    exclude_unset=True,
                ),
            )
        return await self.user_repository.update(
            obj,
            put_schema.model_dump(exclude_unset=True),
        )

    async def register(self, user_data: UserPutSchema) -> str:
        try:
            user = await self.put_user(user_data)
            return self._create_jwt_token(user.id)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Пользователь с таким логином уже существует!",
            )

    async def login(self, user_data: UserLoginSchema) -> str:
        user = await self.user_repository.get_by_username(user_data.username)

        if not user or not verify_password(user_data.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Неверный логин или пароль!"
            )

        return self._create_jwt_token(user.id)

    @staticmethod
    def _create_jwt_token(user_id: int) -> str:
        token_payload = TokenSchema(user_id=user_id).model_dump(mode="json")
        return create_jwt_token(token_payload)

    @classmethod
    def get_service(cls, user_repository: UserRepositoryDependency):
        return cls(user_repository)
