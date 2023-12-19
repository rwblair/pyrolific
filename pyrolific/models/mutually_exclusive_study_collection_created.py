from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from ..types import UNSET, Unset
from ..models.mutually_exclusive_study_collection_created_status import (
    MutuallyExclusiveStudyCollectionCreatedStatus,
)


T = TypeVar("T", bound="MutuallyExclusiveStudyCollectionCreated")


@_attrs_define
class MutuallyExclusiveStudyCollectionCreated:
    """
    Attributes:
        status (Union[Unset, MutuallyExclusiveStudyCollectionCreatedStatus]): Status of the study collection Example:
            ACTIVE.
        estimated_cost (Union[Unset, None, str]): Estimated cost of the study collection Example: £0.00.
        total_cost (Union[Unset, None, str]): Estimated cost of the study collection Example: £0.00.
    """

    status: Union[Unset, MutuallyExclusiveStudyCollectionCreatedStatus] = UNSET
    estimated_cost: Union[Unset, None, str] = UNSET
    total_cost: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        estimated_cost = self.estimated_cost
        total_cost = self.total_cost

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if estimated_cost is not UNSET:
            field_dict["estimated_cost"] = estimated_cost
        if total_cost is not UNSET:
            field_dict["total_cost"] = total_cost

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, MutuallyExclusiveStudyCollectionCreatedStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MutuallyExclusiveStudyCollectionCreatedStatus(_status)

        estimated_cost = d.pop("estimated_cost", UNSET)

        total_cost = d.pop("total_cost", UNSET)

        mutually_exclusive_study_collection_created = cls(
            status=status,
            estimated_cost=estimated_cost,
            total_cost=total_cost,
        )

        return mutually_exclusive_study_collection_created
