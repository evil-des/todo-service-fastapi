from schemas.base import ResponseModel
from schemas.user.forms import UserBaseSchema


class UserSchema(ResponseModel, UserBaseSchema):
    id: int
