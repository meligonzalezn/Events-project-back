from rest_framework.response import Response
from rest_framework import status


class HTTP_ERRORS:
  KEY_ERROR = Response("id doesn't found", status=status.HTTP_400_BAD_REQUEST)
  OBJECT_NOT_FOUND = Response("Query don't found objects on DB", status=status.HTTP_200_OK)
  INTERNAL_ERROR = Response("Unexpected error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  def SuccessfulPetition(content):
    return Response(content, status=status.HTTP_200_OK)
