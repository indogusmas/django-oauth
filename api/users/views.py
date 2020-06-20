from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from  rest_framework.permissions import AllowAny
from  rest_framework import viewsets

import requests
from .serializers import CreateUserSerializers



CLIENT_ID = 'tHUZMfL418Ytz6ETOSjeYOqean8fAaJskklQKzc4'
CLIENT_SECRET = '5hprYeJdeMeW3gseY0sl6ZTyXtBEQxypqodLwoBAhTwKuYYR85p2uX2BmQ7Vs5vC1RnTjsgIdinP6JOefUOPtnrwAJcP5v5ji5olDkHtpuhMAOI8AM1yxfdLX9i53dly'

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''
    Register user to the server. Input should be in the format:
    {"username":"username","password":"2232432"}
    '''
    #Put the from  the request into serializers
    serializer = CreateUserSerializers(data=request.data) 
    #Validate the data
    if serializer.is_valid():
        #if it valid, save the data created user
        #This could be done differenctly
        serializer.save()
        r = requests.post('http://0.0.0.0:8000/o/token/', 
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        return Response(r.json())
    return Response(serializer.errors)


@api_view(['Post'])
@permission_classes([AllowAny])
def token(request):
    '''
    Get Tokens with username and password. Input should be in the format
    '''
    r = requests.post(
    'http://0.0.0.0:8000/o/token/', 
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())

        
@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Register user to the server
    '''
    r = request.post(
        'http://0.0.0.0:8000/o/token/',
        data = {
            'grant_type':'refresh_token',
            'refresh_token':request.data['refresh_token'],
            'client_id':CLIENT_ID,
            'clients_secret':CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    r = requests.post(
        'http://0.0.0.0:8000/o/revoke_token/', 
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return sucess message (would be empty otherwise) 
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)

