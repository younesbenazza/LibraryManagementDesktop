from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializer import SignUpSerializer, UserInfoSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


# register a user
@api_view(['POST'])
def register(request):
    # data variable get data of user with request
    data = request.data
    # here we put data in the serializer and the serializer we put it in user  
    user = SignUpSerializer(data=data)
    
    # in case the user send a valid information
    if user.is_valid():
        # in case we don't have a user with this username or email
        if not User.objects.filter(username=data['username']).exists(): 
            # create the user
            user = User.objects.create( 
                first_name = data['first_name'],
                last_name = data['last_name'],
                username = data['username'],
                email = data['email'],
                password = make_password(data['password'])
            )
            # return the message of succes!
            return Response(
                {'Response':'User has been created successfully!'}, 
                status=status.HTTP_201_CREATED
            )
        # in case we already have this user
        else:
            return Response(
                {'Error':'Failed Register, user already exist!'},
                status=status.HTTP_400_BAD_REQUEST
            )
    # in case the user don't send data
    else:
        return Response(user.errors)   

# get user information
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = UserInfoSerializer(request.user, many=False ) 
    return Response(user.data)

# updating user information
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user
    data = request.data

    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.username = data['username']
    user.email = data['email']
    
    if data['password'] != "":
        user.password = make_password(data['password'])
    
    user.save()
    serializer = UserInfoSerializer(user, many=False)
    return Response(serializer.data)