from typing import Optional

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    username: str
