from decimal import Decimal
from .models import Menu, Category
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import bleach


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']


class MenuSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2)

    def validate(self, attrs):
        attrs = bleach.clean(attrs['title'])
        if (attrs["price"] < 2):
            raise serializers.ValidationError("Price mus be more than 2.0")
        return super().validate(attrs)

    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'stock',
                  'price_after_tax', 'category', 'category_id']

        extra_kwargs = {
            'title': {
                "validators": [
                    UniqueValidator(
                        queryset=Menu.objects.all()
                    )
                ]}
        }

    def calculate_tax(self, product: Menu):
        return product.price * Decimal(1.1)
