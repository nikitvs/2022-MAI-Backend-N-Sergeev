from statistics import mode
import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Category

class CategorySerializer(serializers.Serializer):
    category_text = serializers.CharField(max_length=200)