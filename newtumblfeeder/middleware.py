import logging

logger = logging.getLogger(__name__)


class LogErrorResponseMiddleware:
    """
    Middleware to log the response body of failed requests.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code >= 400:
            logger.error(
                f"Error response for {request.method} {request.path} "
                f"Status: {response.status_code}, Body: {response.content.decode('utf-8')}"
            )
        return response
