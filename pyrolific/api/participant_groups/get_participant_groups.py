from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_participant_groups_active import GetParticipantGroupsActive
from ...models.project_id import ProjectID
from ...models.workspace_id import WorkspaceID
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    active: Union[Unset, GetParticipantGroupsActive] = UNSET,
    filter_: Union["ProjectID", "WorkspaceID"],
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_active: Union[Unset, str] = UNSET
    if not isinstance(active, Unset):
        json_active = active.value

    params["active"] = json_active

    json_filter_: dict[str, Any]
    if isinstance(filter_, WorkspaceID):
        json_filter_ = filter_.to_dict()
    else:
        json_filter_ = filter_.to_dict()

    params["filter"] = json_filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/participant-groups/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    active: Union[Unset, GetParticipantGroupsActive] = UNSET,
    filter_: Union["ProjectID", "WorkspaceID"],
) -> Response[Any]:
    """Get a list of all participant groups within a project or workspace

    Args:
        active (Union[Unset, GetParticipantGroupsActive]):
        filter_ (Union['ProjectID', 'WorkspaceID']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        active=active,
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    active: Union[Unset, GetParticipantGroupsActive] = UNSET,
    filter_: Union["ProjectID", "WorkspaceID"],
) -> Response[Any]:
    """Get a list of all participant groups within a project or workspace

    Args:
        active (Union[Unset, GetParticipantGroupsActive]):
        filter_ (Union['ProjectID', 'WorkspaceID']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        active=active,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
