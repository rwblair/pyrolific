from typing import Any, Dict, Type, TypeVar, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field


from typing import Dict

if TYPE_CHECKING:
    from ..models.range_filter_selected_range import RangeFilterSelectedRange


T = TypeVar("T", bound="RangeFilter")


@_attrs_define
class RangeFilter:
    r"""
    Attributes:
        filter_id (str): ID of the "range" type filter.
        selected_range (RangeFilterSelectedRange): This schema applies for filters of the `range` type, as defined in
            the [filter list response](\#tag/Filters/paths/~1api~1v1~1filters~1/get).

            A dictionary with two possible objects, 'lower' and 'upper'. At least one must be present and a non-null value.

            The expected data type for these values is defined by the `range` filter's `data_type` (see response linked
            above).

            If the data_type is a date, string format should be a parseable ISO8601 date string. Date values should be
            provided as a string in ISO 8601 format.

            Leaving a value as null will result in that bound being set to the lowest or highest possible value, depending
            on whether it is the upper or lower bound.
    """

    filter_id: str
    selected_range: "RangeFilterSelectedRange"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_id = self.filter_id
        selected_range = self.selected_range.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter_id": filter_id,
                "selected_range": selected_range,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.range_filter_selected_range import RangeFilterSelectedRange

        d = src_dict.copy()
        filter_id = d.pop("filter_id")

        selected_range = RangeFilterSelectedRange.from_dict(d.pop("selected_range"))

        range_filter = cls(
            filter_id=filter_id,
            selected_range=selected_range,
        )

        range_filter.additional_properties = d
        return range_filter

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
