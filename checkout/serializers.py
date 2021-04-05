from rest_framework import serializers

from core.models import Product, Link, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'is_ambassador']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Link
        fields = '__all__'
