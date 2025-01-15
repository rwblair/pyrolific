from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_task_builder_batch import AITaskBuilderBatch
from ...models.get_task_builder_batches_body import GetTaskBuilderBatchesBody
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: GetTaskBuilderBatchesBody,
    workspace_id: str,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["workspace_id"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/data-collection/batches",
        "params": params,
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
    *,
    client: AuthenticatedClient,
    body: GetTaskBuilderBatchesBody,
    workspace_id: str,
    authorization: str,
) -> Response[AITaskBuilderBatch]:
    """Get all AI Task Builder batches by workspace

     Get all AI Task Builder batches by workspace id

    Args:
        workspace_id (str):
        authorization (str):
        body (GetTaskBuilderBatchesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AITaskBuilderBatch]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: GetTaskBuilderBatchesBody,
    workspace_id: str,
    authorization: str,
) -> Optional[AITaskBuilderBatch]:
    """Get all AI Task Builder batches by workspace

     Get all AI Task Builder batches by workspace id

    Args:
        workspace_id (str):
        authorization (str):
        body (GetTaskBuilderBatchesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AITaskBuilderBatch
    """

    return sync_detailed(
        client=client,
        body=body,
        workspace_id=workspace_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GetTaskBuilderBatchesBody,
    workspace_id: str,
    authorization: str,
) -> Response[AITaskBuilderBatch]:
    """Get all AI Task Builder batches by workspace

     Get all AI Task Builder batches by workspace id

    Args:
        workspace_id (str):
        authorization (str):
        body (GetTaskBuilderBatchesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AITaskBuilderBatch]
    """

    kwargs = _get_kwargs(
        body=body,
        workspace_id=workspace_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GetTaskBuilderBatchesBody,
    workspace_id: str,
    authorization: str,
) -> Optional[AITaskBuilderBatch]:
    """Get all AI Task Builder batches by workspace

     Get all AI Task Builder batches by workspace id

    Args:
        workspace_id (str):
        authorization (str):
        body (GetTaskBuilderBatchesBody):

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
            workspace_id=workspace_id,
            authorization=authorization,
        )
    ).parsed
