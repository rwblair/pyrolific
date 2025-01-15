from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AccessDetail")


@_attrs_define
class AccessDetail:
    """
    Attributes:
        external_url (str): URL of the task you want to send the participant to. You can pass URL search parameters as
            in `external_study_url`.
        total_allocation (float): The number of places you want to be sent to this URL for taskflow.
    """

    external_url: str
    total_allocation: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_url = self.external_url

        total_allocation = self.total_allocation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_url": external_url,
                "total_allocation": total_allocation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        external_url = d.pop("external_url")

        total_allocation = d.pop("total_allocation")

        access_detail = cls(
            external_url=external_url,
            total_allocation=total_allocation,
        )

        access_detail.additional_properties = d
        return access_detail

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
