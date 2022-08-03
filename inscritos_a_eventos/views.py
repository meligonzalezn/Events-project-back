from datetime import datetime
from urllib.request import Request
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from inscritos_a_eventos.models import Enroll
from inscritos_a_eventos.serializer import EnrollSerializer
from static.http_error_response import HTTP_ERRORS
from django.core.cache import cache

from .models import Event, User
# Create your views here.
class EnrollViewSet(viewsets.ModelViewSet):
    model = Enroll
    serializer_class = EnrollSerializer
    queryset = Enroll.objects.all()

    http_method_names = ['get', 'post']
    
    @action(detail=False, methods=['post'])
    def enroll_user2event(self, request: Request):
        try:
            userId = cache.get('member_id')
            eventId = request.data["event_id"];
            user = User.objects.get(id=userId)
            event = Event.objects.get(id=eventId)
            new_enroll = Enroll.objects.create(ID_User=user, ID_Event=event, Date=datetime.now().strftime('%Y-%m-%d'))
            return HTTP_ERRORS.SuccessfulPetition("enrollment petition finished. Enroll_ID" + str(new_enroll.id))
        except KeyError:
            return HTTP_ERRORS.KEY_ERROR
        except User.DoesNotExist:
            return HTTP_ERRORS.OBJECT_NOT_FOUND
        # except:
        #     return HTTP_ERRORS.INTERNAL_ERROR

    @action(detail=True, methods=['get'])
    def get_participants(self, request: Request, pk: int):
        """
        Get all event participants using event_id
        """
        try:
            query = Enroll.objects.all().get(ID_Event=pk)
            serializer = self.serializer_class(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Enroll.DoesNotExist:
            return HTTP_ERRORS.OBJECT_NOT_FOUND
        except:
            return HTTP_ERRORS.INTERNAL_ERROR