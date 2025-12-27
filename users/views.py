# users/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

@api_view(['POST'])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            },
            "token": str(refresh.access_token)
        })
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def register_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    refresh = RefreshToken.for_user(user)
    return Response({
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        },
        "token": str(refresh.access_token)
    })
