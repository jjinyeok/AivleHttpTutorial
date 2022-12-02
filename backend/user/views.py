from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user.models import User
# Create your views here.

@api_view(['POST'])
def signup(request):
    user_id = request.data['user_id']
    password = request.data['password']
    
    user = User(user_id=user_id, password=password)
    user.save()

    return Response('aaa', status=status.HTTP_201_CREATED)


@api_view(['POST'])
def signin(request):
    id = request.data['id']
    password = request.data['password']
    try:
        user = User.objects.get(user_id=id, password=password)
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
