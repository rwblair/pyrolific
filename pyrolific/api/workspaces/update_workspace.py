from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.workspace import Workspace
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    *,
    body: Workspace,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v1/workspaces/{workspace_id}/",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Workspace]:
    if response.status_code == 200:
        response_200 = Workspace.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Workspace]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: Workspace,
    authorization: str,
) -> Response[Workspace]:
    """Update a workspace

     Updates a workspace's details.

    Args:
        workspace_id (str):
        authorization (str):
        body (Workspace):  Example: {'id': '62fce6fff0a78eb4f3ebc09c', 'title': 'My workspace',
            'description': 'This workspace does...', 'owner': '60a42f4c693c29420793cb73', 'users':
            [{'id': '60a42f4c693c29420793cb73', 'name': 'Joe Soap', 'email': 'joe.soap@gmail.com',
            'roles': ['WORKSPACE_ADMIN']}], 'projects': [{'id': '60a42f4c693c29420793cb73'}],
            'wallet': '61a65c06b084910b3f0c00d6'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Workspace]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: Workspace,
    authorization: str,
) -> Optional[Workspace]:
    """Update a workspace

     Updates a workspace's details.

    Args:
        workspace_id (str):
        authorization (str):
        body (Workspace):  Example: {'id': '62fce6fff0a78eb4f3ebc09c', 'title': 'My workspace',
            'description': 'This workspace does...', 'owner': '60a42f4c693c29420793cb73', 'users':
            [{'id': '60a42f4c693c29420793cb73', 'name': 'Joe Soap', 'email': 'joe.soap@gmail.com',
            'roles': ['WORKSPACE_ADMIN']}], 'projects': [{'id': '60a42f4c693c29420793cb73'}],
            'wallet': '61a65c06b084910b3f0c00d6'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Workspace
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: Workspace,
    authorization: str,
) -> Response[Workspace]:
    """Update a workspace

     Updates a workspace's details.

    Args:
        workspace_id (str):
        authorization (str):
        body (Workspace):  Example: {'id': '62fce6fff0a78eb4f3ebc09c', 'title': 'My workspace',
            'description': 'This workspace does...', 'owner': '60a42f4c693c29420793cb73', 'users':
            [{'id': '60a42f4c693c29420793cb73', 'name': 'Joe Soap', 'email': 'joe.soap@gmail.com',
            'roles': ['WORKSPACE_ADMIN']}], 'projects': [{'id': '60a42f4c693c29420793cb73'}],
            'wallet': '61a65c06b084910b3f0c00d6'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Workspace]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: Workspace,
    authorization: str,
) -> Optional[Workspace]:
    """Update a workspace

     Updates a workspace's details.

    Args:
        workspace_id (str):
        authorization (str):
        body (Workspace):  Example: {'id': '62fce6fff0a78eb4f3ebc09c', 'title': 'My workspace',
            'description': 'This workspace does...', 'owner': '60a42f4c693c29420793cb73', 'users':
            [{'id': '60a42f4c693c29420793cb73', 'name': 'Joe Soap', 'email': 'joe.soap@gmail.com',
            'roles': ['WORKSPACE_ADMIN']}], 'projects': [{'id': '60a42f4c693c29420793cb73'}],
            'wallet': '61a65c06b084910b3f0c00d6'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Workspace
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
