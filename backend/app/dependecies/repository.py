from typing import Annotated
from fastapi import Depends

from repositories.task import TaskRepository
from repositories.user import UserRepository

UserRepositoryDependency = Annotated[
    UserRepository,
    Depends(UserRepository.get_repository),
]
TaskRepositoryDependency = Annotated[
    TaskRepository,
    Depends(TaskRepository.get_repository),
]
