import datetime
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ai_task_builder_batch_status import AITaskBuilderBatchStatus

T = TypeVar("T", bound="AITaskBuilderBatch")


@_attrs_define
class AITaskBuilderBatch:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime): An ISO-8601 formatted string reprenting the batch creation time, in UTC.
        created_by (str): User ID of the Prolific user that created the resource. Example: 6278cb09062dbb35bc4abebc.
        name (str):  Example: Data Collection Batch.
        status (AITaskBuilderBatchStatus):
        total_task_count (int):
        workspace_id (str):  Example: 6278acb09062db3b35bcbeb0.
    """

    id: UUID
    created_at: datetime.datetime
    created_by: str
    name: str
    status: AITaskBuilderBatchStatus
    total_task_count: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        name = self.name

        status = self.status.value

        total_task_count = self.total_task_count

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "created_by": created_by,
                "name": name,
                "status": status,
                "total_task_count": total_task_count,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        name = d.pop("name")

        status = AITaskBuilderBatchStatus(d.pop("status"))

        total_task_count = d.pop("total_task_count")

        workspace_id = d.pop("workspace_id")

        ai_task_builder_batch = cls(
            id=id,
            created_at=created_at,
            created_by=created_by,
            name=name,
            status=status,
            total_task_count=total_task_count,
            workspace_id=workspace_id,
        )

        ai_task_builder_batch.additional_properties = d
        return ai_task_builder_batch

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
