from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.mutually_exclusive_study_collection_update import (
    MutuallyExclusiveStudyCollectionUpdate,
)
from typing import Dict


def _get_kwargs(
    id: str,
    *,
    authorization: str,
) -> Dict[str, Any]:
    headers = {}
    headers["Authorization"] = authorization

    return {
        "method": "get",
        "url": "/api/v1/study-collections/mutually-exclusive/{id}/".format(
            id=id,
        ),
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MutuallyExclusiveStudyCollectionUpdate]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MutuallyExclusiveStudyCollectionUpdate.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MutuallyExclusiveStudyCollectionUpdate]:
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
) -> Response[MutuallyExclusiveStudyCollectionUpdate]:
    """Get a mutually exclusive study collection

     Get a mutually exclusive study collection

    Args:
        id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MutuallyExclusiveStudyCollectionUpdate]
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
) -> Optional[MutuallyExclusiveStudyCollectionUpdate]:
    """Get a mutually exclusive study collection

     Get a mutually exclusive study collection

    Args:
        id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MutuallyExclusiveStudyCollectionUpdate
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
) -> Response[MutuallyExclusiveStudyCollectionUpdate]:
    """Get a mutually exclusive study collection

     Get a mutually exclusive study collection

    Args:
        id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MutuallyExclusiveStudyCollectionUpdate]
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
) -> Optional[MutuallyExclusiveStudyCollectionUpdate]:
    """Get a mutually exclusive study collection

     Get a mutually exclusive study collection

    Args:
        id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MutuallyExclusiveStudyCollectionUpdate
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            authorization=authorization,
        )
    ).parsed