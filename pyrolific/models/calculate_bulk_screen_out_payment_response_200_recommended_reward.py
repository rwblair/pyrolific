from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CalculateBulkScreenOutPaymentResponse200RecommendedReward")


@_attrs_define
class CalculateBulkScreenOutPaymentResponse200RecommendedReward:
    """
    Attributes:
        amount (Union[Unset, float]):  Example: 10.
        currency (Union[Unset, str]):  Example: GBP.
    """

    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        calculate_bulk_screen_out_payment_response_200_recommended_reward = cls(
            amount=amount,
            currency=currency,
        )

        calculate_bulk_screen_out_payment_response_200_recommended_reward.additional_properties = d
        return calculate_bulk_screen_out_payment_response_200_recommended_reward

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
