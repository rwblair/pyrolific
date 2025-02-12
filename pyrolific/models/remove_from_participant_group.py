from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.remove_from_participant_group_action import RemoveFromParticipantGroupAction

T = TypeVar("T", bound="RemoveFromParticipantGroup")


@_attrs_define
class RemoveFromParticipantGroup:
    """
    Attributes:
        action (RemoveFromParticipantGroupAction): The action to take
        participant_group (str): The participant group to remove the participant from. Example:
            636e4f379e7d29c6875313e3.
    """

    action: RemoveFromParticipantGroupAction
    participant_group: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        participant_group = self.participant_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "participant_group": participant_group,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        action = RemoveFromParticipantGroupAction(d.pop("action"))

        participant_group = d.pop("participant_group")

        remove_from_participant_group = cls(
            action=action,
            participant_group=participant_group,
        )

        remove_from_participant_group.additional_properties = d
        return remove_from_participant_group

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
