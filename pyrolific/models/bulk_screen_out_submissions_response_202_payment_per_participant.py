from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkScreenOutSubmissionsResponse202PaymentPerParticipant")


@_attrs_define
class BulkScreenOutSubmissionsResponse202PaymentPerParticipant:
    """
    Attributes:
        amount (Union[Unset, float]): :- The payment paid to each participant in subcurrency value, not including fees
            or VAT. For GBP this would be in pence, for USD this would be in cents. Example: 15.
        currency (Union[Unset, str]): The currency of the payment. Example: GBP.
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

        bulk_screen_out_submissions_response_202_payment_per_participant = cls(
            amount=amount,
            currency=currency,
        )

        bulk_screen_out_submissions_response_202_payment_per_participant.additional_properties = d
        return bulk_screen_out_submissions_response_202_payment_per_participant

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
