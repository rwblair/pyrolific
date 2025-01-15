from enum import Enum


class GetTaskBuilderBatchStatusResponse200Status(str, Enum):
    ERROR = "ERROR"
    PROCESSING = "PROCESSING"
    READY = "READY"
    UNINITIALISED = "UNINITIALISED"

    def __str__(self) -> str:
        return str(self.value)
