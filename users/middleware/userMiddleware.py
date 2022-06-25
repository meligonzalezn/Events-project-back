from django.core.cache import cache
from urllib.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
import json
import os


class UserMiddleware(object):
    
    def return_response(self, response: Response) -> Response:
        """
            Function that should render middleware response.
        """
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        response.render()
        return response

    def __init__(self, get_response) -> None or Response:
        """
            Try to initialize User Middleware\n
            If exist some error in execution, return an Internal error response.
        """
        self.get_response = get_response
        try:
            filepath = os.path.join('static', 'back_url_by_role.json')
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

    def __call__(self, request: Request) -> Response:
        """
            Get an request and check if user has access to some content.\n
            User role perms are saved on /static/roles.json file.
        """
        
        response = self.get_response(request)        
        try:
            userRole = cache.get('Role')
            
            role_url_perms = self.role[userRole]
            
            ##Check if url is access by any user.
            for perm_url in self.role['any_user']:
                if(request.path.startswith("/"+perm_url)):
                    return response
            
            ### Check if url match with an authorized url.
            for perm_url in role_url_perms:
                if(request.path.startswith("/"+perm_url)):
                    return response
            
            ### If user don't have access.
            response = Response(
                data="Role " + userRole + " don't authorized.",
                status=status.HTTP_401_UNAUTHORIZED)
            return self.return_response(response)
        except KeyError:
            response = Response(
                data="Role user don't exist.",
                status=status.HTTP_400_BAD_REQUEST
            )
            return self.return_response(response)
        except:
            response = Response(
                data="Unexpected error",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            return self.return_response(response)
