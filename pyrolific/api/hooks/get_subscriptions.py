from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.subscription_list import SubscriptionList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    is_enabled: Union[Unset, bool] = UNSET,
    workspace_id: Union[Unset, str] = UNSET,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["is_enabled"] = is_enabled

    params["workspace_id"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/hooks/subscriptions/",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SubscriptionList]:
    if response.status_code == 200:
        response_200 = SubscriptionList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SubscriptionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    is_enabled: Union[Unset, bool] = UNSET,
    workspace_id: Union[Unset, str] = UNSET,
    authorization: str,
) -> Response[SubscriptionList]:
    """List all subscriptions

     A view of all subscriptions you have created.

    Args:
        is_enabled (Union[Unset, bool]):
        workspace_id (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubscriptionList]
    """

    kwargs = _get_kwargs(
        is_enabled=is_enabled,
        workspace_id=workspace_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    is_enabled: Union[Unset, bool] = UNSET,
    workspace_id: Union[Unset, str] = UNSET,
    authorization: str,
) -> Optional[SubscriptionList]:
    """List all subscriptions

     A view of all subscriptions you have created.

    Args:
        is_enabled (Union[Unset, bool]):
        workspace_id (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubscriptionList
    """

    return sync_detailed(
        client=client,
        is_enabled=is_enabled,
        workspace_id=workspace_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    is_enabled: Union[Unset, bool] = UNSET,
    workspace_id: Union[Unset, str] = UNSET,
    authorization: str,
) -> Response[SubscriptionList]:
    """List all subscriptions

     A view of all subscriptions you have created.

    Args:
        is_enabled (Union[Unset, bool]):
        workspace_id (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubscriptionList]
    """

    kwargs = _get_kwargs(
        is_enabled=is_enabled,
        workspace_id=workspace_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    is_enabled: Union[Unset, bool] = UNSET,
    workspace_id: Union[Unset, str] = UNSET,
    authorization: str,
) -> Optional[SubscriptionList]:
    """List all subscriptions

     A view of all subscriptions you have created.

    Args:
        is_enabled (Union[Unset, bool]):
        workspace_id (Union[Unset, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubscriptionList
    """

    return (
        await asyncio_detailed(
            client=client,
            is_enabled=is_enabled,
            workspace_id=workspace_id,
            authorization=authorization,
        )
    ).parsed
