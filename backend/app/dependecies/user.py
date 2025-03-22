from typing import Annotated
from fastapi import Depends
from services.user import UserService

UserServiceDependency = Annotated[
    UserService,
    Depends(UserService.get_service),
]
