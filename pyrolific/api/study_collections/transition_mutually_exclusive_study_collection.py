from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.transition_mutually_exclusive_study_collection_json_body import (
    TransitionMutuallyExclusiveStudyCollectionJsonBody,
)
from typing import Dict
from ...models.mutually_exclusive_study_collection_create import (
    MutuallyExclusiveStudyCollectionCreate,
)


def _get_kwargs(
    id: str,
    *,
    json_body: TransitionMutuallyExclusiveStudyCollectionJsonBody,
    authorization: str,
) -> Dict[str, Any]:
    headers = {}
    headers["Authorization"] = authorization

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/api/v1/study-collections/mutually-exclusive/{id}/transition/".format(
            id=id,
        ),
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MutuallyExclusiveStudyCollectionCreate]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MutuallyExclusiveStudyCollectionCreate.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MutuallyExclusiveStudyCollectionCreate]:
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
    json_body: TransitionMutuallyExclusiveStudyCollectionJsonBody,
    authorization: str,
) -> Response[MutuallyExclusiveStudyCollectionCreate]:
    """Transition a mutually exclusive study collection

     Transition a mutually exclusive study collection. This is used to:
    - Publish a study collection
    - Cancel publish a study collection
    - Schedule publish a study collection

    Args:
        id (str):
        authorization (str):
        json_body (TransitionMutuallyExclusiveStudyCollectionJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MutuallyExclusiveStudyCollectionCreate]
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
    json_body: TransitionMutuallyExclusiveStudyCollectionJsonBody,
    authorization: str,
) -> Optional[MutuallyExclusiveStudyCollectionCreate]:
    """Transition a mutually exclusive study collection

     Transition a mutually exclusive study collection. This is used to:
    - Publish a study collection
    - Cancel publish a study collection
    - Schedule publish a study collection

    Args:
        id (str):
        authorization (str):
        json_body (TransitionMutuallyExclusiveStudyCollectionJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MutuallyExclusiveStudyCollectionCreate
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
    json_body: TransitionMutuallyExclusiveStudyCollectionJsonBody,
    authorization: str,
) -> Response[MutuallyExclusiveStudyCollectionCreate]:
    """Transition a mutually exclusive study collection

     Transition a mutually exclusive study collection. This is used to:
    - Publish a study collection
    - Cancel publish a study collection
    - Schedule publish a study collection

    Args:
        id (str):
        authorization (str):
        json_body (TransitionMutuallyExclusiveStudyCollectionJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MutuallyExclusiveStudyCollectionCreate]
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
    json_body: TransitionMutuallyExclusiveStudyCollectionJsonBody,
    authorization: str,
) -> Optional[MutuallyExclusiveStudyCollectionCreate]:
    """Transition a mutually exclusive study collection

     Transition a mutually exclusive study collection. This is used to:
    - Publish a study collection
    - Cancel publish a study collection
    - Schedule publish a study collection

    Args:
        id (str):
        authorization (str):
        json_body (TransitionMutuallyExclusiveStudyCollectionJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MutuallyExclusiveStudyCollectionCreate
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            authorization=authorization,
        )
    ).parsed
