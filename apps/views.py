from django.http import JsonResponse
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.models import User
from apps.serializers import UserModelSerializers


# Create your views here.




@extend_schema(request=UserModelSerializers, responses=UserModelSerializers)
@extend_schema(tags=['auth'])
@api_view(['POST'])
def register_api_view(request):
    data = request.data
    serializer = UserModelSerializers(data=data)
    if serializer.is_valid():
        obj = serializer.save()
        return JsonResponse(UserModelSerializers(instance=obj).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@extend_schema(tags=['auth'])
@extend_schema(responses=UserModelSerializers, request=UserModelSerializers)
@api_view(['POST'])
def login_api_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if email and password:
        user = User.objects.filter(email=email).first()
        if (user and user.check_password(password)) or (user and user.password == password):
            token, created_at = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Email or password is required'}, status=status.HTTP_400_BAD_REQUEST)









