from datetime import datetime
from urllib.request import Request
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Enroll
from .serializer import EnrollSerializer
from static.http_error_response import HTTP_ERRORS
from django.core.cache import cache

from events.models import Event
from users.models import User
# Create your views here.


class EnrollViewSet(viewsets.ModelViewSet):
    model = Enroll
    serializer_class = EnrollSerializer
    queryset = Enroll.objects.all()

    http_method_names = ['get', 'post', 'delete']

    @action(detail=False, methods=['post'])
    def enroll_user2event(self, request: Request):
        try:
            userId = cache.get('member_id')
            eventId = request.data["event_id"]
            user = User.objects.get(id=userId)
            event = Event.objects.get(id=eventId)
            new_enroll = Enroll.objects.create(
                ID_User=user, ID_Event=event, Date=datetime.now().strftime('%Y-%m-%d'))
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

    @action(detail=True, methods=['get'])
    def is_user_enrolled2event(self, request: Request, pk: int):
        """
        Get event_id and check if actual user is enrolled.
        """

        try:
            query = Enroll.objects.all().get(ID_Event=pk)
            serializer = self.serializer_class(query, many=False)
            return HTTP_ERRORS.SuccessfulPetition({"enrolled": True})
        except Enroll.DoesNotExist:
            return Response({"enrolled": False})
        except:
            return HTTP_ERRORS.INTERNAL_ERROR

    @action(detail=True, methods=['delete'])
    def unenrollment(self, request: Request, pk: int):
        """
        Remove an user from event
        """

        try:
            Enroll.objects.all().filter(ID_Event=pk).delete()

            return HTTP_ERRORS.SuccessfulPetition("Enrollment deleted")
        except Enroll.DoesNotExist:
            return HTTP_ERRORS.OBJECT_NOT_FOUND
        # except:
        #   return HTTP_ERRORS.INTERNAL_ERROR
