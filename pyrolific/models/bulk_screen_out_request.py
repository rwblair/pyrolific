from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkScreenOutRequest")


@_attrs_define
class BulkScreenOutRequest:
    """
    Attributes:
        submission_ids (list[str]): List of submission ids to screen out, must belong to the study.
        bonus_per_submission (Union[Unset, float]): The bonus amount to pay per submission, in your study currency.
            Minimum £0.10 or $0.14 per minute.
            Either bonus per submission or reward per hour must be provided. Example: 0.5.
        reward_per_hour (Union[Unset, float]): The reward per hour to pay per submission, in your study currency.
            Minimum £6.00 or $8.00.
            Either bonus per submission or reward per hour must be provided. Example: 6.0.
        increase_places (Union[Unset, bool]): Increase the number of places available in the study by the number of
            submissions screened out.
            If selected, this will increase the number of places by 1 for each person screened out. This will
            not reopen the study if the study has been paused or stopped.
    """

    submission_ids: list[str]
    bonus_per_submission: Union[Unset, float] = UNSET
    reward_per_hour: Union[Unset, float] = UNSET
    increase_places: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        submission_ids = self.submission_ids

        bonus_per_submission = self.bonus_per_submission

        reward_per_hour = self.reward_per_hour

        increase_places = self.increase_places

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "submission_ids": submission_ids,
            }
        )
        if bonus_per_submission is not UNSET:
            field_dict["bonus_per_submission"] = bonus_per_submission
        if reward_per_hour is not UNSET:
            field_dict["reward_per_hour"] = reward_per_hour
        if increase_places is not UNSET:
            field_dict["increase_places"] = increase_places

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        submission_ids = cast(list[str], d.pop("submission_ids"))

        bonus_per_submission = d.pop("bonus_per_submission", UNSET)

        reward_per_hour = d.pop("reward_per_hour", UNSET)

        increase_places = d.pop("increase_places", UNSET)

        bulk_screen_out_request = cls(
            submission_ids=submission_ids,
            bonus_per_submission=bonus_per_submission,
            reward_per_hour=reward_per_hour,
            increase_places=increase_places,
        )

        bulk_screen_out_request.additional_properties = d
        return bulk_screen_out_request

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
