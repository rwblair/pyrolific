from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_task_builder_batch import AITaskBuilderBatch
from ...models.get_task_builder_batch_body import GetTaskBuilderBatchBody
from ...types import Response


def _get_kwargs(
    batch_id: str,
    *,
    body: GetTaskBuilderBatchBody,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/data-collection/batches/{batch_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AITaskBuilderBatch]:
    if response.status_code == 200:
        response_200 = AITaskBuilderBatch.from_dict(response.json())

        return response_200
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
    batch_id: str,
    *,
    client: AuthenticatedClient,
    body: GetTaskBuilderBatchBody,
    authorization: str,
) -> Response[AITaskBuilderBatch]:
    """Get AI Task Builder batch

     Get a specific AI Task Builder batch by its unique identifier.

    Args:
        batch_id (str):
        authorization (str):
        body (GetTaskBuilderBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AITaskBuilderBatch]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        body=body,
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
    body: GetTaskBuilderBatchBody,
    authorization: str,
) -> Optional[AITaskBuilderBatch]:
    """Get AI Task Builder batch

     Get a specific AI Task Builder batch by its unique identifier.

    Args:
        batch_id (str):
        authorization (str):
        body (GetTaskBuilderBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AITaskBuilderBatch
    """

    return sync_detailed(
        batch_id=batch_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    body: GetTaskBuilderBatchBody,
    authorization: str,
) -> Response[AITaskBuilderBatch]:
    """Get AI Task Builder batch

     Get a specific AI Task Builder batch by its unique identifier.

    Args:
        batch_id (str):
        authorization (str):
        body (GetTaskBuilderBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AITaskBuilderBatch]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    body: GetTaskBuilderBatchBody,
    authorization: str,
) -> Optional[AITaskBuilderBatch]:
    """Get AI Task Builder batch

     Get a specific AI Task Builder batch by its unique identifier.

    Args:
        batch_id (str):
        authorization (str):
        body (GetTaskBuilderBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AITaskBuilderBatch
    """

    return (
        await asyncio_detailed(
            batch_id=batch_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
