from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AITaskBuilderDatapointReference")


@_attrs_define
class AITaskBuilderDatapointReference:
    """
    Attributes:
        dataset_id (UUID):
        etag (str):
        filename (str):
        asset_url (str):
    """

    dataset_id: UUID
    etag: str
    filename: str
    asset_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = str(self.dataset_id)

        etag = self.etag

        filename = self.filename

        asset_url = self.asset_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataset_id": dataset_id,
                "etag": etag,
                "filename": filename,
                "asset_url": asset_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        dataset_id = UUID(d.pop("dataset_id"))

        etag = d.pop("etag")

        filename = d.pop("filename")

        asset_url = d.pop("asset_url")

        ai_task_builder_datapoint_reference = cls(
            dataset_id=dataset_id,
            etag=etag,
            filename=filename,
            asset_url=asset_url,
        )

        ai_task_builder_datapoint_reference.additional_properties = d
        return ai_task_builder_datapoint_reference

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
