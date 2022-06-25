from rest_framework.response import Response
from ..loggin_functions import is_logged
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.shortcuts import redirect


class LoggedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """df"""
        response = self.get_response(request)
        if(is_logged() or request.path.startswith("/login") or request.path.startswith("/docs") or request.path.startswith("/api_schema/")):
            return response
        else:
            response = Response(
                data='User not logged.',
                status=status.HTTP_401_UNAUTHORIZED
            )
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            response.render()
            return response
