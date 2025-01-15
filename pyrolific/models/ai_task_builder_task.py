import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_task_builder_task_data_points_item import AITaskBuilderTaskDataPointsItem


T = TypeVar("T", bound="AITaskBuilderTask")


@_attrs_define
class AITaskBuilderTask:
    """
    Attributes:
        id (Union[Unset, UUID]):
        batch_id (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, str]):
        description (Union[Unset, str]):
        instruction_ids (Union[Unset, list[str]]):
        data_points (Union[Unset, list['AITaskBuilderTaskDataPointsItem']]):
    """

    id: Union[Unset, UUID] = UNSET
    batch_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    instruction_ids: Union[Unset, list[str]] = UNSET
    data_points: Union[Unset, list["AITaskBuilderTaskDataPointsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        batch_id = self.batch_id

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        description = self.description

        instruction_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.instruction_ids, Unset):
            instruction_ids = self.instruction_ids

        data_points: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_points, Unset):
            data_points = []
            for data_points_item_data in self.data_points:
                data_points_item = data_points_item_data.to_dict()
                data_points.append(data_points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if instruction_ids is not UNSET:
            field_dict["instruction_ids"] = instruction_ids
        if data_points is not UNSET:
            field_dict["data_points"] = data_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.ai_task_builder_task_data_points_item import AITaskBuilderTaskDataPointsItem

        d = src_dict.copy()
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        batch_id = d.pop("batch_id", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        created_by = d.pop("created_by", UNSET)

        description = d.pop("description", UNSET)

        instruction_ids = cast(list[str], d.pop("instruction_ids", UNSET))

        data_points = []
        _data_points = d.pop("data_points", UNSET)
        for data_points_item_data in _data_points or []:
            data_points_item = AITaskBuilderTaskDataPointsItem.from_dict(data_points_item_data)

            data_points.append(data_points_item)

        ai_task_builder_task = cls(
            id=id,
            batch_id=batch_id,
            created_at=created_at,
            created_by=created_by,
            description=description,
            instruction_ids=instruction_ids,
            data_points=data_points,
        )

        ai_task_builder_task.additional_properties = d
        return ai_task_builder_task

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
