from enum import Enum


class StudyPredictedRecruitmentTimeRequestDeviceCompatibilityItem(str, Enum):
    DESKTOP = "desktop"
    MOBILE = "mobile"
    TABLET = "tablet"

    def __str__(self) -> str:
        return str(self.value)
