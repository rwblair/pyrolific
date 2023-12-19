from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from ..types import UNSET, Unset


T = TypeVar("T", bound="MutuallyExclusiveStudyCollectionList")


@_attrs_define
class MutuallyExclusiveStudyCollectionList:
    """
    Attributes:
        name (str): Mutually exclusive study collection name Example: My Mutually Exclusive Study Collection.
        description (str): A description of the study collection Example: This is a description of my mutually exclusive
            study collection.
        project_id (str): Project id Example: 5f7b9a7b5f7b9a7b5f7b9a7b.
        id (Union[Unset, str]): Mutually exclusive study collection id Example: 6527ffc7fcc2e63a7a555488.
    """

    name: str
    description: str
    project_id: str
    id: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        project_id = self.project_id
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "description": description,
                "project_id": project_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description")

        project_id = d.pop("project_id")

        id = d.pop("id", UNSET)

        mutually_exclusive_study_collection_list = cls(
            name=name,
            description=description,
            project_id=project_id,
            id=id,
        )

        return mutually_exclusive_study_collection_list
