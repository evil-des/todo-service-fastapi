from datetime import datetime

from enums.task import TaskStatus
from schemas.base import ResponseModel
from schemas.task.base import TaskBaseSchema


class TaskSchema(ResponseModel, TaskBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    status: TaskStatus
