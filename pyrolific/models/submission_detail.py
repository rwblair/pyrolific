import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.submission_detail_status import SubmissionDetailStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubmissionDetail")


@_attrs_define
class SubmissionDetail:
    """
    Example:
        {'id': '625d4a831bcda2d59ac5a251', 'completed_at': datetime.datetime(2022, 4, 18, 11, 25, 2, 734000,
            tzinfo=datetime.timezone(datetime.timedelta(0), 'Z')), 'entered_code': '8E8AC860', 'participant':
            '60bf9310e8dec401be6e9615', 'started_at': datetime.datetime(2022, 4, 18, 11, 24, 51, 395000,
            tzinfo=datetime.timezone(datetime.timedelta(0), 'Z')), 'status': 'APPROVED', 'study_id':
            '60aca280709ee40ec37d4885', 'bonus_payments': [1000, 2536]}

    Attributes:
        id (str): The id of the submission
        started_at (str): The date and time that the user started the submission (UTC)
        status (SubmissionDetailStatus): The current status of the submission
        study_id (str): Study id.
        completed_at (Union[None, Unset, str]): The time the submission was completed at.
        entered_code (Union[None, Unset, str]): The completion code used by the participant to complete the study.
        participant (Union[Unset, str]): Participant id.
        bonus_payments (Union[Unset, list[float]]): Bonus payments that have been paid on the submission. Returned in
            pence / cents.
        return_requested (Union[None, Unset, datetime.datetime]): The date and time when a return request for the
            submission was made.
    """

    id: str
    started_at: str
    status: SubmissionDetailStatus
    study_id: str
    completed_at: Union[None, Unset, str] = UNSET
    entered_code: Union[None, Unset, str] = UNSET
    participant: Union[Unset, str] = UNSET
    bonus_payments: Union[Unset, list[float]] = UNSET
    return_requested: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        started_at = self.started_at

        status = self.status.value

        study_id = self.study_id

        completed_at: Union[None, Unset, str]
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = self.completed_at

        entered_code: Union[None, Unset, str]
        if isinstance(self.entered_code, Unset):
            entered_code = UNSET
        else:
            entered_code = self.entered_code

        participant = self.participant

        bonus_payments: Union[Unset, list[float]] = UNSET
        if not isinstance(self.bonus_payments, Unset):
            bonus_payments = self.bonus_payments

        return_requested: Union[None, Unset, str]
        if isinstance(self.return_requested, Unset):
            return_requested = UNSET
        elif isinstance(self.return_requested, datetime.datetime):
            return_requested = self.return_requested.isoformat()
        else:
            return_requested = self.return_requested

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "started_at": started_at,
                "status": status,
                "study_id": study_id,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if entered_code is not UNSET:
            field_dict["entered_code"] = entered_code
        if participant is not UNSET:
            field_dict["participant"] = participant
        if bonus_payments is not UNSET:
            field_dict["bonus_payments"] = bonus_payments
        if return_requested is not UNSET:
            field_dict["return_requested"] = return_requested

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        started_at = d.pop("started_at")

        status = SubmissionDetailStatus(d.pop("status"))

        study_id = d.pop("study_id")

        def _parse_completed_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        def _parse_entered_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        entered_code = _parse_entered_code(d.pop("entered_code", UNSET))

        participant = d.pop("participant", UNSET)

        bonus_payments = cast(list[float], d.pop("bonus_payments", UNSET))

        def _parse_return_requested(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                return_requested_type_0 = isoparse(data)

                return return_requested_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        return_requested = _parse_return_requested(d.pop("return_requested", UNSET))

        submission_detail = cls(
            id=id,
            started_at=started_at,
            status=status,
            study_id=study_id,
            completed_at=completed_at,
            entered_code=entered_code,
            participant=participant,
            bonus_payments=bonus_payments,
            return_requested=return_requested,
        )

        submission_detail.additional_properties = d
        return submission_detail

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
