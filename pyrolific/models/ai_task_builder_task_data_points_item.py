from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_task_builder_task_data_points_item_modality import AITaskBuilderTaskDataPointsItemModality

if TYPE_CHECKING:
    from ..models.ai_task_builder_task_data_points_item_reference import AITaskBuilderTaskDataPointsItemReference


T = TypeVar("T", bound="AITaskBuilderTaskDataPointsItem")


@_attrs_define
class AITaskBuilderTaskDataPointsItem:
    """
    Attributes:
        id (UUID):
        reference (AITaskBuilderTaskDataPointsItemReference):
        modality (AITaskBuilderTaskDataPointsItemModality):
    """

    id: UUID
    reference: "AITaskBuilderTaskDataPointsItemReference"
    modality: AITaskBuilderTaskDataPointsItemModality
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        reference = self.reference.to_dict()

        modality = self.modality.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "reference": reference,
                "modality": modality,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.ai_task_builder_task_data_points_item_reference import AITaskBuilderTaskDataPointsItemReference

        d = src_dict.copy()
        id = UUID(d.pop("id"))

        reference = AITaskBuilderTaskDataPointsItemReference.from_dict(d.pop("reference"))

        modality = AITaskBuilderTaskDataPointsItemModality(d.pop("modality"))

        ai_task_builder_task_data_points_item = cls(
            id=id,
            reference=reference,
            modality=modality,
        )

        ai_task_builder_task_data_points_item.additional_properties = d
        return ai_task_builder_task_data_points_item

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
