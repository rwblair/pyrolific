from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workspace_user import WorkspaceUser


T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    """
    Example:
        {'id': '62fce6fff0a78eb4f3ebc09c', 'title': 'My project', 'description': 'This project is for...', 'owner':
            '60a42f4c693c29420793cb73', 'users': [{'id': '60a42f4c693c29420793cb73', 'name': 'Joe Soap', 'email':
            'joe.soap@gmail.com', 'roles': ['PROJECT_EDITOR']}], 'workspace': '60a42f4c693c29420793cb73',
            'naivety_distribution_rate': 0.5}

    Attributes:
        id (str): Project id. It is created by Prolific.
        title (str): Name of project
        description (Union[Unset, str]): What is this project used for
        owner (Union[Unset, str]): User id of the creator of the project. It is created by Prolific.
        users (Union[Unset, list['WorkspaceUser']]): Data for all users who have access to this project
        workspace (Union[Unset, str]): Id of the workspace this project is in. This is created by Prolific.
        naivety_distribution_rate (Union[None, Unset, float]): The rate at which the studies within this project are
            distributed.
    """

    id: str
    title: str
    description: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    users: Union[Unset, list["WorkspaceUser"]] = UNSET
    workspace: Union[Unset, str] = UNSET
    naivety_distribution_rate: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        description = self.description

        owner = self.owner

        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        workspace = self.workspace

        naivety_distribution_rate: Union[None, Unset, float]
        if isinstance(self.naivety_distribution_rate, Unset):
            naivety_distribution_rate = UNSET
        else:
            naivety_distribution_rate = self.naivety_distribution_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if owner is not UNSET:
            field_dict["owner"] = owner
        if users is not UNSET:
            field_dict["users"] = users
        if workspace is not UNSET:
            field_dict["workspace"] = workspace
        if naivety_distribution_rate is not UNSET:
            field_dict["naivety_distribution_rate"] = naivety_distribution_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.workspace_user import WorkspaceUser

        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title")

        description = d.pop("description", UNSET)

        owner = d.pop("owner", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = WorkspaceUser.from_dict(users_item_data)

            users.append(users_item)

        workspace = d.pop("workspace", UNSET)

        def _parse_naivety_distribution_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        naivety_distribution_rate = _parse_naivety_distribution_rate(d.pop("naivety_distribution_rate", UNSET))

        project = cls(
            id=id,
            title=title,
            description=description,
            owner=owner,
            users=users,
            workspace=workspace,
            naivety_distribution_rate=naivety_distribution_rate,
        )

        project.additional_properties = d
        return project

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
