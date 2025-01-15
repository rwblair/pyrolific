from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_screen_out_submissions_response_202_payment_per_participant import (
        BulkScreenOutSubmissionsResponse202PaymentPerParticipant,
    )


T = TypeVar("T", bound="BulkScreenOutSubmissionsResponse202")


@_attrs_define
class BulkScreenOutSubmissionsResponse202:
    """
    Attributes:
        message (Union[Unset, str]):  Example: The request to bulk screen out has been made successfully..
        payment_per_participant (Union[Unset, BulkScreenOutSubmissionsResponse202PaymentPerParticipant]):
    """

    message: Union[Unset, str] = UNSET
    payment_per_participant: Union[Unset, "BulkScreenOutSubmissionsResponse202PaymentPerParticipant"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        payment_per_participant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_per_participant, Unset):
            payment_per_participant = self.payment_per_participant.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if payment_per_participant is not UNSET:
            field_dict["payment_per_participant"] = payment_per_participant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.bulk_screen_out_submissions_response_202_payment_per_participant import (
            BulkScreenOutSubmissionsResponse202PaymentPerParticipant,
        )

        d = src_dict.copy()
        message = d.pop("message", UNSET)

        _payment_per_participant = d.pop("payment_per_participant", UNSET)
        payment_per_participant: Union[Unset, BulkScreenOutSubmissionsResponse202PaymentPerParticipant]
        if isinstance(_payment_per_participant, Unset):
            payment_per_participant = UNSET
        else:
            payment_per_participant = BulkScreenOutSubmissionsResponse202PaymentPerParticipant.from_dict(
                _payment_per_participant
            )

        bulk_screen_out_submissions_response_202 = cls(
            message=message,
            payment_per_participant=payment_per_participant,
        )

        bulk_screen_out_submissions_response_202.additional_properties = d
        return bulk_screen_out_submissions_response_202

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
