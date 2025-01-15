from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.question_type import QuestionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.answer_option import AnswerOption


T = TypeVar("T", bound="Question")


@_attrs_define
class Question:
    """Responsible for defining a question within a survey.

    Attributes:
        answers (list['AnswerOption']): An array of answer options for a question.
        title (str): The question title. Example: What is your favourite root vegetable?.
        type_ (QuestionType): Responsible for articulating the question type. At the moment we have:

            - single answer
            - multiple answer

            Args:
                str (_type_): The type of question.
                Enum (_type_): The class to define an enum.
        id (Union[Unset, UUID]):
    """

    answers: list["AnswerOption"]
    title: str
    type_: QuestionType
    id: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        answers = []
        for answers_item_data in self.answers:
            answers_item = answers_item_data.to_dict()
            answers.append(answers_item)

        title = self.title

        type_ = self.type_.value

        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "answers": answers,
                "title": title,
                "type": type_,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.answer_option import AnswerOption

        d = src_dict.copy()
        answers = []
        _answers = d.pop("answers")
        for answers_item_data in _answers:
            answers_item = AnswerOption.from_dict(answers_item_data)

            answers.append(answers_item)

        title = d.pop("title")

        type_ = QuestionType(d.pop("type"))

        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        question = cls(
            answers=answers,
            title=title,
            type_=type_,
            id=id,
        )

        question.additional_properties = d
        return question

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
