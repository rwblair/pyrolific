from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParticipantGroupUpdate")


@_attrs_define
class ParticipantGroupUpdate:
    """
    Attributes:
        name (Union[Unset, str]): The name of the participant group Example: Group 1.
        participant_ids (Union[Unset, list[str]]): The ids of participants to be included in the group.

            Note, this overwrites any existing participants in the group; use the participant group membership endpoints to
            [append](#tag/Participant-Groups/operation/AddToParticipantGroup) or [remove](#tag/Participant-
            Groups/operation/RemoveFromParticipantGroup) participants from the group. Example: ['5e9b9c9b0f9c9a0001b0b1f4',
            '5e9b9c9b0f9c9a0001b0b1f5', '5e9b9c9b0f9c9a0001b0b1f6'].
    """

    name: Union[Unset, str] = UNSET
    participant_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        participant_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.participant_ids, Unset):
            participant_ids = self.participant_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if participant_ids is not UNSET:
            field_dict["participant_ids"] = participant_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        participant_ids = cast(list[str], d.pop("participant_ids", UNSET))

        participant_group_update = cls(
            name=name,
            participant_ids=participant_ids,
        )

        participant_group_update.additional_properties = d
        return participant_group_update

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
