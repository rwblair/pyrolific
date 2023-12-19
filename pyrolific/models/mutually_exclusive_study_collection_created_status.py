from enum import Enum


class MutuallyExclusiveStudyCollectionCreatedStatus(str, Enum):
    ACTIVE = "ACTIVE"
    AWAITING_REVIEW = "AWAITING_REVIEW"
    PAUSED = "PAUSED"
    PUBLISHING = "PUBLISHING"
    SCHEDULED = "SCHEDULED"
    UNPUBLISHED = "UNPUBLISHED"

    def __str__(self) -> str:
        return str(self.value)
