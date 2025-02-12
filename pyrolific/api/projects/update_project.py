from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.project import Project
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: Project,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v1/projects/{project_id}/",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Project]:
    if response.status_code == 200:
        response_200 = Project.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Project]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: Project,
    authorization: str,
) -> Response[Project]:
    """Update a project

     Update a project's details

    Args:
        project_id (str):
        authorization (str):
        body (Project):  Example: {'id': '62fce6fff0a78eb4f3ebc09c', 'title': 'My project',
            'description': 'This project is for...', 'owner': '60a42f4c693c29420793cb73', 'users':
            [{'id': '60a42f4c693c29420793cb73', 'name': 'Joe Soap', 'email': 'joe.soap@gmail.com',
            'roles': ['PROJECT_EDITOR']}], 'workspace': '60a42f4c693c29420793cb73',
            'naivety_distribution_rate': 0.5}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Project]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: Project,
    authorization: str,
) -> Optional[Project]:
    """Update a project

     Update a project's details

    Args:
        project_id (str):
        authorization (str):
        body (Project):  Example: {'id': '62fce6fff0a78eb4f3ebc09c', 'title': 'My project',
            'description': 'This project is for...', 'owner': '60a42f4c693c29420793cb73', 'users':
            [{'id': '60a42f4c693c29420793cb73', 'name': 'Joe Soap', 'email': 'joe.soap@gmail.com',
            'roles': ['PROJECT_EDITOR']}], 'workspace': '60a42f4c693c29420793cb73',
            'naivety_distribution_rate': 0.5}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Project
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: Project,
    authorization: str,
) -> Response[Project]:
    """Update a project

     Update a project's details

    Args:
        project_id (str):
        authorization (str):
        body (Project):  Example: {'id': '62fce6fff0a78eb4f3ebc09c', 'title': 'My project',
            'description': 'This project is for...', 'owner': '60a42f4c693c29420793cb73', 'users':
            [{'id': '60a42f4c693c29420793cb73', 'name': 'Joe Soap', 'email': 'joe.soap@gmail.com',
            'roles': ['PROJECT_EDITOR']}], 'workspace': '60a42f4c693c29420793cb73',
            'naivety_distribution_rate': 0.5}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Project]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: Project,
    authorization: str,
) -> Optional[Project]:
    """Update a project

     Update a project's details

    Args:
        project_id (str):
        authorization (str):
        body (Project):  Example: {'id': '62fce6fff0a78eb4f3ebc09c', 'title': 'My project',
            'description': 'This project is for...', 'owner': '60a42f4c693c29420793cb73', 'users':
            [{'id': '60a42f4c693c29420793cb73', 'name': 'Joe Soap', 'email': 'joe.soap@gmail.com',
            'roles': ['PROJECT_EDITOR']}], 'workspace': '60a42f4c693c29420793cb73',
            'naivety_distribution_rate': 0.5}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Project
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
