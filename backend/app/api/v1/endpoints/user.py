from fastapi import APIRouter, Body, Path, Query
from dependecies.auth import CurrentUserDependency
from dependecies.user import UserServiceDependency
from schemas.user.forms import UserLoginSchema, UserPutSchema
from schemas.user.response import UserSchema

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/me")
async def user_me(user: CurrentUserDependency) -> UserSchema:
    return UserSchema.model_validate(user, from_attributes=True)


@router.post("/login")
async def auth_user(
        user_service: UserServiceDependency,
        user_data: UserLoginSchema,
) -> str:
    return await user_service.login(user_data)


@router.post("/register")
async def register_user(
        user_service: UserServiceDependency,
        user_data: UserPutSchema,
) -> str:
    return await user_service.register(user_data)
