from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.response_answer import ResponseAnswer


T = TypeVar("T", bound="QuestionResponse")


@_attrs_define
class QuestionResponse:
    """Responsible for defining an answer to a survey question

    Attributes:
        answers (list['ResponseAnswer']): The answers selected.
        question_id (UUID): The question ID.
        question_title (str): The title of the survey question.
    """

    answers: list["ResponseAnswer"]
    question_id: UUID
    question_title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        answers = []
        for answers_item_data in self.answers:
            answers_item = answers_item_data.to_dict()
            answers.append(answers_item)

        question_id = str(self.question_id)

        question_title = self.question_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "answers": answers,
                "question_id": question_id,
                "question_title": question_title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.response_answer import ResponseAnswer

        d = src_dict.copy()
        answers = []
        _answers = d.pop("answers")
        for answers_item_data in _answers:
            answers_item = ResponseAnswer.from_dict(answers_item_data)

            answers.append(answers_item)

        question_id = UUID(d.pop("question_id"))

        question_title = d.pop("question_title")

        question_response = cls(
            answers=answers,
            question_id=question_id,
            question_title=question_title,
        )

        question_response.additional_properties = d
        return question_response

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
