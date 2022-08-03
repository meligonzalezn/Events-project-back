import json
from rest_framework import viewsets
from .serializer import PaymentSerializer
from .models import Payment
from urllib.request import Request
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class PaymentViewSet(viewsets.ModelViewSet):

    model = Payment
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    @action(detail=True, methods=['post'])
    def is_enrolled(this, request: Request, pk: int) -> Response:
        """
          For user with ID_User=pk checks wheter or not is enrolled to activity with
          ID_Activity and ID_Event obtained from request.body.
        """

        try:
            data = json.loads(request.body)
            print(data)
            ID_User = pk
            ID_Event = int(json.loads(request.body)["ID_Event"])
            ID_Activity = int(json.loads(request.body)["ID_Activity"])
            print(ID_Event, ID_Activity, ID_User)
            resp = Payment.objects.get(
                ID_Activity=ID_Activity, ID_User=ID_User, ID_Event=ID_Event)

            return Response("Enrolled", status=status.HTTP_200_OK)
        except:
            return Response("Not Enrolled", status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def unenroll(this, request: Request, pk: int) -> Response:
        """
          For user with ID_User=pk cancels its enroll to activity with
          ID_Activity and ID_Event obtained from request.body.
        """

        try:
            data = json.loads(request.body)
            ID_User = pk
            ID_Event = int(data["ID_Event"])
            ID_Activity = int(data["ID_Activity"])
            resp = Payment.objects.filter(
                ID_Activity=ID_Activity, ID_User=ID_User, ID_Event=ID_Event).delete()

            return Response("Unenrolled", status=status.HTTP_200_OK)
        except:
            return Response("Not Unenrolled", status=status.HTTP_400_BAD_REQUEST)
