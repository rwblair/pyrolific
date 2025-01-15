from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageParticipantGroup")


@_attrs_define
class MessageParticipantGroup:
    """
    Attributes:
        participant_group_id (str): A participant group ID
        body (str): Message Body. Text is sanitised for safe storage and display.
        study_id (Union[Unset, str]): A study ID
    """

    participant_group_id: str
    body: str
    study_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        participant_group_id = self.participant_group_id

        body = self.body

        study_id = self.study_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "participant_group_id": participant_group_id,
                "body": body,
            }
        )
        if study_id is not UNSET:
            field_dict["study_id"] = study_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        participant_group_id = d.pop("participant_group_id")

        body = d.pop("body")

        study_id = d.pop("study_id", UNSET)

        message_participant_group = cls(
            participant_group_id=participant_group_id,
            body=body,
            study_id=study_id,
        )

        message_participant_group.additional_properties = d
        return message_participant_group

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
