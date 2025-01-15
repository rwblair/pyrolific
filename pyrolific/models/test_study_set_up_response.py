from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestStudySetUpResponse")


@_attrs_define
class TestStudySetUpResponse:
    """
    Attributes:
        study_id (Union[Unset, str]): The ID of the study that was created for the test.
        study_url (Union[Unset, str]): The URL of the study that was created for the test.
    """

    study_id: Union[Unset, str] = UNSET
    study_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        study_id = self.study_id

        study_url = self.study_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if study_id is not UNSET:
            field_dict["study_id"] = study_id
        if study_url is not UNSET:
            field_dict["study_url"] = study_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        study_id = d.pop("study_id", UNSET)

        study_url = d.pop("study_url", UNSET)

        test_study_set_up_response = cls(
            study_id=study_id,
            study_url=study_url,
        )

        test_study_set_up_response.additional_properties = d
        return test_study_set_up_response

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
