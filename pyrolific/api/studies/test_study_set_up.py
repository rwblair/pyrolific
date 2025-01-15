from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.test_study_set_up_response import TestStudySetUpResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: Any,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/study/{id}/test-study",
    }

    _body: Any
    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TestStudySetUpResponse]:
    if response.status_code == 200:
        response_200 = TestStudySetUpResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TestStudySetUpResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Any,
    authorization: str,
) -> Response[TestStudySetUpResponse]:
    """Create a test study

     Create and publish a test study from a draft study. This will allow you to test the study as a
    participant. (Only certain workspaces have access to this feature)

    Args:
        id (str):
        authorization (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestStudySetUpResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Any,
    authorization: str,
) -> Optional[TestStudySetUpResponse]:
    """Create a test study

     Create and publish a test study from a draft study. This will allow you to test the study as a
    participant. (Only certain workspaces have access to this feature)

    Args:
        id (str):
        authorization (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestStudySetUpResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Any,
    authorization: str,
) -> Response[TestStudySetUpResponse]:
    """Create a test study

     Create and publish a test study from a draft study. This will allow you to test the study as a
    participant. (Only certain workspaces have access to this feature)

    Args:
        id (str):
        authorization (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestStudySetUpResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Any,
    authorization: str,
) -> Optional[TestStudySetUpResponse]:
    """Create a test study

     Create and publish a test study from a draft study. This will allow you to test the study as a
    participant. (Only certain workspaces have access to this feature)

    Args:
        id (str):
        authorization (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestStudySetUpResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
