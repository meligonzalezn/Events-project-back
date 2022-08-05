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
from users.user_functions import UserFunctions

# Create your views here.


class LoginViewSet(viewsets.ViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()

    http_method_names = ['post']

    @action(detail=False, methods=['post'])
    def post(self, request: Request):
        """
            loggin function. HTTP_200 if it is loggin or could logging.
            Otherwise, HTTP_406
        """

        try:
            user: User = self.queryset.get(Email=request.data['Email'])
            if user.check_password(request.data['Password']):
                return Response({
                    "id": str(user.id),
                    "Name": user.Name,
                    "Role": user.Role,
                    "State": user.State,
                    "Media_file": user.Media_file
                }, status=status.HTTP_200_OK)
            else:
                return Response("Your username and password didn't match.", status=status.HTTP_406_NOT_ACCEPTABLE)
        except User.DoesNotExist:
            return Response("Your username and password didn't match.", status=status.HTTP_406_NOT_ACCEPTABLE)
