import datetime
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.ai_task_builder_task_response_response import AITaskBuilderTaskResponseResponse


T = TypeVar("T", bound="AITaskBuilderTaskResponse")


@_attrs_define
class AITaskBuilderTaskResponse:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        batch_id (str):
        participant_id (str):
        response (AITaskBuilderTaskResponseResponse):
        task_id (str):
    """

    id: UUID
    created_at: datetime.datetime
    batch_id: str
    participant_id: str
    response: "AITaskBuilderTaskResponseResponse"
    task_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        batch_id = self.batch_id

        participant_id = self.participant_id

        response = self.response.to_dict()

        task_id = self.task_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "batch_id": batch_id,
                "participant_id": participant_id,
                "response": response,
                "task_id": task_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.ai_task_builder_task_response_response import AITaskBuilderTaskResponseResponse

        d = src_dict.copy()
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        batch_id = d.pop("batch_id")

        participant_id = d.pop("participant_id")

        response = AITaskBuilderTaskResponseResponse.from_dict(d.pop("response"))

        task_id = d.pop("task_id")

        ai_task_builder_task_response = cls(
            id=id,
            created_at=created_at,
            batch_id=batch_id,
            participant_id=participant_id,
            response=response,
            task_id=task_id,
        )

        ai_task_builder_task_response.additional_properties = d
        return ai_task_builder_task_response

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
