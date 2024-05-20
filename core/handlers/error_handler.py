from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def error_handler(exc: Exception, context: dict) -> Response:
    handlers = {
        'JWTException': _jwt_validation_error
    }

    exc_class = exc.__class__.__name__

    if exc_class in handlers:
        return handlers[exc_class](exc, context)

    return exception_handler(exc, context)


def _jwt_validation_error(exc: Exception, context: dict) -> Response:
    return Response({'details': 'Token is invalid or expired'}, status.HTTP_400_BAD_REQUEST)
