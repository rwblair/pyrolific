import datetime
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ai_task_builder_free_text_input_instruction_type import AITaskBuilderFreeTextInputInstructionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AITaskBuilderFreeTextInputInstruction")


@_attrs_define
class AITaskBuilderFreeTextInputInstruction:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        type_ (AITaskBuilderFreeTextInputInstructionType):
        batch_id (str):
        created_by (str):
        description (str):
        placeholder_text_input (Union[Unset, str]):
    """

    id: UUID
    created_at: datetime.datetime
    type_: AITaskBuilderFreeTextInputInstructionType
    batch_id: str
    created_by: str
    description: str
    placeholder_text_input: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        type_ = self.type_.value

        batch_id = self.batch_id

        created_by = self.created_by

        description = self.description

        placeholder_text_input = self.placeholder_text_input

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "type": type_,
                "batch_id": batch_id,
                "created_by": created_by,
                "description": description,
            }
        )
        if placeholder_text_input is not UNSET:
            field_dict["placeholder_text_input"] = placeholder_text_input

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        type_ = AITaskBuilderFreeTextInputInstructionType(d.pop("type"))

        batch_id = d.pop("batch_id")

        created_by = d.pop("created_by")

        description = d.pop("description")

        placeholder_text_input = d.pop("placeholder_text_input", UNSET)

        ai_task_builder_free_text_input_instruction = cls(
            id=id,
            created_at=created_at,
            type_=type_,
            batch_id=batch_id,
            created_by=created_by,
            description=description,
            placeholder_text_input=placeholder_text_input,
        )

        ai_task_builder_free_text_input_instruction.additional_properties = d
        return ai_task_builder_free_text_input_instruction

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
