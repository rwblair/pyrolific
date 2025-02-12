from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RequestSubmissionReturnBody")


@_attrs_define
class RequestSubmissionReturnBody:
    """
    Example:
        {'request_return_reasons': ['Withdrew consent.', 'Did not finish study.']}

    Attributes:
        request_return_reasons (list[str]):
    """

    request_return_reasons: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_return_reasons = self.request_return_reasons

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "request_return_reasons": request_return_reasons,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        request_return_reasons = cast(list[str], d.pop("request_return_reasons"))

        request_submission_return_body = cls(
            request_return_reasons=request_return_reasons,
        )

        request_submission_return_body.additional_properties = d
        return request_submission_return_body

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
