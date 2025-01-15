from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dynamic_payment_action import DynamicPaymentAction

T = TypeVar("T", bound="DynamicPayment")


@_attrs_define
class DynamicPayment:
    """
    Attributes:
        action (DynamicPaymentAction): Use this action to set up a dynamic payment study. Only certain workspaces have
            access to this feature. When using this action, the actor must be "researcher".
    """

    action: DynamicPaymentAction
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        action = DynamicPaymentAction(d.pop("action"))

        dynamic_payment = cls(
            action=action,
        )

        dynamic_payment.additional_properties = d
        return dynamic_payment

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
