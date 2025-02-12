from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.participant_i_ds import ParticipantIDs
from ...models.submission_i_ds import SubmissionIDs
from ...types import Response


def _get_kwargs(
    *,
    body: Union["ParticipantIDs", "SubmissionIDs"],
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/submissions/bulk-approve/",
    }

    _body: dict[str, Any]
    if isinstance(body, ParticipantIDs):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[str]:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union["ParticipantIDs", "SubmissionIDs"],
    authorization: str,
) -> Response[str]:
    """Bulk approve submissions

     Bulk approve study submissions to pay participants after they have
    completed your survey or experiment. There are two variant payloads to
    this request.

    1. You can supply a Study ID, and a list of participant IDs, or
    2. You can provide a list of submission IDs

    We strongly recommend that you provide a list of submission IDs.
    These submissions do not need to be from the same study.

    Args:
        authorization (str):
        body (Union['ParticipantIDs', 'SubmissionIDs']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
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
    body: Union["ParticipantIDs", "SubmissionIDs"],
    authorization: str,
) -> Optional[str]:
    """Bulk approve submissions

     Bulk approve study submissions to pay participants after they have
    completed your survey or experiment. There are two variant payloads to
    this request.

    1. You can supply a Study ID, and a list of participant IDs, or
    2. You can provide a list of submission IDs

    We strongly recommend that you provide a list of submission IDs.
    These submissions do not need to be from the same study.

    Args:
        authorization (str):
        body (Union['ParticipantIDs', 'SubmissionIDs']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union["ParticipantIDs", "SubmissionIDs"],
    authorization: str,
) -> Response[str]:
    """Bulk approve submissions

     Bulk approve study submissions to pay participants after they have
    completed your survey or experiment. There are two variant payloads to
    this request.

    1. You can supply a Study ID, and a list of participant IDs, or
    2. You can provide a list of submission IDs

    We strongly recommend that you provide a list of submission IDs.
    These submissions do not need to be from the same study.

    Args:
        authorization (str):
        body (Union['ParticipantIDs', 'SubmissionIDs']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
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
    body: Union["ParticipantIDs", "SubmissionIDs"],
    authorization: str,
) -> Optional[str]:
    """Bulk approve submissions

     Bulk approve study submissions to pay participants after they have
    completed your survey or experiment. There are two variant payloads to
    this request.

    1. You can supply a Study ID, and a list of participant IDs, or
    2. You can provide a list of submission IDs

    We strongly recommend that you provide a list of submission IDs.
    These submissions do not need to be from the same study.

    Args:
        authorization (str):
        body (Union['ParticipantIDs', 'SubmissionIDs']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
