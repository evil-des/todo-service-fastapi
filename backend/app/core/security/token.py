from datetime import datetime, UTC
from typing import TypeVar, Type

from fastapi import HTTPException
from jose import jwt, JWTError
from loguru import logger
from pydantic import ValidationError
from starlette import status

from core.config import core_settings
from dependecies.security import HeaderTokenSec
from schemas.token import TokenSchema

T = TypeVar("T", bound=TokenSchema)


def create_jwt_token(data: dict) -> str:
    return jwt.encode(
        data,
        core_settings.JWT_KEY.get_secret_value(),
        algorithm="HS256",
    )


def parse_jwt_token(token: str, schema: Type[T]) -> T:
    data = jwt.decode(
        token,
        core_settings.JWT_KEY.get_secret_value(),
        algorithms=['HS256'],
    )
    return schema.model_validate(data)


def _get_token(jwt_token: HeaderTokenSec, schema: Type[T]) -> T:
    if not jwt_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        token = parse_jwt_token(jwt_token, schema)
        if token.expires_in <= datetime.now(UTC):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return token
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    except ValidationError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


def get_user_token(jwt_token: HeaderTokenSec) -> TokenSchema:
    return _get_token(jwt_token, TokenSchema)
