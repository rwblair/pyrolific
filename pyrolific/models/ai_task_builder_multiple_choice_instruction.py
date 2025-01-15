import datetime
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ai_task_builder_multiple_choice_instruction_type import AITaskBuilderMultipleChoiceInstructionType

if TYPE_CHECKING:
    from ..models.ai_task_builder_multiple_choice_instruction_options_item import (
        AITaskBuilderMultipleChoiceInstructionOptionsItem,
    )


T = TypeVar("T", bound="AITaskBuilderMultipleChoiceInstruction")


@_attrs_define
class AITaskBuilderMultipleChoiceInstruction:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        type_ (AITaskBuilderMultipleChoiceInstructionType):
        batch_id (str):
        created_by (str):
        description (str):
        options (list['AITaskBuilderMultipleChoiceInstructionOptionsItem']):
    """

    id: UUID
    created_at: datetime.datetime
    type_: AITaskBuilderMultipleChoiceInstructionType
    batch_id: str
    created_by: str
    description: str
    options: list["AITaskBuilderMultipleChoiceInstructionOptionsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        type_ = self.type_.value

        batch_id = self.batch_id

        created_by = self.created_by

        description = self.description

        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)

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
                "options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.ai_task_builder_multiple_choice_instruction_options_item import (
            AITaskBuilderMultipleChoiceInstructionOptionsItem,
        )

        d = src_dict.copy()
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        type_ = AITaskBuilderMultipleChoiceInstructionType(d.pop("type"))

        batch_id = d.pop("batch_id")

        created_by = d.pop("created_by")

        description = d.pop("description")

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = AITaskBuilderMultipleChoiceInstructionOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        ai_task_builder_multiple_choice_instruction = cls(
            id=id,
            created_at=created_at,
            type_=type_,
            batch_id=batch_id,
            created_by=created_by,
            description=description,
            options=options,
        )

        ai_task_builder_multiple_choice_instruction.additional_properties = d
        return ai_task_builder_multiple_choice_instruction

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
