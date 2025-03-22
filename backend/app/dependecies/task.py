from typing import Annotated
from fastapi import Depends
from services.task import TaskService

TaskServiceDependency = Annotated[
    TaskService,
    Depends(TaskService.get_service),
]
