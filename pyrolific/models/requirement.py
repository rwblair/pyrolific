from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute import Attribute
    from ..models.requirement_query import RequirementQuery


T = TypeVar("T", bound="Requirement")


@_attrs_define
class Requirement:
    """
    Attributes:
        field_cls (str): Type of requirement Example: SelectAnswerEligibilityRequirement.
        attributes (list['Attribute']): Attributes defining the requirement. Its values will depend
            on the type of requirement
        query (Union[Unset, RequirementQuery]):
    """

    field_cls: str
    attributes: list["Attribute"]
    query: Union[Unset, "RequirementQuery"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_cls = self.field_cls

        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        query: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_cls": field_cls,
                "attributes": attributes,
            }
        )
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.attribute import Attribute
        from ..models.requirement_query import RequirementQuery

        d = src_dict.copy()
        field_cls = d.pop("_cls")

        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = Attribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        _query = d.pop("query", UNSET)
        query: Union[Unset, RequirementQuery]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = RequirementQuery.from_dict(_query)

        requirement = cls(
            field_cls=field_cls,
            attributes=attributes,
            query=query,
        )

        requirement.additional_properties = d
        return requirement

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
