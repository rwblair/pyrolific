from typing import Any, Dict, Type, TypeVar


from attrs import define as _attrs_define

from ..types import UNSET, Unset

from typing import Union
from ..types import UNSET, Unset
from typing import cast, List


T = TypeVar("T", bound="MutuallyExclusiveStudyCollectionStudies")


@_attrs_define
class MutuallyExclusiveStudyCollectionStudies:
    """
    Attributes:
        study_ids (Union[Unset, List[str]]): List of study ids you wish to add to the collection
    """

    study_ids: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        study_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.study_ids, Unset):
            study_ids = self.study_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if study_ids is not UNSET:
            field_dict["study_ids"] = study_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        study_ids = cast(List[str], d.pop("study_ids", UNSET))

        mutually_exclusive_study_collection_studies = cls(
            study_ids=study_ids,
        )

        return mutually_exclusive_study_collection_studies
