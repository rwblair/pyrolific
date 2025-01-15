from enum import Enum


class AITaskBuilderBatchStatus(str, Enum):
    ERROR = "ERROR"
    PROCESSING = "PROCESSING"
    READY = "READY"
    UNINITIALISED = "UNINITIALISED"

    def __str__(self) -> str:
        return str(self.value)
