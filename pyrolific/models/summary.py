from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.summary_question import SummaryQuestion


T = TypeVar("T", bound="Summary")


@_attrs_define
class Summary:
    """Responsible for providing a base for all the aggregated answers for a survey.

    Example:
        {'survey_id': '63346b3a4fd1fe7b39f192e9', 'questions': [{'question_id': '02dee012-25e4-449e-8f2f-a552b9007d92',
            'question': 'Do you feel that this will all be alright on the night?', 'total_answers': 10, 'answers':
            [{'answer_id': '4c69011b-9b6b-46c6-8ba2-da80761131dc', 'answer': 'Yes', 'count': 4}, {'answer_id':
            'f3c8d38f-842c-49d9-a0bb-e17b7803b240', 'answer': 'No', 'count': 6}]}]}

    Attributes:
        survey_id (str): The survey ID.
        questions (Union[Unset, list['SummaryQuestion']]): A list of questions for the given survey.
    """

    survey_id: str
    questions: Union[Unset, list["SummaryQuestion"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        survey_id = self.survey_id

        questions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.questions, Unset):
            questions = []
            for questions_item_data in self.questions:
                questions_item = questions_item_data.to_dict()
                questions.append(questions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "survey_id": survey_id,
            }
        )
        if questions is not UNSET:
            field_dict["questions"] = questions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.summary_question import SummaryQuestion

        d = src_dict.copy()
        survey_id = d.pop("survey_id")

        questions = []
        _questions = d.pop("questions", UNSET)
        for questions_item_data in _questions or []:
            questions_item = SummaryQuestion.from_dict(questions_item_data)

            questions.append(questions_item)

        summary = cls(
            survey_id=survey_id,
            questions=questions,
        )

        summary.additional_properties = d
        return summary

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
