from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_task_builder_free_text_input_instruction import AITaskBuilderFreeTextInputInstruction
from ...models.ai_task_builder_multiple_choice_instruction import AITaskBuilderMultipleChoiceInstruction
from ...models.update_task_builder_instructions_body_item import UpdateTaskBuilderInstructionsBodyItem
from ...types import Response


def _get_kwargs(
    batch_id: str,
    *,
    body: list["UpdateTaskBuilderInstructionsBodyItem"],
    authorization: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/data-collection/batches/{batch_id}/instructions",
    }

    _body = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _body.append(body_item)

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list[Union["AITaskBuilderFreeTextInputInstruction", "AITaskBuilderMultipleChoiceInstruction"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(
                data: object,
            ) -> Union["AITaskBuilderFreeTextInputInstruction", "AITaskBuilderMultipleChoiceInstruction"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ai_task_builder_instruction_type_0 = (
                        AITaskBuilderMultipleChoiceInstruction.from_dict(data)
                    )

                    return componentsschemas_ai_task_builder_instruction_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ai_task_builder_instruction_type_1 = AITaskBuilderFreeTextInputInstruction.from_dict(
                    data
                )

                return componentsschemas_ai_task_builder_instruction_type_1

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list[Union["AITaskBuilderFreeTextInputInstruction", "AITaskBuilderMultipleChoiceInstruction"]]]:
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
    body: list["UpdateTaskBuilderInstructionsBodyItem"],
    authorization: str,
) -> Response[list[Union["AITaskBuilderFreeTextInputInstruction", "AITaskBuilderMultipleChoiceInstruction"]]]:
    """Update Task Builder Instructions

     Updates the instructions for a task builder batch

    Args:
        batch_id (str):
        authorization (str):
        body (list['UpdateTaskBuilderInstructionsBodyItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Union['AITaskBuilderFreeTextInputInstruction', 'AITaskBuilderMultipleChoiceInstruction']]]
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


def sync(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    body: list["UpdateTaskBuilderInstructionsBodyItem"],
    authorization: str,
) -> Optional[list[Union["AITaskBuilderFreeTextInputInstruction", "AITaskBuilderMultipleChoiceInstruction"]]]:
    """Update Task Builder Instructions

     Updates the instructions for a task builder batch

    Args:
        batch_id (str):
        authorization (str):
        body (list['UpdateTaskBuilderInstructionsBodyItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Union['AITaskBuilderFreeTextInputInstruction', 'AITaskBuilderMultipleChoiceInstruction']]
    """

    return sync_detailed(
        batch_id=batch_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    body: list["UpdateTaskBuilderInstructionsBodyItem"],
    authorization: str,
) -> Response[list[Union["AITaskBuilderFreeTextInputInstruction", "AITaskBuilderMultipleChoiceInstruction"]]]:
    """Update Task Builder Instructions

     Updates the instructions for a task builder batch

    Args:
        batch_id (str):
        authorization (str):
        body (list['UpdateTaskBuilderInstructionsBodyItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Union['AITaskBuilderFreeTextInputInstruction', 'AITaskBuilderMultipleChoiceInstruction']]]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    batch_id: str,
    *,
    client: AuthenticatedClient,
    body: list["UpdateTaskBuilderInstructionsBodyItem"],
    authorization: str,
) -> Optional[list[Union["AITaskBuilderFreeTextInputInstruction", "AITaskBuilderMultipleChoiceInstruction"]]]:
    """Update Task Builder Instructions

     Updates the instructions for a task builder batch

    Args:
        batch_id (str):
        authorization (str):
        body (list['UpdateTaskBuilderInstructionsBodyItem']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Union['AITaskBuilderFreeTextInputInstruction', 'AITaskBuilderMultipleChoiceInstruction']]
    """

    return (
        await asyncio_detailed(
            batch_id=batch_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
