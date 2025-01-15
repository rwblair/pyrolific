from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubmissionTransitionCompletionCodeData")


@_attrs_define
class SubmissionTransitionCompletionCodeData:
    """Required if the action is 'COMPLETE' and the code has the action "DYNAMIC_PAYMENT" associated with it.

    Attributes:
        percentage_of_reward (Union[Unset, float]): Required if the code is for a DYNAMIC_PAYMENT action. Must be
            between 8 - 99 (inclusive).
        message_to_participant (Union[Unset, str]): Optional message to the participant to be sent alongside a dynamic
            payment.
    """

    percentage_of_reward: Union[Unset, float] = UNSET
    message_to_participant: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        percentage_of_reward = self.percentage_of_reward

        message_to_participant = self.message_to_participant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percentage_of_reward is not UNSET:
            field_dict["percentage_of_reward"] = percentage_of_reward
        if message_to_participant is not UNSET:
            field_dict["message_to_participant"] = message_to_participant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        percentage_of_reward = d.pop("percentage_of_reward", UNSET)

        message_to_participant = d.pop("message_to_participant", UNSET)

        submission_transition_completion_code_data = cls(
            percentage_of_reward=percentage_of_reward,
            message_to_participant=message_to_participant,
        )

        submission_transition_completion_code_data.additional_properties = d
        return submission_transition_completion_code_data

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
