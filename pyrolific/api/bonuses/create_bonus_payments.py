from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response
from ... import errors

from ...models.bulk_bonus import BulkBonus
from typing import Dict
from ...models.create_bonus_payments_json_body import CreateBonusPaymentsJsonBody


def _get_kwargs(
    *,
    json_body: CreateBonusPaymentsJsonBody,
    authorization: str,
) -> Dict[str, Any]:
    headers = {}
    headers["Authorization"] = authorization

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/api/v1/submissions/bonus-payments/",
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BulkBonus]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = BulkBonus.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BulkBonus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreateBonusPaymentsJsonBody,
    authorization: str,
) -> Response[BulkBonus]:
    r"""Set up bonuses

     Set up bonus payments to one or more participants/submissions in a study.

    You need the study id, the participant|submission ids and the request in CSV format.

    The csv_bonuses field needs to be structured in the format of either:

    - `<participant_id>,<amount>\n`.
    - `<submission_id>,<amount>\n`.

    Setting up a bonus payment does not actually pay them, to do so check [/api/v1/bulk-bonus-
    payments/{id}/pay/](#tag/Bonuses/paths/~1api~1v1~1bulk-bonus-payments~1%7Bid%7D~1pay~1/post)

    The submission and participant IDs need to have taken part in the study in order for this call to be
    successful.
    If not, you will get a \"400\" HTTP response back, which explains which IDs are incorrect.

    Args:
        authorization (str):
        json_body (CreateBonusPaymentsJsonBody):  Example: {'study_id':
            '60f6acb180a7b59ac0621f9e', 'csv_bonuses':
            '60ffe5c8371090c7041d43f8,4.25\n60ff44a1d00991f1dfe405d9,4.25'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkBonus]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: CreateBonusPaymentsJsonBody,
    authorization: str,
) -> Optional[BulkBonus]:
    r"""Set up bonuses

     Set up bonus payments to one or more participants/submissions in a study.

    You need the study id, the participant|submission ids and the request in CSV format.

    The csv_bonuses field needs to be structured in the format of either:

    - `<participant_id>,<amount>\n`.
    - `<submission_id>,<amount>\n`.

    Setting up a bonus payment does not actually pay them, to do so check [/api/v1/bulk-bonus-
    payments/{id}/pay/](#tag/Bonuses/paths/~1api~1v1~1bulk-bonus-payments~1%7Bid%7D~1pay~1/post)

    The submission and participant IDs need to have taken part in the study in order for this call to be
    successful.
    If not, you will get a \"400\" HTTP response back, which explains which IDs are incorrect.

    Args:
        authorization (str):
        json_body (CreateBonusPaymentsJsonBody):  Example: {'study_id':
            '60f6acb180a7b59ac0621f9e', 'csv_bonuses':
            '60ffe5c8371090c7041d43f8,4.25\n60ff44a1d00991f1dfe405d9,4.25'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkBonus
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreateBonusPaymentsJsonBody,
    authorization: str,
) -> Response[BulkBonus]:
    r"""Set up bonuses

     Set up bonus payments to one or more participants/submissions in a study.

    You need the study id, the participant|submission ids and the request in CSV format.

    The csv_bonuses field needs to be structured in the format of either:

    - `<participant_id>,<amount>\n`.
    - `<submission_id>,<amount>\n`.

    Setting up a bonus payment does not actually pay them, to do so check [/api/v1/bulk-bonus-
    payments/{id}/pay/](#tag/Bonuses/paths/~1api~1v1~1bulk-bonus-payments~1%7Bid%7D~1pay~1/post)

    The submission and participant IDs need to have taken part in the study in order for this call to be
    successful.
    If not, you will get a \"400\" HTTP response back, which explains which IDs are incorrect.

    Args:
        authorization (str):
        json_body (CreateBonusPaymentsJsonBody):  Example: {'study_id':
            '60f6acb180a7b59ac0621f9e', 'csv_bonuses':
            '60ffe5c8371090c7041d43f8,4.25\n60ff44a1d00991f1dfe405d9,4.25'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkBonus]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: CreateBonusPaymentsJsonBody,
    authorization: str,
) -> Optional[BulkBonus]:
    r"""Set up bonuses

     Set up bonus payments to one or more participants/submissions in a study.

    You need the study id, the participant|submission ids and the request in CSV format.

    The csv_bonuses field needs to be structured in the format of either:

    - `<participant_id>,<amount>\n`.
    - `<submission_id>,<amount>\n`.

    Setting up a bonus payment does not actually pay them, to do so check [/api/v1/bulk-bonus-
    payments/{id}/pay/](#tag/Bonuses/paths/~1api~1v1~1bulk-bonus-payments~1%7Bid%7D~1pay~1/post)

    The submission and participant IDs need to have taken part in the study in order for this call to be
    successful.
    If not, you will get a \"400\" HTTP response back, which explains which IDs are incorrect.

    Args:
        authorization (str):
        json_body (CreateBonusPaymentsJsonBody):  Example: {'study_id':
            '60f6acb180a7b59ac0621f9e', 'csv_bonuses':
            '60ffe5c8371090c7041d43f8,4.25\n60ff44a1d00991f1dfe405d9,4.25'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkBonus
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            authorization=authorization,
        )
    ).parsed
