from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_invitation_request_role import CreateInvitationRequestRole
from ..types import UNSET, Unset
from typing import Union
from typing import cast, List


T = TypeVar("T", bound="CreateInvitationRequest")


@_attrs_define
class CreateInvitationRequest:
    """
    Attributes:
        association (Union[Unset, str]): The ID of the workspace to which the users are being invited.
        emails (Union[Unset, List[str]]): An array of email addresses of the users to invite.
        role (Union[Unset, CreateInvitationRequestRole]): The role that the invited users will have in the workspace or
            project. This can be one of the following:
            - "WORKSPACE_ADMIN": The user will have administrative rights in the workspace. They can manage settings, invite
            users, and oversee all projects.
            - "WORKSPACE_COLLABORATOR": The user will be a regular collaborator in the workspace. They can contribute to
            projects but don't have administrative rights.
            - "PROJECT_EDITOR": The user will have edit rights for a specific project within a workspace.
    """

    association: Union[Unset, str] = UNSET
    emails: Union[Unset, List[str]] = UNSET
    role: Union[Unset, CreateInvitationRequestRole] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        association = self.association
        emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = self.emails

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if association is not UNSET:
            field_dict["association"] = association
        if emails is not UNSET:
            field_dict["emails"] = emails
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        association = d.pop("association", UNSET)

        emails = cast(List[str], d.pop("emails", UNSET))

        _role = d.pop("role", UNSET)
        role: Union[Unset, CreateInvitationRequestRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = CreateInvitationRequestRole(_role)

        create_invitation_request = cls(
            association=association,
            emails=emails,
            role=role,
        )

        create_invitation_request.additional_properties = d
        return create_invitation_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
