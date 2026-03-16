from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

    def validate_code(self, value):
        if Vendor.objects.filter(code=value).exists():
            raise serializers.ValidationError('Vendor code must be unique.')
        return value
