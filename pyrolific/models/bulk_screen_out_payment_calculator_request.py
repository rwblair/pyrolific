from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkScreenOutPaymentCalculatorRequest")


@_attrs_define
class BulkScreenOutPaymentCalculatorRequest:
    """
    Attributes:
        submission_ids (list[str]): List of submission ids to screen out, must belong to the study.
    """

    submission_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        submission_ids = self.submission_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "submission_ids": submission_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        submission_ids = cast(list[str], d.pop("submission_ids"))

        bulk_screen_out_payment_calculator_request = cls(
            submission_ids=submission_ids,
        )

        bulk_screen_out_payment_calculator_request.additional_properties = d
        return bulk_screen_out_payment_calculator_request

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
