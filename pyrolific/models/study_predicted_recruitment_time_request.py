from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.study_predicted_recruitment_time_request_device_compatibility_item import (
    StudyPredictedRecruitmentTimeRequestDeviceCompatibilityItem,
)
from ..models.study_predicted_recruitment_time_request_peripheral_requirements_item import (
    StudyPredictedRecruitmentTimeRequestPeripheralRequirementsItem,
)
from ..models.study_predicted_recruitment_time_request_study_labels import (
    StudyPredictedRecruitmentTimeRequestStudyLabels,
)
from ..models.study_predicted_recruitment_time_request_study_type import StudyPredictedRecruitmentTimeRequestStudyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.range_filter import RangeFilter
    from ..models.select_filter import SelectFilter


T = TypeVar("T", bound="StudyPredictedRecruitmentTimeRequest")


@_attrs_define
class StudyPredictedRecruitmentTimeRequest:
    """
    Attributes:
        filters (list[Union['RangeFilter', 'SelectFilter']]): List of filters to apply to the count. This parameter uses
            the new, simplified
            filters schema for interacting with eligibility.
        workspace_id (str): The ID of the workspace the study will be created in.
        reward (float): How much are you going to pay the participants in cents. We use the currency of the workspace
        study_type (StudyPredictedRecruitmentTimeRequestStudyType): Type of study.
        total_available_places (float): How many participants are you looking to recruit
        estimated_completion_time (float): Estimated duration in minutes of the experiment or survey
        device_compatibility (Union[Unset, list[StudyPredictedRecruitmentTimeRequestDeviceCompatibilityItem]]): Add all
            devices that participants can use.
            You can include one or more options.
        peripheral_requirements (Union[Unset, list[StudyPredictedRecruitmentTimeRequestPeripheralRequirementsItem]]):
            Add all requirements that participants have to meet.
        study_labels (Union[Unset, StudyPredictedRecruitmentTimeRequestStudyLabels]): The field that the study is about
            to get tagged with.
    """

    filters: list[Union["RangeFilter", "SelectFilter"]]
    workspace_id: str
    reward: float
    study_type: StudyPredictedRecruitmentTimeRequestStudyType
    total_available_places: float
    estimated_completion_time: float
    device_compatibility: Union[Unset, list[StudyPredictedRecruitmentTimeRequestDeviceCompatibilityItem]] = UNSET
    peripheral_requirements: Union[Unset, list[StudyPredictedRecruitmentTimeRequestPeripheralRequirementsItem]] = UNSET
    study_labels: Union[Unset, StudyPredictedRecruitmentTimeRequestStudyLabels] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.select_filter import SelectFilter

        filters = []
        for filters_item_data in self.filters:
            filters_item: dict[str, Any]
            if isinstance(filters_item_data, SelectFilter):
                filters_item = filters_item_data.to_dict()
            else:
                filters_item = filters_item_data.to_dict()

            filters.append(filters_item)

        workspace_id = self.workspace_id

        reward = self.reward

        study_type = self.study_type.value

        total_available_places = self.total_available_places

        estimated_completion_time = self.estimated_completion_time

        device_compatibility: Union[Unset, list[str]] = UNSET
        if not isinstance(self.device_compatibility, Unset):
            device_compatibility = []
            for device_compatibility_item_data in self.device_compatibility:
                device_compatibility_item = device_compatibility_item_data.value
                device_compatibility.append(device_compatibility_item)

        peripheral_requirements: Union[Unset, list[str]] = UNSET
        if not isinstance(self.peripheral_requirements, Unset):
            peripheral_requirements = []
            for peripheral_requirements_item_data in self.peripheral_requirements:
                peripheral_requirements_item = peripheral_requirements_item_data.value
                peripheral_requirements.append(peripheral_requirements_item)

        study_labels: Union[Unset, str] = UNSET
        if not isinstance(self.study_labels, Unset):
            study_labels = self.study_labels.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
                "workspace_id": workspace_id,
                "reward": reward,
                "study_type": study_type,
                "total_available_places": total_available_places,
                "estimated_completion_time": estimated_completion_time,
            }
        )
        if device_compatibility is not UNSET:
            field_dict["device_compatibility"] = device_compatibility
        if peripheral_requirements is not UNSET:
            field_dict["peripheral_requirements"] = peripheral_requirements
        if study_labels is not UNSET:
            field_dict["study_labels"] = study_labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.range_filter import RangeFilter
        from ..models.select_filter import SelectFilter

        d = src_dict.copy()
        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:

            def _parse_filters_item(data: object) -> Union["RangeFilter", "SelectFilter"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    filters_item_type_0 = SelectFilter.from_dict(data)

                    return filters_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                filters_item_type_1 = RangeFilter.from_dict(data)

                return filters_item_type_1

            filters_item = _parse_filters_item(filters_item_data)

            filters.append(filters_item)

        workspace_id = d.pop("workspace_id")

        reward = d.pop("reward")

        study_type = StudyPredictedRecruitmentTimeRequestStudyType(d.pop("study_type"))

        total_available_places = d.pop("total_available_places")

        estimated_completion_time = d.pop("estimated_completion_time")

        device_compatibility = []
        _device_compatibility = d.pop("device_compatibility", UNSET)
        for device_compatibility_item_data in _device_compatibility or []:
            device_compatibility_item = StudyPredictedRecruitmentTimeRequestDeviceCompatibilityItem(
                device_compatibility_item_data
            )

            device_compatibility.append(device_compatibility_item)

        peripheral_requirements = []
        _peripheral_requirements = d.pop("peripheral_requirements", UNSET)
        for peripheral_requirements_item_data in _peripheral_requirements or []:
            peripheral_requirements_item = StudyPredictedRecruitmentTimeRequestPeripheralRequirementsItem(
                peripheral_requirements_item_data
            )

            peripheral_requirements.append(peripheral_requirements_item)

        _study_labels = d.pop("study_labels", UNSET)
        study_labels: Union[Unset, StudyPredictedRecruitmentTimeRequestStudyLabels]
        if isinstance(_study_labels, Unset):
            study_labels = UNSET
        else:
            study_labels = StudyPredictedRecruitmentTimeRequestStudyLabels(_study_labels)

        study_predicted_recruitment_time_request = cls(
            filters=filters,
            workspace_id=workspace_id,
            reward=reward,
            study_type=study_type,
            total_available_places=total_available_places,
            estimated_completion_time=estimated_completion_time,
            device_compatibility=device_compatibility,
            peripheral_requirements=peripheral_requirements,
            study_labels=study_labels,
        )

        study_predicted_recruitment_time_request.additional_properties = d
        return study_predicted_recruitment_time_request

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
