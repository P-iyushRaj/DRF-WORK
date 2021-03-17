from django.shortcuts import render
from .models import Total
from .serializer import GenerateRandomUserSerializer
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.views import APIView
from cronj2 import tasks
from rest_framework.response import Response
from rest_framework import status


class generate(APIView):

    def post(self, request,format=None):
        serializer = GenerateRandomUserSerializer(data = request.data)
        if serializer.is_valid():

            serializer.save()
            #breakpoint()

            tasks.create_random_user_accounts(int(request.data['total']))

            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

