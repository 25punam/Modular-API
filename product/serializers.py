from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_code(self, value):
        if Product.objects.filter(code=value).exists():
            raise serializers.ValidationError('Product code must be unique.')
        return value
