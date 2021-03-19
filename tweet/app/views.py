from django.shortcuts import render
from .models import Tweet

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import TweetSerializer
from rest_framework.generics import ListAPIView
from .twitter import set_inactive, set_active, save_to_db

class TweetListS(ListAPIView):
    queryset = Tweet.objects.order_by('-published_date')[:5]
    serializer_class = TweetSerializer

def tweet_set_inactive(request, pk):
    set_inactive(pk)
    return Response({'msg':'tweet_set_inactive'}, status=status.HTTP_201_CREATED)


def tweet_set_active(request, pk):
    set_active(pk)
    return Response({'msg':'tweet_set_active'}, status=status.HTTP_201_CREATED)


def tweet_fetch(request):
    save_to_db()
    return Response({'msg':'tweet_fetch'}, status=status.HTTP_201_CREATED)

