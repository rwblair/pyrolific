from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lock_filter_set_response_200 import LockFilterSetResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/filter-sets/{id}/lock/",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[LockFilterSetResponse200]:
    if response.status_code == 200:
        response_200 = LockFilterSetResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[LockFilterSetResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    authorization: str,
) -> Response[LockFilterSetResponse200]:
    """Lock filter set for editing

     Lock the filter set for editing.

    Args:
        id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LockFilterSetResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    authorization: str,
) -> Optional[LockFilterSetResponse200]:
    """Lock filter set for editing

     Lock the filter set for editing.

    Args:
        id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LockFilterSetResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    authorization: str,
) -> Response[LockFilterSetResponse200]:
    """Lock filter set for editing

     Lock the filter set for editing.

    Args:
        id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LockFilterSetResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    authorization: str,
) -> Optional[LockFilterSetResponse200]:
    """Lock filter set for editing

     Lock the filter set for editing.

    Args:
        id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LockFilterSetResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            authorization=authorization,
        )
    ).parsed
