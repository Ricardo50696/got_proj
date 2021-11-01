
from rest_framework.decorators import api_view, permission_classes, schema
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
@schema(None)
@permission_classes((permissions.AllowAny,))
def health_check(request):
    return Response('ok', status=status.HTTP_200_OK)