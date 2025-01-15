import datetime
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ai_task_builder_dataset_status import AITaskBuilderDatasetStatus

T = TypeVar("T", bound="AITaskBuilderDataset")


@_attrs_define
class AITaskBuilderDataset:
    """
    Attributes:
        id (UUID):
        name (str):  Example: Text Dataset.
        created_at (datetime.datetime):
        created_by (str):  Example: 65786062db3b35bcbeb07bcc.
        status (AITaskBuilderDatasetStatus):  Default: AITaskBuilderDatasetStatus.UNINITIALISED.
        total_datapoint_count (int):
        workspace_id (str):  Example: 6278acb09062db3b35bcbeb0.
    """

    id: UUID
    name: str
    created_at: datetime.datetime
    created_by: str
    total_datapoint_count: int
    workspace_id: str
    status: AITaskBuilderDatasetStatus = AITaskBuilderDatasetStatus.UNINITIALISED
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        status = self.status.value

        total_datapoint_count = self.total_datapoint_count

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created_at": created_at,
                "created_by": created_by,
                "status": status,
                "total_datapoint_count": total_datapoint_count,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = UUID(d.pop("id"))

        name = d.pop("name")

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        status = AITaskBuilderDatasetStatus(d.pop("status"))

        total_datapoint_count = d.pop("total_datapoint_count")

        workspace_id = d.pop("workspace_id")

        ai_task_builder_dataset = cls(
            id=id,
            name=name,
            created_at=created_at,
            created_by=created_by,
            status=status,
            total_datapoint_count=total_datapoint_count,
            workspace_id=workspace_id,
        )

        ai_task_builder_dataset.additional_properties = d
        return ai_task_builder_dataset

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
