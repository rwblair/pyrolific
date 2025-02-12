from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.mutually_exclusive_study_collections_response import MutuallyExclusiveStudyCollectionsResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    project_id: str,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["project_id"] = project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/study-collections/mutually-exclusive/",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MutuallyExclusiveStudyCollectionsResponse]:
    if response.status_code == 200:
        response_200 = MutuallyExclusiveStudyCollectionsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MutuallyExclusiveStudyCollectionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    project_id: str,
    authorization: str,
) -> Response[MutuallyExclusiveStudyCollectionsResponse]:
    """List mutually exclusive study collections in a project

     List studies

    Args:
        project_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MutuallyExclusiveStudyCollectionsResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    project_id: str,
    authorization: str,
) -> Optional[MutuallyExclusiveStudyCollectionsResponse]:
    """List mutually exclusive study collections in a project

     List studies

    Args:
        project_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MutuallyExclusiveStudyCollectionsResponse
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project_id: str,
    authorization: str,
) -> Response[MutuallyExclusiveStudyCollectionsResponse]:
    """List mutually exclusive study collections in a project

     List studies

    Args:
        project_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MutuallyExclusiveStudyCollectionsResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    project_id: str,
    authorization: str,
) -> Optional[MutuallyExclusiveStudyCollectionsResponse]:
    """List mutually exclusive study collections in a project

     List studies

    Args:
        project_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MutuallyExclusiveStudyCollectionsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            authorization=authorization,
        )
    ).parsed
