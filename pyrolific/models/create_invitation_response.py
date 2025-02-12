from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invitation import Invitation


T = TypeVar("T", bound="CreateInvitationResponse")


@_attrs_define
class CreateInvitationResponse:
    """
    Attributes:
        invitations (Union[Unset, list['Invitation']]):
    """

    invitations: Union[Unset, list["Invitation"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invitations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.invitations, Unset):
            invitations = []
            for invitations_item_data in self.invitations:
                invitations_item = invitations_item_data.to_dict()
                invitations.append(invitations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invitations is not UNSET:
            field_dict["invitations"] = invitations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.invitation import Invitation

        d = src_dict.copy()
        invitations = []
        _invitations = d.pop("invitations", UNSET)
        for invitations_item_data in _invitations or []:
            invitations_item = Invitation.from_dict(invitations_item_data)

            invitations.append(invitations_item)

        create_invitation_response = cls(
            invitations=invitations,
        )

        create_invitation_response.additional_properties = d
        return create_invitation_response

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
