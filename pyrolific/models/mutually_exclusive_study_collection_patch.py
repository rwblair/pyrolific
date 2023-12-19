from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from ..types import UNSET, Unset
from typing import cast, List


T = TypeVar("T", bound="MutuallyExclusiveStudyCollectionPatch")


@_attrs_define
class MutuallyExclusiveStudyCollectionPatch:
    """
    Attributes:
        name (str): Mutually exclusive study collection name Example: My Mutually Exclusive Study Collection.
        description (str): A description of the study collection Example: This is a description of my mutually exclusive
            study collection.
        project_id (str): Project id Example: 5f7b9a7b5f7b9a7b5f7b9a7b.
        id (Union[Unset, str]): Mutually exclusive study collection id Example: 6527ffc7fcc2e63a7a555488.
        study_ids (Union[Unset, List[str]]): List of study ids you wish to add to the collection
    """

    name: str
    description: str
    project_id: str
    id: Union[Unset, str] = UNSET
    study_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        project_id = self.project_id
        id = self.id
        study_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.study_ids, Unset):
            study_ids = self.study_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "project_id": project_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if study_ids is not UNSET:
            field_dict["study_ids"] = study_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description")

        project_id = d.pop("project_id")

        id = d.pop("id", UNSET)

        study_ids = cast(List[str], d.pop("study_ids", UNSET))

        mutually_exclusive_study_collection_patch = cls(
            name=name,
            description=description,
            project_id=project_id,
            id=id,
            study_ids=study_ids,
        )

        mutually_exclusive_study_collection_patch.additional_properties = d
        return mutually_exclusive_study_collection_patch

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
