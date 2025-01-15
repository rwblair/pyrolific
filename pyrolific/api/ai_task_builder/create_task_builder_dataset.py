from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_task_builder_dataset import AITaskBuilderDataset
from ...models.create_task_builder_dataset_body import CreateTaskBuilderDatasetBody
from ...types import Response


def _get_kwargs(
    *,
    body: CreateTaskBuilderDatasetBody,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/data-collection/datasets",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AITaskBuilderDataset]:
    if response.status_code == 201:
        response_201 = AITaskBuilderDataset.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AITaskBuilderDataset]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateTaskBuilderDatasetBody,
    authorization: str,
) -> Response[AITaskBuilderDataset]:
    """Create AI Task Builder Dataset

     Create a new AI Task Builder dataset.

    Args:
        authorization (str):
        body (CreateTaskBuilderDatasetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AITaskBuilderDataset]
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
    body: CreateTaskBuilderDatasetBody,
    authorization: str,
) -> Optional[AITaskBuilderDataset]:
    """Create AI Task Builder Dataset

     Create a new AI Task Builder dataset.

    Args:
        authorization (str):
        body (CreateTaskBuilderDatasetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AITaskBuilderDataset
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateTaskBuilderDatasetBody,
    authorization: str,
) -> Response[AITaskBuilderDataset]:
    """Create AI Task Builder Dataset

     Create a new AI Task Builder dataset.

    Args:
        authorization (str):
        body (CreateTaskBuilderDatasetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AITaskBuilderDataset]
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
    body: CreateTaskBuilderDatasetBody,
    authorization: str,
) -> Optional[AITaskBuilderDataset]:
    """Create AI Task Builder Dataset

     Create a new AI Task Builder dataset.

    Args:
        authorization (str):
        body (CreateTaskBuilderDatasetBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AITaskBuilderDataset
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
