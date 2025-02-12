from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.secret_list import SecretList
from ...types import UNSET, Response


def _get_kwargs(
    *,
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
        "url": "/api/v1/hooks/secrets/",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[SecretList]:
    if response.status_code == 200:
        response_200 = SecretList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[SecretList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    authorization: str,
) -> Response[SecretList]:
    """List all secrets

     A view of all the secrets for the workspaces you belong to.

    Args:
        workspace_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SecretList]
    """

    kwargs = _get_kwargs(
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
    workspace_id: str,
    authorization: str,
) -> Optional[SecretList]:
    """List all secrets

     A view of all the secrets for the workspaces you belong to.

    Args:
        workspace_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SecretList
    """

    return sync_detailed(
        client=client,
        workspace_id=workspace_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    authorization: str,
) -> Response[SecretList]:
    """List all secrets

     A view of all the secrets for the workspaces you belong to.

    Args:
        workspace_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SecretList]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    authorization: str,
) -> Optional[SecretList]:
    """List all secrets

     A view of all the secrets for the workspaces you belong to.

    Args:
        workspace_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SecretList
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_id=workspace_id,
            authorization=authorization,
        )
    ).parsed
