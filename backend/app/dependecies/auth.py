from typing import Annotated

from fastapi import Depends

from core.security.auth import get_current_user
from models.user import User
from typing import TypeVar, Generic, Type

T = TypeVar("T")

CurrentUserDependency = Annotated[User, Depends(get_current_user)]
