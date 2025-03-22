from enum import auto
from enums.base import SameCaseStrEnum


class TaskStatus(SameCaseStrEnum):
    COMPLETED = auto()
    NOT_COMPLETED = auto()
