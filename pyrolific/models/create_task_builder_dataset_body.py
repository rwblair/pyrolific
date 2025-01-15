from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTaskBuilderDatasetBody")


@_attrs_define
class CreateTaskBuilderDatasetBody:
    """
    Attributes:
        name (Union[Unset, str]): The name or identifier of the AI Task Builder dataset. Example: Text Dataset.
        workspace_id (Union[Unset, str]): The ID of the Prolific workspace the dataset will be created in. Example:
            6278acb09062db3b35bcbeb0.
    """

    name: Union[Unset, str] = UNSET
    workspace_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        workspace_id = d.pop("workspace_id", UNSET)

        create_task_builder_dataset_body = cls(
            name=name,
            workspace_id=workspace_id,
        )

        create_task_builder_dataset_body.additional_properties = d
        return create_task_builder_dataset_body

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
