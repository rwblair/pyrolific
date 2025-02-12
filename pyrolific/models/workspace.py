from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_short import ProjectShort
    from ..models.workspace_user import WorkspaceUser


T = TypeVar("T", bound="Workspace")


@_attrs_define
class Workspace:
    """
    Example:
        {'id': '62fce6fff0a78eb4f3ebc09c', 'title': 'My workspace', 'description': 'This workspace does...', 'owner':
            '60a42f4c693c29420793cb73', 'users': [{'id': '60a42f4c693c29420793cb73', 'name': 'Joe Soap', 'email':
            'joe.soap@gmail.com', 'roles': ['WORKSPACE_ADMIN']}], 'projects': [{'id': '60a42f4c693c29420793cb73'}],
            'wallet': '61a65c06b084910b3f0c00d6'}

    Attributes:
        id (str): Workspace id. It is created by Prolific.
        title (str): Name of workspace
        description (Union[Unset, str]): What is this workspace used for
        owner (Union[Unset, str]): Workspace id. It is created by Prolific.
        users (Union[Unset, list['WorkspaceUser']]): Data for a user related to a workspace
        projects (Union[Unset, list['ProjectShort']]): Data for a project related to a workspace
        wallet (Union[Unset, str]): Wallet tied to workspace
        naivety_distribution_rate (Union[None, Unset, float]): The rate at which the studies within this workspace are
            distributed.
    """

    id: str
    title: str
    description: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    users: Union[Unset, list["WorkspaceUser"]] = UNSET
    projects: Union[Unset, list["ProjectShort"]] = UNSET
    wallet: Union[Unset, str] = UNSET
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

        projects: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)

        wallet = self.wallet

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
        if projects is not UNSET:
            field_dict["projects"] = projects
        if wallet is not UNSET:
            field_dict["wallet"] = wallet
        if naivety_distribution_rate is not UNSET:
            field_dict["naivety_distribution_rate"] = naivety_distribution_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.project_short import ProjectShort
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

        projects = []
        _projects = d.pop("projects", UNSET)
        for projects_item_data in _projects or []:
            projects_item = ProjectShort.from_dict(projects_item_data)

            projects.append(projects_item)

        wallet = d.pop("wallet", UNSET)

        def _parse_naivety_distribution_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        naivety_distribution_rate = _parse_naivety_distribution_rate(d.pop("naivety_distribution_rate", UNSET))

        workspace = cls(
            id=id,
            title=title,
            description=description,
            owner=owner,
            users=users,
            projects=projects,
            wallet=wallet,
            naivety_distribution_rate=naivety_distribution_rate,
        )

        workspace.additional_properties = d
        return workspace

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
