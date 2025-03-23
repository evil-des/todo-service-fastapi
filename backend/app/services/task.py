from typing import Optional, Sequence

from fastapi import HTTPException, WebSocket
from pydantic import TypeAdapter
from starlette import status

from core.security.token import create_jwt_token
from dependecies.repository import TaskRepositoryDependency
from models.task import Task
from repositories.task import TaskRepository
from schemas.task.forms import TaskPatchSchema, TaskPutSchema
from schemas.task.response import TaskSchema
from schemas.token import TokenSchema
from services.base import BaseService


class TaskService(BaseService):
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    async def get_task_or_none(
            self,
            *,
            db_id: int = None,
    ) -> Optional[Task]:
        if db_id and (task := await self.task_repository.get(db_id)):
            return task
        return None

    async def get_tasks(self, user_id: int) -> list[TaskSchema]:
        return TypeAdapter(list[TaskSchema]).validate_python(
            await self.task_repository.list(
                filters=[Task.user_id == user_id],
            ),
            from_attributes=True,
        )

    async def create_task(self, user_id: int, put_schema: TaskPutSchema) -> TaskSchema:
        data = put_schema.model_dump()
        data.update({"user_id": user_id})

        return TaskSchema.model_validate(
            await self.task_repository.create(data),
            from_attributes=True,
        )

    async def patch_task(
            self,
            user_id: int,
            task_id: int,
            patch_schema: TaskPatchSchema,
    ) -> TaskSchema:
        if task := await self.get_task_or_none(db_id=task_id):
            if task.user_id != user_id:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

            return TaskSchema.model_validate(
                await self.task_repository.update(
                    task,
                    patch_schema.model_dump(exclude_unset=True),
                ),
                from_attributes=True,
            )
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    async def delete_task(
            self,
            user_id: int,
            task_id: int,
    ) -> None:
        if task := await self.get_task_or_none(db_id=task_id):
            if task.user_id != user_id:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

            return await self.task_repository.delete(task_id)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def _create_jwt_token(user_id: int) -> str:
        token_payload = TokenSchema(user_id=user_id).model_dump(mode="json")
        return create_jwt_token(token_payload)

    @classmethod
    def get_service(cls, task_repository: TaskRepositoryDependency):
        return cls(task_repository)
