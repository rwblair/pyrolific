import datetime
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ai_task_builder_datapoint_modality import AITaskBuilderDatapointModality

if TYPE_CHECKING:
    from ..models.ai_task_builder_datapoint_reference import AITaskBuilderDatapointReference


T = TypeVar("T", bound="AITaskBuilderDatapoint")


@_attrs_define
class AITaskBuilderDatapoint:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        modality (AITaskBuilderDatapointModality):
        reference (AITaskBuilderDatapointReference):
    """

    id: UUID
    created_at: datetime.datetime
    modality: AITaskBuilderDatapointModality
    reference: "AITaskBuilderDatapointReference"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        modality = self.modality.value

        reference = self.reference.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "modality": modality,
                "reference": reference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.ai_task_builder_datapoint_reference import AITaskBuilderDatapointReference

        d = src_dict.copy()
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        modality = AITaskBuilderDatapointModality(d.pop("modality"))

        reference = AITaskBuilderDatapointReference.from_dict(d.pop("reference"))

        ai_task_builder_datapoint = cls(
            id=id,
            created_at=created_at,
            modality=modality,
            reference=reference,
        )

        ai_task_builder_datapoint.additional_properties = d
        return ai_task_builder_datapoint

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
