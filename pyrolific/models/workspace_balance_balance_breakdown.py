from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WorkspaceBalanceBalanceBreakdown")


@_attrs_define
class WorkspaceBalanceBalanceBreakdown:
    """A breakdown of the total balance of the workspace into:
    - Funds available to pay to participants
    - Funds pre-paid to Prolific for our services
    - Funds for any VAT applied to our Platform fees

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        workspace_balance_balance_breakdown = cls()

        workspace_balance_balance_breakdown.additional_properties = d
        return workspace_balance_balance_breakdown

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
