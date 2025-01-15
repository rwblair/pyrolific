from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.calculate_bulk_screen_out_payment_response_200_minimum_reward import (
        CalculateBulkScreenOutPaymentResponse200MinimumReward,
    )
    from ..models.calculate_bulk_screen_out_payment_response_200_recommended_reward import (
        CalculateBulkScreenOutPaymentResponse200RecommendedReward,
    )


T = TypeVar("T", bound="CalculateBulkScreenOutPaymentResponse200")


@_attrs_define
class CalculateBulkScreenOutPaymentResponse200:
    """
    Attributes:
        recommended_reward (Union[Unset, CalculateBulkScreenOutPaymentResponse200RecommendedReward]):
        minimum_reward (Union[Unset, CalculateBulkScreenOutPaymentResponse200MinimumReward]):
        average_submission_time_minutes (Union[Unset, float]):  Example: 10.
    """

    recommended_reward: Union[Unset, "CalculateBulkScreenOutPaymentResponse200RecommendedReward"] = UNSET
    minimum_reward: Union[Unset, "CalculateBulkScreenOutPaymentResponse200MinimumReward"] = UNSET
    average_submission_time_minutes: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recommended_reward: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recommended_reward, Unset):
            recommended_reward = self.recommended_reward.to_dict()

        minimum_reward: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.minimum_reward, Unset):
            minimum_reward = self.minimum_reward.to_dict()

        average_submission_time_minutes = self.average_submission_time_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recommended_reward is not UNSET:
            field_dict["recommended_reward"] = recommended_reward
        if minimum_reward is not UNSET:
            field_dict["minimum_reward"] = minimum_reward
        if average_submission_time_minutes is not UNSET:
            field_dict["average_submission_time_minutes"] = average_submission_time_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.calculate_bulk_screen_out_payment_response_200_minimum_reward import (
            CalculateBulkScreenOutPaymentResponse200MinimumReward,
        )
        from ..models.calculate_bulk_screen_out_payment_response_200_recommended_reward import (
            CalculateBulkScreenOutPaymentResponse200RecommendedReward,
        )

        d = src_dict.copy()
        _recommended_reward = d.pop("recommended_reward", UNSET)
        recommended_reward: Union[Unset, CalculateBulkScreenOutPaymentResponse200RecommendedReward]
        if isinstance(_recommended_reward, Unset):
            recommended_reward = UNSET
        else:
            recommended_reward = CalculateBulkScreenOutPaymentResponse200RecommendedReward.from_dict(
                _recommended_reward
            )

        _minimum_reward = d.pop("minimum_reward", UNSET)
        minimum_reward: Union[Unset, CalculateBulkScreenOutPaymentResponse200MinimumReward]
        if isinstance(_minimum_reward, Unset):
            minimum_reward = UNSET
        else:
            minimum_reward = CalculateBulkScreenOutPaymentResponse200MinimumReward.from_dict(_minimum_reward)

        average_submission_time_minutes = d.pop("average_submission_time_minutes", UNSET)

        calculate_bulk_screen_out_payment_response_200 = cls(
            recommended_reward=recommended_reward,
            minimum_reward=minimum_reward,
            average_submission_time_minutes=average_submission_time_minutes,
        )

        calculate_bulk_screen_out_payment_response_200.additional_properties = d
        return calculate_bulk_screen_out_payment_response_200

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
