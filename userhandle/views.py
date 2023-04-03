from _testcapi import raise_exception
from django.shortcuts import render
from django.http import HttpResponse,Http404
from . models import  user
from . serializers import userserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
def welcome(request):
    return HttpResponse("Hey Welome to IPL Registration")

class RegisterView(APIView):
    serializer_class = userserializer

    def post(self,request):
        serializer = userserializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                'message':'Registered Sucessfully',
                'data':serializer.data
            }
            return Response(data=response,
                             status=status.HTTP_201_CREATED)

        return Response(data=response,status=status.HTTP_400_BAD_REQUEST)
