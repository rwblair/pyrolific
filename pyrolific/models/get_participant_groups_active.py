from enum import Enum


class GetParticipantGroupsActive(str, Enum):
    FALSE = "false"
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
