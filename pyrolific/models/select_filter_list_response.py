from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_list_attributes_type import FilterListAttributesType
from ..models.select_filter_list_attributes_data_type import SelectFilterListAttributesDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.select_filter_list_attributes_choices import SelectFilterListAttributesChoices


T = TypeVar("T", bound="SelectFilterListResponse")


@_attrs_define
class SelectFilterListResponse:
    """
    Attributes:
        filter_id (Union[Unset, str]): The ID of the filter, based on a slugified version of the title at the time the
            filter was created.
        title (Union[Unset, str]): The title of the filter.
        description (Union[Unset, str]): A description of the filter.
        type_ (Union[Unset, FilterListAttributesType]): The filter type.
        question (Union[Unset, str]): The question asked of participants to generate this filter.
        choices (Union[Unset, SelectFilterListAttributesChoices]): An object containing all the filter's possible
            responses as key-value pairs, with sequential integer IDs or database ObjectIDs as the keys and the text of the
            response as the values.
        data_type (Union[Unset, SelectFilterListAttributesDataType]): The format of the keys in the choices object. If
            the keys are strings representing sequential integers,
            the data format is integer. If the keys are database ObjectIDs, the type of ID is specified.
    """

    filter_id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    type_: Union[Unset, FilterListAttributesType] = UNSET
    question: Union[Unset, str] = UNSET
    choices: Union[Unset, "SelectFilterListAttributesChoices"] = UNSET
    data_type: Union[Unset, SelectFilterListAttributesDataType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_id = self.filter_id

        title = self.title

        description = self.description

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        question = self.question

        choices: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.choices, Unset):
            choices = self.choices.to_dict()

        data_type: Union[Unset, str] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_id is not UNSET:
            field_dict["filter_id"] = filter_id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if question is not UNSET:
            field_dict["question"] = question
        if choices is not UNSET:
            field_dict["choices"] = choices
        if data_type is not UNSET:
            field_dict["data_type"] = data_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.select_filter_list_attributes_choices import SelectFilterListAttributesChoices

        d = src_dict.copy()
        filter_id = d.pop("filter_id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, FilterListAttributesType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FilterListAttributesType(_type_)

        question = d.pop("question", UNSET)

        _choices = d.pop("choices", UNSET)
        choices: Union[Unset, SelectFilterListAttributesChoices]
        if isinstance(_choices, Unset):
            choices = UNSET
        else:
            choices = SelectFilterListAttributesChoices.from_dict(_choices)

        _data_type = d.pop("data_type", UNSET)
        data_type: Union[Unset, SelectFilterListAttributesDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = SelectFilterListAttributesDataType(_data_type)

        select_filter_list_response = cls(
            filter_id=filter_id,
            title=title,
            description=description,
            type_=type_,
            question=question,
            choices=choices,
            data_type=data_type,
        )

        select_filter_list_response.additional_properties = d
        return select_filter_list_response

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
