from rest_framework import serializers
from .models import Sneaker

class SneakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sneaker
        fields = [
            'id',
            'name',
            'price',
            'category',
            'surface_type',
            'composition',
            'description',
            'gender',
            'sizes'
        ]