from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from typing import Dict
from ...models.mutually_exclusive_study_collection_update import (
    MutuallyExclusiveStudyCollectionUpdate,
)


def _get_kwargs(
    id: str,
    *,
    json_body: MutuallyExclusiveStudyCollectionUpdate,
    authorization: str,
) -> Dict[str, Any]:
    headers = {}
    headers["Authorization"] = authorization

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": "/api/v1/study-collections/mutually-exclusive/{id}/".format(
            id=id,
        ),
        "json": json_json_body,
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
    json_body: MutuallyExclusiveStudyCollectionUpdate,
    authorization: str,
) -> Response[MutuallyExclusiveStudyCollectionUpdate]:
    """Update a mutually exclusive study collection

     Update a mutually exclusive study collection

    Args:
        id (str):
        authorization (str):
        json_body (MutuallyExclusiveStudyCollectionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MutuallyExclusiveStudyCollectionUpdate]
    """

    kwargs = _get_kwargs(
        id=id,
        json_body=json_body,
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
    json_body: MutuallyExclusiveStudyCollectionUpdate,
    authorization: str,
) -> Optional[MutuallyExclusiveStudyCollectionUpdate]:
    """Update a mutually exclusive study collection

     Update a mutually exclusive study collection

    Args:
        id (str):
        authorization (str):
        json_body (MutuallyExclusiveStudyCollectionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MutuallyExclusiveStudyCollectionUpdate
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: MutuallyExclusiveStudyCollectionUpdate,
    authorization: str,
) -> Response[MutuallyExclusiveStudyCollectionUpdate]:
    """Update a mutually exclusive study collection

     Update a mutually exclusive study collection

    Args:
        id (str):
        authorization (str):
        json_body (MutuallyExclusiveStudyCollectionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MutuallyExclusiveStudyCollectionUpdate]
    """

    kwargs = _get_kwargs(
        id=id,
        json_body=json_body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: MutuallyExclusiveStudyCollectionUpdate,
    authorization: str,
) -> Optional[MutuallyExclusiveStudyCollectionUpdate]:
    """Update a mutually exclusive study collection

     Update a mutually exclusive study collection

    Args:
        id (str):
        authorization (str):
        json_body (MutuallyExclusiveStudyCollectionUpdate):

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
            json_body=json_body,
            authorization=authorization,
        )
    ).parsed
