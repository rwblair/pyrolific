from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.filter_set_list import FilterSetList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workspace_id: Union[Unset, str] = UNSET,
    organisation_id: Union[Unset, str] = UNSET,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["workspace_id"] = workspace_id

    params["organisation_id"] = organisation_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/filter-sets/",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[FilterSetList]:
    if response.status_code == 200:
        response_200 = FilterSetList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[FilterSetList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, str] = UNSET,
    organisation_id: Union[Unset, str] = UNSET,
    authorization: str,
) -> Response[FilterSetList]:
    """List all filter sets

     List of all filter sets in the specified workspace.

    Args:
        workspace_id (Union[Unset, str]):
        organisation_id (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilterSetList]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        organisation_id=organisation_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, str] = UNSET,
    organisation_id: Union[Unset, str] = UNSET,
    authorization: str,
) -> Optional[FilterSetList]:
    """List all filter sets

     List of all filter sets in the specified workspace.

    Args:
        workspace_id (Union[Unset, str]):
        organisation_id (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilterSetList
    """

    return sync_detailed(
        client=client,
        workspace_id=workspace_id,
        organisation_id=organisation_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, str] = UNSET,
    organisation_id: Union[Unset, str] = UNSET,
    authorization: str,
) -> Response[FilterSetList]:
    """List all filter sets

     List of all filter sets in the specified workspace.

    Args:
        workspace_id (Union[Unset, str]):
        organisation_id (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilterSetList]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        organisation_id=organisation_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, str] = UNSET,
    organisation_id: Union[Unset, str] = UNSET,
    authorization: str,
) -> Optional[FilterSetList]:
    """List all filter sets

     List of all filter sets in the specified workspace.

    Args:
        workspace_id (Union[Unset, str]):
        organisation_id (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilterSetList
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_id=workspace_id,
            organisation_id=organisation_id,
            authorization=authorization,
        )
    ).parsed
