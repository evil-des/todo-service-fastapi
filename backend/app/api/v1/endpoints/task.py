from typing import Annotated, Optional

from fastapi import APIRouter, Body, Query, Path
from dependecies.auth import CurrentUserDependency
from dependecies.task import TaskServiceDependency
from schemas.task.response import TaskSchema
from schemas.task.forms import TaskPatchSchema, TaskPutSchema

router = APIRouter(prefix="/task", tags=["task"])


@router.put("/")
async def create_task(
        put_schema: Annotated[TaskPutSchema, Body(...)],
        user: CurrentUserDependency,
        task_service: TaskServiceDependency,
) -> TaskSchema:
    return await task_service.create_task(user.id, put_schema)


@router.get("/")
async def get_tasks(
        user: CurrentUserDependency,
        task_service: TaskServiceDependency,
) -> list[TaskSchema]:
    return await task_service.get_tasks(user.id)


@router.patch("/{task_id}")
async def patch_task(
        task_id: Annotated[int, Path(...)],
        patch_schema: Annotated[TaskPatchSchema, Body(...)],
        user: CurrentUserDependency,
        task_service: TaskServiceDependency,
) -> TaskSchema:
    return await task_service.patch_task(user.id, task_id, patch_schema)


@router.delete("/{task_id}")
async def delete_task(
        task_id: Annotated[int, Path(...)],
        user: CurrentUserDependency,
        task_service: TaskServiceDependency,
) -> TaskSchema:
    return await task_service.delete_task(user.id, task_id)
