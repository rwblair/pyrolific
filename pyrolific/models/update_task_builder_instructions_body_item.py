from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_task_builder_instructions_body_item_type import UpdateTaskBuilderInstructionsBodyItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_task_builder_instructions_body_item_options_item import (
        UpdateTaskBuilderInstructionsBodyItemOptionsItem,
    )


T = TypeVar("T", bound="UpdateTaskBuilderInstructionsBodyItem")


@_attrs_define
class UpdateTaskBuilderInstructionsBodyItem:
    """
    Attributes:
        type_ (UpdateTaskBuilderInstructionsBodyItemType): The type of instruction.
        created_by (str): The user who created the instruction.
        description (str): The instruction text.
        options (Union[Unset, list['UpdateTaskBuilderInstructionsBodyItemOptionsItem']]): Required for multiple_choice
            type. The options for the instruction.
    """

    type_: UpdateTaskBuilderInstructionsBodyItemType
    created_by: str
    description: str
    options: Union[Unset, list["UpdateTaskBuilderInstructionsBodyItemOptionsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        created_by = self.created_by

        description = self.description

        options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "created_by": created_by,
                "description": description,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.update_task_builder_instructions_body_item_options_item import (
            UpdateTaskBuilderInstructionsBodyItemOptionsItem,
        )

        d = src_dict.copy()
        type_ = UpdateTaskBuilderInstructionsBodyItemType(d.pop("type"))

        created_by = d.pop("created_by")

        description = d.pop("description")

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = UpdateTaskBuilderInstructionsBodyItemOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        update_task_builder_instructions_body_item = cls(
            type_=type_,
            created_by=created_by,
            description=description,
            options=options,
        )

        update_task_builder_instructions_body_item.additional_properties = d
        return update_task_builder_instructions_body_item

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
