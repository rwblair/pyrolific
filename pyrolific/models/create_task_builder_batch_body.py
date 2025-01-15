from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTaskBuilderBatchBody")


@_attrs_define
class CreateTaskBuilderBatchBody:
    """
    Attributes:
        name (Union[Unset, str]):  Example: Data Collection Batch.
        workspace_id (Union[Unset, str]):  Example: 6278acb09062db3b35bcbeb0.
        dataset_id (Union[Unset, str]):  Example: 1234acb09999db4b99bcded1.
    """

    name: Union[Unset, str] = UNSET
    workspace_id: Union[Unset, str] = UNSET
    dataset_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        workspace_id = self.workspace_id

        dataset_id = self.dataset_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id
        if dataset_id is not UNSET:
            field_dict["dataset_id"] = dataset_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        workspace_id = d.pop("workspace_id", UNSET)

        dataset_id = d.pop("dataset_id", UNSET)

        create_task_builder_batch_body = cls(
            name=name,
            workspace_id=workspace_id,
            dataset_id=dataset_id,
        )

        create_task_builder_batch_body.additional_properties = d
        return create_task_builder_batch_body

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
