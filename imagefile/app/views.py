from django.shortcuts import render
from rest_framework import viewsets
from .models import Notes
from .serializer import NotesSerializer

class NotesView(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer