from rest_framework import serializers
from .models import CourseCertificationMapping


class CourseCertificationMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseCertificationMapping
        fields = '__all__'

    def validate(self, data):

        course = data.get('course')
        certification = data.get('certification')
        primary_mapping = data.get('primary_mapping')

        queryset = CourseCertificationMapping.objects.all()

        # Exclude current instance during update
        if self.instance:
            queryset = queryset.exclude(id=self.instance.id)

        # Prevent duplicate course-certification mapping
        if queryset.filter(course=course, certification=certification).exists():
            raise serializers.ValidationError(
                "Duplicate course-certification mapping."
            )

        # Allow only one primary mapping per course
        if primary_mapping:
            if queryset.filter(course=course, primary_mapping=True).exists():
                raise serializers.ValidationError(
                    "Only one primary mapping per course allowed."
                )

        return data