from django.shortcuts import render
from urllib.request import Request
from django.http import HttpResponse
from rest_framework import viewsets
from .loggin_functions import is_logged
from users.serializer import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from django.core.cache import cache
from users.user_functions import UserFunctions

# Create your views here.

class LoginViewSet(viewsets.ViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()

    http_method_names = ['get','post', 'delete']
    
    
    @action(detail=False, methods=['get'])
    def get(self, request: Request):
        """
            Check if an user is currently logged.\n
            True if that's it, False otherwise
        """
        try:
            if is_logged():
                return Response("You're logged in. ", status=status.HTTP_200_OK)
            else:
                return Response("You're not logged", status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response("Unexpected error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=False, methods=['post'])
    def has_access(self, request: Request) -> Response:
        """
            Check if an user has permissions to access to a functionality.
        """
        # return Response("Siempre es true", status=status.HTTP_200_OK)
        userFunctions = UserFunctions
        userFunctions.__init__(userFunctions)
        return UserFunctions.has_perms(userFunctions, request)
        
        
    

    @action(detail=False, methods=['post'])
    def post(self, request: Request):
        """
            loggin function. HTTP_200 if it is loggin or could logging.
            Otherwise, HTTP_406
        """
        if(cache.get('member_id') is not None):
            return Response("You're logged in. ", status=status.HTTP_200_OK)

        try:
            user = self.queryset.get(Email=request.data['Email'])
            if user.check_password(request.data['Password']):
                cache.set('member_id', user.id)
                cache.set('Role', user.Role)
                return Response("You're logged in.", status=status.HTTP_200_OK)
            else:
                return Response("Your username and password didn't match.", status=status.HTTP_406_NOT_ACCEPTABLE)
        except User.DoesNotExist:
            return Response("Your username and password didn't match.", status=status.HTTP_406_NOT_ACCEPTABLE)
        except:
            return Response("Internal server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            
    @action(detail=False, methods=['delete'])
    def delete(self, request: Request):
        """
            Remove cookies information from cache.
        """
        try:
            cache.delete('member_id')
            cache.delete('Role')
            cache.clear()
            cache.set('member_id', None)
            cache.set('Role', None)
        except KeyError:
            pass
        return Response("You're logged out.", status=status.HTTP_200_OK)