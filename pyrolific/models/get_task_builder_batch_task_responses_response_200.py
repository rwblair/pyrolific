from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_task_builder_task_response import AITaskBuilderTaskResponse


T = TypeVar("T", bound="GetTaskBuilderBatchTaskResponsesResponse200")


@_attrs_define
class GetTaskBuilderBatchTaskResponsesResponse200:
    """
    Attributes:
        responses (Union[Unset, list['AITaskBuilderTaskResponse']]):
    """

    responses: Union[Unset, list["AITaskBuilderTaskResponse"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        responses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.responses, Unset):
            responses = []
            for responses_item_data in self.responses:
                responses_item = responses_item_data.to_dict()
                responses.append(responses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if responses is not UNSET:
            field_dict["responses"] = responses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.ai_task_builder_task_response import AITaskBuilderTaskResponse

        d = src_dict.copy()
        responses = []
        _responses = d.pop("responses", UNSET)
        for responses_item_data in _responses or []:
            responses_item = AITaskBuilderTaskResponse.from_dict(responses_item_data)

            responses.append(responses_item)

        get_task_builder_batch_task_responses_response_200 = cls(
            responses=responses,
        )

        get_task_builder_batch_task_responses_response_200.additional_properties = d
        return get_task_builder_batch_task_responses_response_200

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
