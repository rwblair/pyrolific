from enum import Enum


class AITaskBuilderMultipleChoiceInstructionType(str, Enum):
    MULTIPLE_CHOICE = "multiple_choice"

    def __str__(self) -> str:
        return str(self.value)
