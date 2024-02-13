from typing import Any, Dict, Type, TypeVar

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union


T = TypeVar("T", bound="DuplicateStudyJsonBody")


@_attrs_define
class DuplicateStudyJsonBody:
    """
    Attributes:
        block_previous_participants (Union[Unset, bool]): Controls whether the block list is added or not. Default:
            True.
    """

    block_previous_participants: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        block_previous_participants = self.block_previous_participants

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_previous_participants is not UNSET:
            field_dict["block_previous_participants"] = block_previous_participants

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        block_previous_participants = d.pop("block_previous_participants", UNSET)

        duplicate_study_json_body = cls(
            block_previous_participants=block_previous_participants,
        )

        duplicate_study_json_body.additional_properties = d
        return duplicate_study_json_body

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
