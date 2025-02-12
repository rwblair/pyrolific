from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.requirements_count import RequirementsCount
from ...models.requirements_count_request import RequirementsCountRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RequirementsCountRequest,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/eligibility-count/",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RequirementsCount]:
    if response.status_code == 200:
        response_200 = RequirementsCount.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RequirementsCount]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RequirementsCountRequest,
    authorization: Union[Unset, str] = UNSET,
) -> Response[RequirementsCount]:
    """Count participants

     Count how many participants meet all the given filters.
    Only participants that pass **every one** of the filters are counted.
    Zero means that there are less than 25 participants. We do not show lower numbers to protect the
    privacy of the participants.

    To see a list of filters that may be passed to this endpoint, see the documentation for filters.

    Args:
        authorization (Union[Unset, str]):
        body (RequirementsCountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementsCount]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RequirementsCountRequest,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[RequirementsCount]:
    """Count participants

     Count how many participants meet all the given filters.
    Only participants that pass **every one** of the filters are counted.
    Zero means that there are less than 25 participants. We do not show lower numbers to protect the
    privacy of the participants.

    To see a list of filters that may be passed to this endpoint, see the documentation for filters.

    Args:
        authorization (Union[Unset, str]):
        body (RequirementsCountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementsCount
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RequirementsCountRequest,
    authorization: Union[Unset, str] = UNSET,
) -> Response[RequirementsCount]:
    """Count participants

     Count how many participants meet all the given filters.
    Only participants that pass **every one** of the filters are counted.
    Zero means that there are less than 25 participants. We do not show lower numbers to protect the
    privacy of the participants.

    To see a list of filters that may be passed to this endpoint, see the documentation for filters.

    Args:
        authorization (Union[Unset, str]):
        body (RequirementsCountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementsCount]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RequirementsCountRequest,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[RequirementsCount]:
    """Count participants

     Count how many participants meet all the given filters.
    Only participants that pass **every one** of the filters are counted.
    Zero means that there are less than 25 participants. We do not show lower numbers to protect the
    privacy of the participants.

    To see a list of filters that may be passed to this endpoint, see the documentation for filters.

    Args:
        authorization (Union[Unset, str]):
        body (RequirementsCountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementsCount
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
