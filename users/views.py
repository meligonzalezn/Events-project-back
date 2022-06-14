import os
from types import MemberDescriptorType
from typing import List
from urllib.request import Request
import django
from django.http import HttpResponse
from rest_framework import viewsets
from .serializer import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from login.loggin_functions import is_logged
import json

filepath = os.path.join('static', 'roles.json')
filename = open(filepath, 'r')
role: dict = json.loads(filename.read())



class UserViewSet(viewsets.ModelViewSet):

    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()

    http_method_names = ['get', 'post', 'put']
    
    def authentificate(self, request: Request, permissions: List[str]):
        """
        Check if actual session is valid and has access to required functionalities.\n
        @return [response: Response, is_authentificated: bool]
        """
        if(not is_logged(request)):
            return [Response("Not logged.", status=status.HTTP_406_NOT_ACCEPTABLE), False]
                
        for perm in permissions:
            if(not (perm in role[request.session['Role']])):
                return [Response("Not authorized", status=status.HTTP_401_UNAUTHORIZED), False]
        
        return [None, True]

    @action(detail=True, methods=['get'])
    def get_user(this, request: Request, pk: int):
        """
        return a all users on DB.\n
        @return users: List[Object]
        """
        [res, has_perms] = this.authentificate(request, ['user_watch'])
        if not has_perms:
            return res
            
            
        try:
            query = User.objects.all().get(pk=pk)
            serializer: UserSerializer = this.serializer_class(query, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("User doesn't exist", status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'])
    def actualizar(this, request, pk):
        
        [res, has_perms] = this.authentificate(request, ['user_edit'])
        if not has_perms:
            return res
        
        try:
            user = User.objects.get(id=pk)

            if('Name' in request.data):
                user.Name = request.data['Name']
            if('State' in request.data):
                user.State = request.data['State']
            if('Role' in request.data):
                user.Role = request.data['Role']
            if('Email' in request.data):
                user.Email = request.data['Email']
            if('Phone' in request.data):
                user.Phone = request.data['Phone']
            if('Password' in request.data):
                user.Password = request.data['Password']
            user.save()

            return Response("User " + user.Name + " updated", status=status.HTTP_200_OK)
        except:
            return Response("Error", status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['get'], url_path='enable')
    def enable(this, request, pk):
        """
        Switch user state.
        """
        [res, has_perms] = this.authentificate(request, ['user_edit'])
        print(res, has_perms)
        if not has_perms:
            return res
        
        try:
            user = User.objects.get(id=pk)
            user.State = not user.State
            user.save()

            return Response("User " + user.Name + " updated", status=status.HTTP_200_OK)
        except:
            return Response("Error", status.HTTP_404_NOT_FOUND)
