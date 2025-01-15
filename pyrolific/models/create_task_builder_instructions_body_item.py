from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_task_builder_instructions_body_item_instructions_item import (
        CreateTaskBuilderInstructionsBodyItemInstructionsItem,
    )


T = TypeVar("T", bound="CreateTaskBuilderInstructionsBodyItem")


@_attrs_define
class CreateTaskBuilderInstructionsBodyItem:
    """
    Attributes:
        instructions (Union[Unset, list['CreateTaskBuilderInstructionsBodyItemInstructionsItem']]): The instructions to
            create for the AI Task Builder batch.
    """

    instructions: Union[Unset, list["CreateTaskBuilderInstructionsBodyItemInstructionsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instructions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.instructions, Unset):
            instructions = []
            for instructions_item_data in self.instructions:
                instructions_item = instructions_item_data.to_dict()
                instructions.append(instructions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instructions is not UNSET:
            field_dict["instructions"] = instructions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_task_builder_instructions_body_item_instructions_item import (
            CreateTaskBuilderInstructionsBodyItemInstructionsItem,
        )

        d = src_dict.copy()
        instructions = []
        _instructions = d.pop("instructions", UNSET)
        for instructions_item_data in _instructions or []:
            instructions_item = CreateTaskBuilderInstructionsBodyItemInstructionsItem.from_dict(instructions_item_data)

            instructions.append(instructions_item)

        create_task_builder_instructions_body_item = cls(
            instructions=instructions,
        )

        create_task_builder_instructions_body_item.additional_properties = d
        return create_task_builder_instructions_body_item

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
