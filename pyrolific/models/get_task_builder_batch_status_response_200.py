from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_task_builder_batch_status_response_200_status import GetTaskBuilderBatchStatusResponse200Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTaskBuilderBatchStatusResponse200")


@_attrs_define
class GetTaskBuilderBatchStatusResponse200:
    """
    Attributes:
        status (Union[Unset, GetTaskBuilderBatchStatusResponse200Status]): The status of the Batch - one of
            'UNINITIALISED', 'PROCESSING', 'READY', 'ERROR'
    """

    status: Union[Unset, GetTaskBuilderBatchStatusResponse200Status] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, GetTaskBuilderBatchStatusResponse200Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetTaskBuilderBatchStatusResponse200Status(_status)

        get_task_builder_batch_status_response_200 = cls(
            status=status,
        )

        get_task_builder_batch_status_response_200.additional_properties = d
        return get_task_builder_batch_status_response_200

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
