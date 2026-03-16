from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def validate_code(self, value):
        if Course.objects.filter(code=value).exists():
            raise serializers.ValidationError('Course code must be unique.')
        return value
