from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_task_builder_instructions_body_item_instructions_item_type import (
    CreateTaskBuilderInstructionsBodyItemInstructionsItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_task_builder_instructions_body_item_instructions_item_options_item import (
        CreateTaskBuilderInstructionsBodyItemInstructionsItemOptionsItem,
    )


T = TypeVar("T", bound="CreateTaskBuilderInstructionsBodyItemInstructionsItem")


@_attrs_define
class CreateTaskBuilderInstructionsBodyItemInstructionsItem:
    """
    Attributes:
        type_ (Union[Unset, CreateTaskBuilderInstructionsBodyItemInstructionsItemType]): The type of instruction
            (multiple choice or free text).
        created_by (Union[Unset, str]): The creator of the instruction.
        description (Union[Unset, str]): The description or question for the instruction.
        options (Union[Unset, list['CreateTaskBuilderInstructionsBodyItemInstructionsItemOptionsItem']]): The options
            for multiple choice instructions (required if type is multiple_choice).
    """

    type_: Union[Unset, CreateTaskBuilderInstructionsBodyItemInstructionsItemType] = UNSET
    created_by: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    options: Union[Unset, list["CreateTaskBuilderInstructionsBodyItemInstructionsItemOptionsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
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
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_task_builder_instructions_body_item_instructions_item_options_item import (
            CreateTaskBuilderInstructionsBodyItemInstructionsItemOptionsItem,
        )

        d = src_dict.copy()
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CreateTaskBuilderInstructionsBodyItemInstructionsItemType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CreateTaskBuilderInstructionsBodyItemInstructionsItemType(_type_)

        created_by = d.pop("created_by", UNSET)

        description = d.pop("description", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = CreateTaskBuilderInstructionsBodyItemInstructionsItemOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        create_task_builder_instructions_body_item_instructions_item = cls(
            type_=type_,
            created_by=created_by,
            description=description,
            options=options,
        )

        create_task_builder_instructions_body_item_instructions_item.additional_properties = d
        return create_task_builder_instructions_body_item_instructions_item

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
