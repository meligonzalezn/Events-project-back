from django.shortcuts import render
import os
from types import MemberDescriptorType
from typing import List
from urllib.request import Request
import django
from django.http import HttpResponse
from rest_framework import viewsets
from users.serializer import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from users.models import User

# Create your views here.

class LoginViewSet(viewsets.ViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()

    http_method_names = ['post', 'delete']

    @action(detail=False, methods=['post'], url_path='in')
    def login(self, request: Request):
        """
        loggin function. HTTP_200 if it is loggin or could logging. otherwise, HTTP_406
        """
        if(request.session.get('member_id') is not None):
            return Response("You're logged in. ", status=status.HTTP_200_OK)
        # try:
        user = self.queryset.get(Email=request.data['Email'])
        if user.check_password(request.data['Password']):
            request.session['member_id'] = user.id
            request.session['Role'] = user.Role
            return Response("You're logged in.", status=status.HTTP_200_OK)
        else:
            return Response("Your username and password didn't match.", status=status.HTTP_406_NOT_ACCEPTABLE)
        # except:
        #     return Response("Your username and password didn't match.", status=status.HTTP_406_NOT_ACCEPTABLE)

            

    @action(detail=False, methods=['delete'], url_path="out")
    def loggout(self, request: Request):
        try:
            del request.session['member_id']
            del request.session['Role']
        except KeyError:
            pass
        return HttpResponse("You're logged out.")