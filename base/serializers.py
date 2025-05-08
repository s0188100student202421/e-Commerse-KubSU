from rest_framework import serializers
from .models import Sneaker, Cart, CartItem, User

class SneakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sneaker
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    sneaker = SneakerSerializer(read_only=True)  # Включаем информацию о кроссовке
    sneaker_id = serializers.PrimaryKeyRelatedField(queryset=Sneaker.objects.all(), source='sneaker', write_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'sneaker', 'sneaker_id', 'size', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)  # Включаем элементы корзины
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')

    class Meta:
        model = Cart
        fields = ['id', 'user_id', 'total_amount', 'is_paid', 'items']