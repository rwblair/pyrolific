from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from ...models.subscription_event_list import SubscriptionEventList
from typing import Dict
from typing import Union
from typing import Optional


def _get_kwargs(
    subscription_id: str,
    *,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    status: Union[Unset, None, str] = UNSET,
    resource_id: Union[Unset, None, str] = UNSET,
    authorization: str,
) -> Dict[str, Any]:
    headers = {}
    headers["Authorization"] = authorization

    params: Dict[str, Any] = {}
    params["offset"] = offset

    params["limit"] = limit

    params["status"] = status

    params["resource_id"] = resource_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/api/v1/hooks/subscriptions/{subscription_id}/events/".format(
            subscription_id=subscription_id,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SubscriptionEventList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SubscriptionEventList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SubscriptionEventList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    status: Union[Unset, None, str] = UNSET,
    resource_id: Union[Unset, None, str] = UNSET,
    authorization: str,
) -> Response[SubscriptionEventList]:
    """Get subscription events

     Get all of the events that have triggered for the given subscription.

    Args:
        subscription_id (str):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        status (Union[Unset, None, str]):
        resource_id (Union[Unset, None, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubscriptionEventList]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        offset=offset,
        limit=limit,
        status=status,
        resource_id=resource_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    status: Union[Unset, None, str] = UNSET,
    resource_id: Union[Unset, None, str] = UNSET,
    authorization: str,
) -> Optional[SubscriptionEventList]:
    """Get subscription events

     Get all of the events that have triggered for the given subscription.

    Args:
        subscription_id (str):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        status (Union[Unset, None, str]):
        resource_id (Union[Unset, None, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubscriptionEventList
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
        offset=offset,
        limit=limit,
        status=status,
        resource_id=resource_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    status: Union[Unset, None, str] = UNSET,
    resource_id: Union[Unset, None, str] = UNSET,
    authorization: str,
) -> Response[SubscriptionEventList]:
    """Get subscription events

     Get all of the events that have triggered for the given subscription.

    Args:
        subscription_id (str):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        status (Union[Unset, None, str]):
        resource_id (Union[Unset, None, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubscriptionEventList]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        offset=offset,
        limit=limit,
        status=status,
        resource_id=resource_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    status: Union[Unset, None, str] = UNSET,
    resource_id: Union[Unset, None, str] = UNSET,
    authorization: str,
) -> Optional[SubscriptionEventList]:
    """Get subscription events

     Get all of the events that have triggered for the given subscription.

    Args:
        subscription_id (str):
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        status (Union[Unset, None, str]):
        resource_id (Union[Unset, None, str]):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubscriptionEventList
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
            offset=offset,
            limit=limit,
            status=status,
            resource_id=resource_id,
            authorization=authorization,
        )
    ).parsed
