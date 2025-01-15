from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_task_builder_batch import AITaskBuilderBatch
from ...models.create_task_builder_batch_body import CreateTaskBuilderBatchBody
from ...types import Response


def _get_kwargs(
    *,
    body: CreateTaskBuilderBatchBody,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/data-collection/batches",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AITaskBuilderBatch]:
    if response.status_code == 201:
        response_201 = AITaskBuilderBatch.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AITaskBuilderBatch]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateTaskBuilderBatchBody,
    authorization: str,
) -> Response[AITaskBuilderBatch]:
    """Create an AI Task Builder batch

     Create a new AI Task Builder batch.

    Args:
        authorization (str):
        body (CreateTaskBuilderBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AITaskBuilderBatch]
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
    body: CreateTaskBuilderBatchBody,
    authorization: str,
) -> Optional[AITaskBuilderBatch]:
    """Create an AI Task Builder batch

     Create a new AI Task Builder batch.

    Args:
        authorization (str):
        body (CreateTaskBuilderBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AITaskBuilderBatch
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateTaskBuilderBatchBody,
    authorization: str,
) -> Response[AITaskBuilderBatch]:
    """Create an AI Task Builder batch

     Create a new AI Task Builder batch.

    Args:
        authorization (str):
        body (CreateTaskBuilderBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AITaskBuilderBatch]
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
    body: CreateTaskBuilderBatchBody,
    authorization: str,
) -> Optional[AITaskBuilderBatch]:
    """Create an AI Task Builder batch

     Create a new AI Task Builder batch.

    Args:
        authorization (str):
        body (CreateTaskBuilderBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AITaskBuilderBatch
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
