from django.shortcuts import render
from .models import Tweet

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import TweetSerializer
from rest_framework.generics import ListAPIView
from .twitter import set_inactive, set_active, save_to_db

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from time import sleep


class TweetListS(ListAPIView):
    queryset = Tweet.objects.order_by('-published_date')
    serializer_class = TweetSerializer



from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from time import sleep
from rest_framework.response import Response
from rest_framework import status

def tweet_set_inactive(request, pk):
    set_inactive(pk)
    return Response({'msg':'tweet_set_inactive'}, status=status.HTTP_201_CREATED)


def tweet_set_active(request, pk):
    set_active(pk)
    return Response({'msg':'tweet_set_active'}, status=status.HTTP_201_CREATED)


@api_view(('GET',))
@renderer_classes(( JSONRenderer,))
def tweet_fetch(request):
    save_to_db()
    return Response({'msg':'tweet fetched'}, status=status.HTTP_201_CREATED)


