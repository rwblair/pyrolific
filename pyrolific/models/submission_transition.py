from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.submission_transition_action import SubmissionTransitionAction
from ..models.submission_transition_rejection_category import SubmissionTransitionRejectionCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.submission_transition_completion_code_data import SubmissionTransitionCompletionCodeData


T = TypeVar("T", bound="SubmissionTransition")


@_attrs_define
class SubmissionTransition:
    """
    Attributes:
        action (SubmissionTransitionAction): Action to execute. Example: APPROVE.
        message (Union[Unset, str]): Required if action is 'REJECT'. Message sent to the participant
            explaining the reason for the rejection.
            It must be at least 100 chars long. Example: Good explanation of the situation..
        rejection_category (Union[Unset, SubmissionTransitionRejectionCategory]): Required if action is 'REJECT', it
            sums as the category of
            the rejection. Example: LOW_EFFORT.
        completion_code (Union[Unset, str]): Required if the action is 'COMPLETE'. The completion code must match a
            value provided when creating the study, and the actor must have been set to `researcher`. Any actions that were
            provided during the set up of the completion code (e.g. automatically approve) will then be carried out.
        completion_code_data (Union[Unset, SubmissionTransitionCompletionCodeData]): Required if the action is
            'COMPLETE' and the code has the action "DYNAMIC_PAYMENT" associated with it.
    """

    action: SubmissionTransitionAction
    message: Union[Unset, str] = UNSET
    rejection_category: Union[Unset, SubmissionTransitionRejectionCategory] = UNSET
    completion_code: Union[Unset, str] = UNSET
    completion_code_data: Union[Unset, "SubmissionTransitionCompletionCodeData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        message = self.message

        rejection_category: Union[Unset, str] = UNSET
        if not isinstance(self.rejection_category, Unset):
            rejection_category = self.rejection_category.value

        completion_code = self.completion_code

        completion_code_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.completion_code_data, Unset):
            completion_code_data = self.completion_code_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if rejection_category is not UNSET:
            field_dict["rejection_category"] = rejection_category
        if completion_code is not UNSET:
            field_dict["completion_code"] = completion_code
        if completion_code_data is not UNSET:
            field_dict["completion_code_data"] = completion_code_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.submission_transition_completion_code_data import SubmissionTransitionCompletionCodeData

        d = src_dict.copy()
        action = SubmissionTransitionAction(d.pop("action"))

        message = d.pop("message", UNSET)

        _rejection_category = d.pop("rejection_category", UNSET)
        rejection_category: Union[Unset, SubmissionTransitionRejectionCategory]
        if isinstance(_rejection_category, Unset):
            rejection_category = UNSET
        else:
            rejection_category = SubmissionTransitionRejectionCategory(_rejection_category)

        completion_code = d.pop("completion_code", UNSET)

        _completion_code_data = d.pop("completion_code_data", UNSET)
        completion_code_data: Union[Unset, SubmissionTransitionCompletionCodeData]
        if isinstance(_completion_code_data, Unset):
            completion_code_data = UNSET
        else:
            completion_code_data = SubmissionTransitionCompletionCodeData.from_dict(_completion_code_data)

        submission_transition = cls(
            action=action,
            message=message,
            rejection_category=rejection_category,
            completion_code=completion_code,
            completion_code_data=completion_code_data,
        )

        submission_transition.additional_properties = d
        return submission_transition

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
