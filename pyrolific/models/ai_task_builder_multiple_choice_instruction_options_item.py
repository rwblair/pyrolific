from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AITaskBuilderMultipleChoiceInstructionOptionsItem")


@_attrs_define
class AITaskBuilderMultipleChoiceInstructionOptionsItem:
    """
    Attributes:
        label (str):
        value (Union[bool, float, str]):
    """

    label: str
    value: Union[bool, float, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        value: Union[bool, float, str]
        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        def _parse_value(data: object) -> Union[bool, float, str]:
            return cast(Union[bool, float, str], data)

        value = _parse_value(d.pop("value"))

        ai_task_builder_multiple_choice_instruction_options_item = cls(
            label=label,
            value=value,
        )

        ai_task_builder_multiple_choice_instruction_options_item.additional_properties = d
        return ai_task_builder_multiple_choice_instruction_options_item

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
