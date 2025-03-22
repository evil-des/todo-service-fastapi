from typing import Optional
from pydantic import BaseModel

from enums.task import TaskStatus
from schemas.base import FormModel
from schemas.task.base import TaskBaseSchema


class TaskPutSchema(FormModel, TaskBaseSchema):
    pass


class TaskPatchSchema(FormModel, BaseModel):
    name: Optional[str]
    description: Optional[str]
    status: Optional[TaskStatus]
