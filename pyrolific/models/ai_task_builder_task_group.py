import datetime
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AITaskBuilderTaskGroup")


@_attrs_define
class AITaskBuilderTaskGroup:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        batch_id (str):
        created_by (str):
        task_ids (list[str]):
    """

    id: UUID
    created_at: datetime.datetime
    batch_id: str
    created_by: str
    task_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        batch_id = self.batch_id

        created_by = self.created_by

        task_ids = self.task_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "batch_id": batch_id,
                "created_by": created_by,
                "task_ids": task_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        batch_id = d.pop("batch_id")

        created_by = d.pop("created_by")

        task_ids = cast(list[str], d.pop("task_ids"))

        ai_task_builder_task_group = cls(
            id=id,
            created_at=created_at,
            batch_id=batch_id,
            created_by=created_by,
            task_ids=task_ids,
        )

        ai_task_builder_task_group.additional_properties = d
        return ai_task_builder_task_group

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
