from django.shortcuts import render

# Create your views here.
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student

#django-filter for specific class view
from django_filters.rest_framework import DjangoFilterBackend

class StudentList(ListAPIView):
    #filtering
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    #filterset_fields =['city']
    filterset_fields =['city']

    