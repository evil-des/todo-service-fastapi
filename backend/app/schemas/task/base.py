from typing import Optional
from pydantic import BaseModel


class TaskBaseSchema(BaseModel):
    name: str
    description: str
