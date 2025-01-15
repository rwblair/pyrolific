from enum import Enum


class GetTaskBuilderDatasetStatusResponse200Status(str, Enum):
    ERROR = "ERROR"
    PROCESSING = "PROCESSING"
    READY = "READY"
    UNINITIALISED = "UNINITIALISED"

    def __str__(self) -> str:
        return str(self.value)
