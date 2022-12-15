from operator import is_
from django.forms import CharField
#from django.shortcuts import render

from rest_framework import viewsets
from api.models import Checkbox
from api.serializers import CheckboxSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import authentication, permissions


#class CheckboxViewSet(viewsets.ModelViewSet):
#    queryset = Checkbox.objects.all()
#    serializer_class = CheckboxSerializer

class UserList(APIView):
    #authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, req, format=None):
        users = [user.username for user in User.objects.all()]
        return Response(users)

@api_view(['GET'])
def checkbox_list(req):
    checkbox = Checkbox.objects.all()
    serializer = CheckboxSerializer(checkbox, many=True)  
    return Response(serializer.data)

@api_view(['GET'])
def checkbox_detail(req, pk):
    try:
        checkbox = Checkbox.objects.get(id=pk)
        serializer = CheckboxSerializer(checkbox)
    except CheckboxSerializer.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(['POST'])
def checkbox_create(req):
    serializer = CheckboxSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def checkbox_update(req, pk):
    try:
        checkbox = Checkbox.objects.get(id=pk)
        serializer = CheckboxSerializer(checkbox, data=req.data)
        if serializer.is_valid():
            serializer.save()
    except Checkbox.DoesNotExist:
        return Response (( f"error: Checkbox with id = {pk} is not found"), status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)                  

@api_view(['DELETE'])
def checkbox_delete(req, pk):
    checkbox = Checkbox.objects.get(id=pk)
    checkbox.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
