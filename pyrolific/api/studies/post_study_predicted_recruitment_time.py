from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.study_predicted_recruitment_time_request import StudyPredictedRecruitmentTimeRequest
from ...models.study_predicted_recruitment_time_response import StudyPredictedRecruitmentTimeResponse
from ...types import Response


def _get_kwargs(
    *,
    body: StudyPredictedRecruitmentTimeRequest,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/studies/predicted-recruitment-time/",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[StudyPredictedRecruitmentTimeResponse]:
    if response.status_code == 200:
        response_200 = StudyPredictedRecruitmentTimeResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[StudyPredictedRecruitmentTimeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: StudyPredictedRecruitmentTimeRequest,
    authorization: str,
) -> Response[StudyPredictedRecruitmentTimeResponse]:
    """Show Study predicted recruitment time

     Returns the predicted recruitment time for a study that has not even been saved as a draft if it was
    published right now, based on a machine learning model.
    The recruitment time is the time from publish to the time when the final participant starts their
    submission.
    It does not account for the time to complete the submission.

    Args:
        authorization (str):
        body (StudyPredictedRecruitmentTimeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StudyPredictedRecruitmentTimeResponse]
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
    body: StudyPredictedRecruitmentTimeRequest,
    authorization: str,
) -> Optional[StudyPredictedRecruitmentTimeResponse]:
    """Show Study predicted recruitment time

     Returns the predicted recruitment time for a study that has not even been saved as a draft if it was
    published right now, based on a machine learning model.
    The recruitment time is the time from publish to the time when the final participant starts their
    submission.
    It does not account for the time to complete the submission.

    Args:
        authorization (str):
        body (StudyPredictedRecruitmentTimeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StudyPredictedRecruitmentTimeResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: StudyPredictedRecruitmentTimeRequest,
    authorization: str,
) -> Response[StudyPredictedRecruitmentTimeResponse]:
    """Show Study predicted recruitment time

     Returns the predicted recruitment time for a study that has not even been saved as a draft if it was
    published right now, based on a machine learning model.
    The recruitment time is the time from publish to the time when the final participant starts their
    submission.
    It does not account for the time to complete the submission.

    Args:
        authorization (str):
        body (StudyPredictedRecruitmentTimeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StudyPredictedRecruitmentTimeResponse]
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
    body: StudyPredictedRecruitmentTimeRequest,
    authorization: str,
) -> Optional[StudyPredictedRecruitmentTimeResponse]:
    """Show Study predicted recruitment time

     Returns the predicted recruitment time for a study that has not even been saved as a draft if it was
    published right now, based on a machine learning model.
    The recruitment time is the time from publish to the time when the final participant starts their
    submission.
    It does not account for the time to complete the submission.

    Args:
        authorization (str):
        body (StudyPredictedRecruitmentTimeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StudyPredictedRecruitmentTimeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
