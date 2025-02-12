from enum import Enum


class StudyPredictedRecruitmentTimeRequestStudyType(str, Enum):
    REP_SAMPLE_GLOBAL_REP_SAMPLE = "REP_SAMPLE_GLOBAL_REP_SAMPLE"
    REP_SAMPLE_UK_ENGLISH_AGE_POLITICAL_AFFILIATION = "REP_SAMPLE_UK_ENGLISH_AGE_POLITICAL_AFFILIATION"
    REP_SAMPLE_UK_ENGLISH_AGE_POLITICAL_AFFILIATION_ETHNICITY = (
        "REP_SAMPLE_UK_ENGLISH_AGE_POLITICAL_AFFILIATION_ETHNICITY"
    )
    REP_SAMPLE_US_ENGLISH_AGE_POLITICAL_AFFILIATION = "REP_SAMPLE_US_ENGLISH_AGE_POLITICAL_AFFILIATION"
    REP_SAMPLE_US_ENGLISH_AGE_POLITICAL_AFFILIATION_ETHNICITY = (
        "REP_SAMPLE_US_ENGLISH_AGE_POLITICAL_AFFILIATION_ETHNICITY"
    )
    SINGLE = "SINGLE"
    UK_REP_SAMPLE = "UK_REP_SAMPLE"
    US_REP_SAMPLE = "US_REP_SAMPLE"

    def __str__(self) -> str:
        return str(self.value)
