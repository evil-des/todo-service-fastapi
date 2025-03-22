from typing import Optional
from pydantic import BaseModel
from schemas.user.base import UserBaseSchema


class UserLoginSchema(UserBaseSchema):
    password: str


class UserPutSchema(UserBaseSchema):
    password: str


class UserPatchSchema(BaseModel):
    username: Optional[str]
    password: Optional[str]
