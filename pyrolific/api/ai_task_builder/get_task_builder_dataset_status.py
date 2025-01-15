from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_task_builder_dataset_status_response_200 import GetTaskBuilderDatasetStatusResponse200
from ...types import Response


def _get_kwargs(
    dataset_id: str,
    *,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/data-collection/datasets/{dataset_id}/status",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetTaskBuilderDatasetStatusResponse200]:
    if response.status_code == 200:
        response_200 = GetTaskBuilderDatasetStatusResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetTaskBuilderDatasetStatusResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    authorization: str,
) -> Response[GetTaskBuilderDatasetStatusResponse200]:
    """Get AI Task Builder Dataset Status

     Get status for AI Task Builder dataset.

    Args:
        dataset_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTaskBuilderDatasetStatusResponse200]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    authorization: str,
) -> Optional[GetTaskBuilderDatasetStatusResponse200]:
    """Get AI Task Builder Dataset Status

     Get status for AI Task Builder dataset.

    Args:
        dataset_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTaskBuilderDatasetStatusResponse200
    """

    return sync_detailed(
        dataset_id=dataset_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    authorization: str,
) -> Response[GetTaskBuilderDatasetStatusResponse200]:
    """Get AI Task Builder Dataset Status

     Get status for AI Task Builder dataset.

    Args:
        dataset_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTaskBuilderDatasetStatusResponse200]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    authorization: str,
) -> Optional[GetTaskBuilderDatasetStatusResponse200]:
    """Get AI Task Builder Dataset Status

     Get status for AI Task Builder dataset.

    Args:
        dataset_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTaskBuilderDatasetStatusResponse200
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
