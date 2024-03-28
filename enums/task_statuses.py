from enum import StrEnum, auto

class TaskStatus(StrEnum):
    """An enum of the possible statuses of a task."""
    GENERATING = auto()
    SUCCESS = auto()