from urllib.request import Request
from rest_framework import viewsets
from .serializer import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from users.models import User
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # http_method_names = ['get', 'post', 'put']

    
    @action(detail=True, methods=['get'], url_path='watch')
    ## 
    def get_user(self: object, request: Request, pk: int):
        try:
            query = User.objects.all().get(pk=pk)
            serializer: UserSerializer = self.serializer_class(query, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("User doesn't exist", status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update')
    def actualizar(this, request, pk):
        # try:
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
        # except:
        #     return Response("Error", status.HTTP_500_INTERNAL_SERVER_ERROR)

    # @action(detail=True, methods={'post'})
    # def gl():
    @action(detail=True, methods=['get'], url_path='enable')
    def enable(this, _, pk):
        # try:
            user = User.objects.get(id=pk)
            user.State = not user.State
            user.save()
            
            return Response("User " + user.Name + " updated", status=status.HTTP_200_OK)
        # except:
        #     return Response("Error", status.HTTP_400_BAD_REQUEST)