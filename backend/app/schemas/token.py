from datetime import datetime, UTC
from pydantic import BaseModel, Field, field_serializer
from core.security.globals import TOKEN_EXPIRE_IN


class TokenSchema(BaseModel):
    user_id: int
    expires_in: datetime = Field(
        default_factory=lambda: datetime.now(UTC) + TOKEN_EXPIRE_IN,
    )

    @field_serializer("expires_in")
    def serialize_expires_in(self, expires_in: datetime):
        return int(expires_in.timestamp())
