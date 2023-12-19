from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from ..models.mutually_exclusive_study_collection_created_status import (
    MutuallyExclusiveStudyCollectionCreatedStatus,
)
from ..types import UNSET, Unset
from typing import cast, List


T = TypeVar("T", bound="MutuallyExclusiveStudyCollectionDetail")


@_attrs_define
class MutuallyExclusiveStudyCollectionDetail:
    """
    Attributes:
        name (str): Mutually exclusive study collection name Example: My Mutually Exclusive Study Collection.
        description (str): A description of the study collection Example: This is a description of my mutually exclusive
            study collection.
        project_id (str): Project id Example: 5f7b9a7b5f7b9a7b5f7b9a7b.
        id (Union[Unset, str]): Mutually exclusive study collection id Example: 6527ffc7fcc2e63a7a555488.
        status (Union[Unset, MutuallyExclusiveStudyCollectionCreatedStatus]): Status of the study collection Example:
            ACTIVE.
        estimated_cost (Union[Unset, None, str]): Estimated cost of the study collection Example: £0.00.
        total_cost (Union[Unset, None, str]): Estimated cost of the study collection Example: £0.00.
        study_ids (Union[Unset, List[str]]): List of study ids you wish to add to the collection
    """

    name: str
    description: str
    project_id: str
    id: Union[Unset, str] = UNSET
    status: Union[Unset, MutuallyExclusiveStudyCollectionCreatedStatus] = UNSET
    estimated_cost: Union[Unset, None, str] = UNSET
    total_cost: Union[Unset, None, str] = UNSET
    study_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        project_id = self.project_id
        id = self.id
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        estimated_cost = self.estimated_cost
        total_cost = self.total_cost
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
        if status is not UNSET:
            field_dict["status"] = status
        if estimated_cost is not UNSET:
            field_dict["estimated_cost"] = estimated_cost
        if total_cost is not UNSET:
            field_dict["total_cost"] = total_cost
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

        _status = d.pop("status", UNSET)
        status: Union[Unset, MutuallyExclusiveStudyCollectionCreatedStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MutuallyExclusiveStudyCollectionCreatedStatus(_status)

        estimated_cost = d.pop("estimated_cost", UNSET)

        total_cost = d.pop("total_cost", UNSET)

        study_ids = cast(List[str], d.pop("study_ids", UNSET))

        mutually_exclusive_study_collection_detail = cls(
            name=name,
            description=description,
            project_id=project_id,
            id=id,
            status=status,
            estimated_cost=estimated_cost,
            total_cost=total_cost,
            study_ids=study_ids,
        )

        mutually_exclusive_study_collection_detail.additional_properties = d
        return mutually_exclusive_study_collection_detail

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
