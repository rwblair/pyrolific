from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.setup_task_builder_batch_body import SetupTaskBuilderBatchBody
from ...types import Response


def _get_kwargs(
    batch_id: str,
    *,
    body: SetupTaskBuilderBatchBody,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/data-collection/batches/{batch_id}/setup",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 202:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    body: SetupTaskBuilderBatchBody,
    authorization: str,
) -> Response[Any]:
    """Setup AI Task Builder batch

     The setup process creates all of the **tasks** within the batch according to your configuration.
    The dataset referenced in the requesty body must be in a **READY** status before the setup process
    can be initiated.

    Upon successful invocation, the setup process will begin asynchronously, and the batch will be set
    to a **PROCESSING** status.

    To retrieve the status of the setup, call the `GET /api/v1/data-
    collection/batches/{batch_id}/status` endpoint.
    The setup is complete once the batch status changes to **READY**.

    Args:
        batch_id (str):
        authorization (str):
        body (SetupTaskBuilderBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    body: SetupTaskBuilderBatchBody,
    authorization: str,
) -> Response[Any]:
    """Setup AI Task Builder batch

     The setup process creates all of the **tasks** within the batch according to your configuration.
    The dataset referenced in the requesty body must be in a **READY** status before the setup process
    can be initiated.

    Upon successful invocation, the setup process will begin asynchronously, and the batch will be set
    to a **PROCESSING** status.

    To retrieve the status of the setup, call the `GET /api/v1/data-
    collection/batches/{batch_id}/status` endpoint.
    The setup is complete once the batch status changes to **READY**.

    Args:
        batch_id (str):
        authorization (str):
        body (SetupTaskBuilderBatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
