from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SendBulkMessage")


@_attrs_define
class SendBulkMessage:
    """
    Attributes:
        ids (list[str]): A list of participant ID's
        body (str): Message Body. Text is sanitised for safe storage and display.
        study_id (str): A study ID
    """

    ids: list[str]
    body: str
    study_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        body = self.body

        study_id = self.study_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
                "body": body,
                "study_id": study_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ids = cast(list[str], d.pop("ids"))

        body = d.pop("body")

        study_id = d.pop("study_id")

        send_bulk_message = cls(
            ids=ids,
            body=body,
            study_id=study_id,
        )

        send_bulk_message.additional_properties = d
        return send_bulk_message

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
