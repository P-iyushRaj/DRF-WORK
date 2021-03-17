from rest_framework import serializers
from .models import Total

from django.core.validators import MinValueValidator,MaxValueValidator

class GenerateRandomUserSerializer(serializers.ModelSerializer):
  class Meta:
    total = serializers.IntegerField(
               validators=[
                 MinValueValidator(5),
                 MaxValueValidator(500)
            ]
    )
    model = Total
    fields = ['id','total']

