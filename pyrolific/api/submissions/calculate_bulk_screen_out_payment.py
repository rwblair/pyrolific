from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_screen_out_payment_calculator_request import BulkScreenOutPaymentCalculatorRequest
from ...models.calculate_bulk_screen_out_payment_response_200 import CalculateBulkScreenOutPaymentResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: BulkScreenOutPaymentCalculatorRequest,
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/studies/{id}/calculate-screen-out-payment/",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CalculateBulkScreenOutPaymentResponse200]:
    if response.status_code == 200:
        response_200 = CalculateBulkScreenOutPaymentResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CalculateBulkScreenOutPaymentResponse200]:
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
    body: BulkScreenOutPaymentCalculatorRequest,
    authorization: str,
) -> Response[CalculateBulkScreenOutPaymentResponse200]:
    """Calculate bulk screen payment amount

     Calculates the recommended and minimum screen out payment amounts for a given set of submission
    based on
    the time taken to complete the submissions. The bulk screen out endpoint will fail for the same
    submissions if
    the payment amount is less than the minimum screen out payment amount.

    Args:
        id (str):
        authorization (str):
        body (BulkScreenOutPaymentCalculatorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalculateBulkScreenOutPaymentResponse200]
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
    body: BulkScreenOutPaymentCalculatorRequest,
    authorization: str,
) -> Optional[CalculateBulkScreenOutPaymentResponse200]:
    """Calculate bulk screen payment amount

     Calculates the recommended and minimum screen out payment amounts for a given set of submission
    based on
    the time taken to complete the submissions. The bulk screen out endpoint will fail for the same
    submissions if
    the payment amount is less than the minimum screen out payment amount.

    Args:
        id (str):
        authorization (str):
        body (BulkScreenOutPaymentCalculatorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalculateBulkScreenOutPaymentResponse200
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
    body: BulkScreenOutPaymentCalculatorRequest,
    authorization: str,
) -> Response[CalculateBulkScreenOutPaymentResponse200]:
    """Calculate bulk screen payment amount

     Calculates the recommended and minimum screen out payment amounts for a given set of submission
    based on
    the time taken to complete the submissions. The bulk screen out endpoint will fail for the same
    submissions if
    the payment amount is less than the minimum screen out payment amount.

    Args:
        id (str):
        authorization (str):
        body (BulkScreenOutPaymentCalculatorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalculateBulkScreenOutPaymentResponse200]
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
    body: BulkScreenOutPaymentCalculatorRequest,
    authorization: str,
) -> Optional[CalculateBulkScreenOutPaymentResponse200]:
    """Calculate bulk screen payment amount

     Calculates the recommended and minimum screen out payment amounts for a given set of submission
    based on
    the time taken to complete the submissions. The bulk screen out endpoint will fail for the same
    submissions if
    the payment amount is less than the minimum screen out payment amount.

    Args:
        id (str):
        authorization (str):
        body (BulkScreenOutPaymentCalculatorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalculateBulkScreenOutPaymentResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
