from loguru import logger

from horde_sdk.exceptions import HordeException
from horde_sdk.generic_api.apimodels import RequestErrorResponse


class AIHordeServerException(HordeException):
    """Base exception for any case where the AI Horde API returns a `RequestErrorResponse` and it was not handled."""

    def __init__(
        self,
        *,
        message: str = "The AI Horde API returned an error response and it wasn't handled.",
        error_response: RequestErrorResponse,
    ) -> None:
        """Initialize the exception.

        Args:
            message: The message to display to the user.
            error_response: The error response returned by the AI Horde API.
        """
        logger.error(f"The AI Horde API returned an error response and it wasn't handled. Response: {error_response}")
        if error_response.object_data is not None:
            logger.error(f"Response object data: {error_response.object_data}")
        super().__init__(message)