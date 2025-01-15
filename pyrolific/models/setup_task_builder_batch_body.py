from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetupTaskBuilderBatchBody")


@_attrs_define
class SetupTaskBuilderBatchBody:
    """
    Attributes:
        dataset_id (Union[Unset, UUID]): The ID of the dataset being configured into tasks as part of the setup process.
        tasks_per_group (Union[Unset, float]): The number of tasks to be presented to each annotator that provides a
            response. Default: 1.0. Example: 3.
    """

    dataset_id: Union[Unset, UUID] = UNSET
    tasks_per_group: Union[Unset, float] = 1.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id: Union[Unset, str] = UNSET
        if not isinstance(self.dataset_id, Unset):
            dataset_id = str(self.dataset_id)

        tasks_per_group = self.tasks_per_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dataset_id is not UNSET:
            field_dict["dataset_id"] = dataset_id
        if tasks_per_group is not UNSET:
            field_dict["tasks_per_group"] = tasks_per_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _dataset_id = d.pop("dataset_id", UNSET)
        dataset_id: Union[Unset, UUID]
        if isinstance(_dataset_id, Unset):
            dataset_id = UNSET
        else:
            dataset_id = UUID(_dataset_id)

        tasks_per_group = d.pop("tasks_per_group", UNSET)

        setup_task_builder_batch_body = cls(
            dataset_id=dataset_id,
            tasks_per_group=tasks_per_group,
        )

        setup_task_builder_batch_body.additional_properties = d
        return setup_task_builder_batch_body

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
