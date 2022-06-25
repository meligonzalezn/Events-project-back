

from ast import Constant
import json
import os
from typing import Optional
from urllib.request import Request
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer


class UserFunctions(object):

    HAS_PERMS_RESPONSE = Response(
        "User has permissions", status=status.HTTP_200_OK)
    NOT_HAS_PERMS_RESPONSE = Response(
        "User doesn't has permissions", status=status.HTTP_401_UNAUTHORIZED)
    INTERNAL_ERROR_RESPONSE = Response(
        "Unexpected error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
    role : dict = {}

    def __init__(self) -> None or Response:
        """
            Try to initialize User Middleware\n
            If exist some error in execution, return an Internal error response.
        """
        try:
            filepath = os.path.join('static', 'front_url_by_role.json')
            filename = open(filepath, 'r')
            self.role: dict = json.loads(filename.read())
        except FileNotFoundError:
            response = Response(
                data='Static File not found',
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            return self.return_response(response)
        except:
            response = Response(
                data='Unexpected error',
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            return self.return_response(response)

    def has_perms(self, request: Request) -> Response:
        try:
          
            path: str = request.data["path"]
            for perm_url in self.role['exact_url']:
                if(path == perm_url):
                    return self.HAS_PERMS_RESPONSE
            # Check if url is access by any user.
            for perm_url in self.role['any_user']:
                if(path.startswith("/"+perm_url)):
                    return self.HAS_PERMS_RESPONSE
            
            # Check if User has Role cookie (He is logged.)
            userRole = cache.get('Role')
            if(userRole is None):
                return self.NOT_HAS_PERMS_RESPONSE

            role_url_perms = self.role[userRole]
            # Check if url match with an authorized url.
            for perm_url in role_url_perms:
                if(path.startswith("/"+perm_url)):
                    return self.HAS_PERMS_RESPONSE

            # If user don't have access.
            return Response(
                data="Role " + userRole + " don't authorized.",
                status=status.HTTP_401_UNAUTHORIZED)
        except KeyError:
            return Response(
                data="User role don't exist.",
                status=status.HTTP_400_BAD_REQUEST
            )
        except:
            return Response(
                data="Unexpected error",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
