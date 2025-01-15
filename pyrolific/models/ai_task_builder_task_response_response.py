from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AITaskBuilderTaskResponseResponse")


@_attrs_define
class AITaskBuilderTaskResponseResponse:
    """
    Attributes:
        instruction_id (str):
        type_ (str):
        answer (str):
    """

    instruction_id: str
    type_: str
    answer: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instruction_id = self.instruction_id

        type_ = self.type_

        answer = self.answer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instruction_id": instruction_id,
                "type": type_,
                "answer": answer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        instruction_id = d.pop("instruction_id")

        type_ = d.pop("type")

        answer = d.pop("answer")

        ai_task_builder_task_response_response = cls(
            instruction_id=instruction_id,
            type_=type_,
            answer=answer,
        )

        ai_task_builder_task_response_response.additional_properties = d
        return ai_task_builder_task_response_response

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
