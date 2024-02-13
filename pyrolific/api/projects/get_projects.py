from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from typing import Dict
from ...models.project_short_list_response import ProjectShortListResponse


def _get_kwargs(
    workspace_id: str,
    *,
    authorization: str,
) -> Dict[str, Any]:
    headers = {}
    headers["Authorization"] = authorization

    return {
        "method": "get",
        "url": "/api/v1/workspaces/{workspace_id}/projects/".format(
            workspace_id=workspace_id,
        ),
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ProjectShortListResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ProjectShortListResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ProjectShortListResponse]:
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
    authorization: str,
) -> Response[ProjectShortListResponse]:
    """Get all projects in a workspace

     Gets a list of all the projects within the workspace.

    Args:
        workspace_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectShortListResponse]
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
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    authorization: str,
) -> Optional[ProjectShortListResponse]:
    """Get all projects in a workspace

     Gets a list of all the projects within the workspace.

    Args:
        workspace_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectShortListResponse
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    authorization: str,
) -> Response[ProjectShortListResponse]:
    """Get all projects in a workspace

     Gets a list of all the projects within the workspace.

    Args:
        workspace_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectShortListResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    authorization: str,
) -> Optional[ProjectShortListResponse]:
    """Get all projects in a workspace

     Gets a list of all the projects within the workspace.

    Args:
        workspace_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectShortListResponse
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
