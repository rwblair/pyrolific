from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_filter_set import UpdateFilterSet
from ...models.update_filter_set_response_200 import UpdateFilterSetResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateFilterSet,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v1/filter-sets/{id}/",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UpdateFilterSetResponse200]:
    if response.status_code == 200:
        response_200 = UpdateFilterSetResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UpdateFilterSetResponse200]:
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
    body: UpdateFilterSet,
    authorization: str,
) -> Response[UpdateFilterSetResponse200]:
    """Update filter set

     Update the details of a filter set.

    Args:
        id (str):
        authorization (str):
        body (UpdateFilterSet):  Example: [{'name': 'Left-handed 30-somethings', 'filters':
            [{'id': 'handedness', 'selected_values': ['1']}, {'id': 'age', 'selected_range': {'lower':
            30, 'upper': 39}}]}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateFilterSetResponse200]
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
    body: UpdateFilterSet,
    authorization: str,
) -> Optional[UpdateFilterSetResponse200]:
    """Update filter set

     Update the details of a filter set.

    Args:
        id (str):
        authorization (str):
        body (UpdateFilterSet):  Example: [{'name': 'Left-handed 30-somethings', 'filters':
            [{'id': 'handedness', 'selected_values': ['1']}, {'id': 'age', 'selected_range': {'lower':
            30, 'upper': 39}}]}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateFilterSetResponse200
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
    body: UpdateFilterSet,
    authorization: str,
) -> Response[UpdateFilterSetResponse200]:
    """Update filter set

     Update the details of a filter set.

    Args:
        id (str):
        authorization (str):
        body (UpdateFilterSet):  Example: [{'name': 'Left-handed 30-somethings', 'filters':
            [{'id': 'handedness', 'selected_values': ['1']}, {'id': 'age', 'selected_range': {'lower':
            30, 'upper': 39}}]}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateFilterSetResponse200]
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
    body: UpdateFilterSet,
    authorization: str,
) -> Optional[UpdateFilterSetResponse200]:
    """Update filter set

     Update the details of a filter set.

    Args:
        id (str):
        authorization (str):
        body (UpdateFilterSet):  Example: [{'name': 'Left-handed 30-somethings', 'filters':
            [{'id': 'handedness', 'selected_values': ['1']}, {'id': 'age', 'selected_range': {'lower':
            30, 'upper': 39}}]}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateFilterSetResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
