from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import UserSerializer


@api_view(http_method_names=['POST', ])
def post_user(request):
    user = request.user
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
