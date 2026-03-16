from rest_framework import serializers
from .models import Certification

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

    def validate_code(self, value):
        if Certification.objects.filter(code=value).exists():
            raise serializers.ValidationError('Certification code must be unique.')
        return value
