from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterListDetailedAttributes")


@_attrs_define
class FilterListDetailedAttributes:
    """
    Attributes:
        researcher_help_text (Union[None, Unset, str]): Some help text to be displayed to researchers in the
            prescreening modal.
        participant_help_text (Union[None, Unset, str]): Some help text to be displayed to participants in the About You
            section.
        category (Union[None, Unset, str]): The category the filter is displayed in in About You and the prescreening
            modal.
        subcategory (Union[None, Unset, str]): The sub-category the filter is displayed in in the prescreening modal.
        display_order (Union[None, Unset, int]): The order in which the filter is displayed within its sub-category in
            the prescreening modal.
        tags (Union[None, Unset, list[str]]): Some additional tags that can be used to display the filter in a specific
            way, e.g. recommended, new, expiring.
    """

    researcher_help_text: Union[None, Unset, str] = UNSET
    participant_help_text: Union[None, Unset, str] = UNSET
    category: Union[None, Unset, str] = UNSET
    subcategory: Union[None, Unset, str] = UNSET
    display_order: Union[None, Unset, int] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        researcher_help_text: Union[None, Unset, str]
        if isinstance(self.researcher_help_text, Unset):
            researcher_help_text = UNSET
        else:
            researcher_help_text = self.researcher_help_text

        participant_help_text: Union[None, Unset, str]
        if isinstance(self.participant_help_text, Unset):
            participant_help_text = UNSET
        else:
            participant_help_text = self.participant_help_text

        category: Union[None, Unset, str]
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        subcategory: Union[None, Unset, str]
        if isinstance(self.subcategory, Unset):
            subcategory = UNSET
        else:
            subcategory = self.subcategory

        display_order: Union[None, Unset, int]
        if isinstance(self.display_order, Unset):
            display_order = UNSET
        else:
            display_order = self.display_order

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if researcher_help_text is not UNSET:
            field_dict["researcher_help_text"] = researcher_help_text
        if participant_help_text is not UNSET:
            field_dict["participant_help_text"] = participant_help_text
        if category is not UNSET:
            field_dict["category"] = category
        if subcategory is not UNSET:
            field_dict["subcategory"] = subcategory
        if display_order is not UNSET:
            field_dict["display_order"] = display_order
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_researcher_help_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        researcher_help_text = _parse_researcher_help_text(d.pop("researcher_help_text", UNSET))

        def _parse_participant_help_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        participant_help_text = _parse_participant_help_text(d.pop("participant_help_text", UNSET))

        def _parse_category(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_subcategory(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subcategory = _parse_subcategory(d.pop("subcategory", UNSET))

        def _parse_display_order(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        display_order = _parse_display_order(d.pop("display_order", UNSET))

        def _parse_tags(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        filter_list_detailed_attributes = cls(
            researcher_help_text=researcher_help_text,
            participant_help_text=participant_help_text,
            category=category,
            subcategory=subcategory,
            display_order=display_order,
            tags=tags,
        )

        filter_list_detailed_attributes.additional_properties = d
        return filter_list_detailed_attributes

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
