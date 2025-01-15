from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTaskBuilderInstructionsBodyItemInstructionsItemOptionsItem")


@_attrs_define
class CreateTaskBuilderInstructionsBodyItemInstructionsItemOptionsItem:
    """
    Attributes:
        label (Union[Unset, str]): The display label for the option.
        value (Union[Unset, str]): The value associated with the option.
    """

    label: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label", UNSET)

        value = d.pop("value", UNSET)

        create_task_builder_instructions_body_item_instructions_item_options_item = cls(
            label=label,
            value=value,
        )

        create_task_builder_instructions_body_item_instructions_item_options_item.additional_properties = d
        return create_task_builder_instructions_body_item_instructions_item_options_item

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
