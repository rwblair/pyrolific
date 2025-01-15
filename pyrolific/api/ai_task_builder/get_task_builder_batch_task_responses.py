from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_task_builder_batch_task_responses_response_200 import GetTaskBuilderBatchTaskResponsesResponse200
from ...types import Response


def _get_kwargs(
    batch_id: str,
    *,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/data-collection/batches/{batch_id}/responses",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetTaskBuilderBatchTaskResponsesResponse200]:
    if response.status_code == 200:
        response_200 = GetTaskBuilderBatchTaskResponsesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetTaskBuilderBatchTaskResponsesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    authorization: str,
) -> Response[GetTaskBuilderBatchTaskResponsesResponse200]:
    """Get AI Task Builder Batch Task Responses

     Get tasks for an AI Task Builder batch.

    Args:
        batch_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTaskBuilderBatchTaskResponsesResponse200]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    authorization: str,
) -> Optional[GetTaskBuilderBatchTaskResponsesResponse200]:
    """Get AI Task Builder Batch Task Responses

     Get tasks for an AI Task Builder batch.

    Args:
        batch_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTaskBuilderBatchTaskResponsesResponse200
    """

    return sync_detailed(
        batch_id=batch_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    authorization: str,
) -> Response[GetTaskBuilderBatchTaskResponsesResponse200]:
    """Get AI Task Builder Batch Task Responses

     Get tasks for an AI Task Builder batch.

    Args:
        batch_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTaskBuilderBatchTaskResponsesResponse200]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    authorization: str,
) -> Optional[GetTaskBuilderBatchTaskResponsesResponse200]:
    """Get AI Task Builder Batch Task Responses

     Get tasks for an AI Task Builder batch.

    Args:
        batch_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTaskBuilderBatchTaskResponsesResponse200
    """

    return (
        await asyncio_detailed(
            batch_id=batch_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
