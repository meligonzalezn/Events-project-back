from rest_framework import viewsets
from .models import News
from rest_framework.response import Response
from .serializer import NewsSerializer


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
"""
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

"""