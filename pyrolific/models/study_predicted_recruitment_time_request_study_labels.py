from enum import Enum


class StudyPredictedRecruitmentTimeRequestStudyLabels(str, Enum):
    ANNOTATION = "annotation"
    INTERVIEW = "interview"
    OTHER = "other"
    SURVEY = "survey"
    WRITING_TASK = "writing_task"

    def __str__(self) -> str:
        return str(self.value)
