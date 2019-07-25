from rest_framework import serializers
from .models import movieList

class movieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = movieList