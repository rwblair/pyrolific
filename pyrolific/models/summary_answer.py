from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SummaryAnswer")


@_attrs_define
class SummaryAnswer:
    """Responsible for housing the aggregation for a specific answer.

    Attributes:
        answer (str): The answer selected.
        answer_id (Union[Unset, UUID]): The answer ID.
        count (Union[Unset, int]): The count of how many times this answer was used in a response. Default: 0.
    """

    answer: str
    answer_id: Union[Unset, UUID] = UNSET
    count: Union[Unset, int] = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        answer = self.answer

        answer_id: Union[Unset, str] = UNSET
        if not isinstance(self.answer_id, Unset):
            answer_id = str(self.answer_id)

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "answer": answer,
            }
        )
        if answer_id is not UNSET:
            field_dict["answer_id"] = answer_id
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        answer = d.pop("answer")

        _answer_id = d.pop("answer_id", UNSET)
        answer_id: Union[Unset, UUID]
        if isinstance(_answer_id, Unset):
            answer_id = UNSET
        else:
            answer_id = UUID(_answer_id)

        count = d.pop("count", UNSET)

        summary_answer = cls(
            answer=answer,
            answer_id=answer_id,
            count=count,
        )

        summary_answer.additional_properties = d
        return summary_answer

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
