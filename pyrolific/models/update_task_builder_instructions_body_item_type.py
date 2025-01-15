from enum import Enum


class UpdateTaskBuilderInstructionsBodyItemType(str, Enum):
    FREE_TEXT = "free_text"
    MULTIPLE_CHOICE = "multiple_choice"

    def __str__(self) -> str:
        return str(self.value)
