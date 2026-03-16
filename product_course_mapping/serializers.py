from rest_framework import serializers
from .models import ProductCourseMapping


class ProductCourseMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCourseMapping
        fields = '__all__'

    def validate(self, data):

        product = data.get('product')
        course = data.get('course')
        primary_mapping = data.get('primary_mapping')

        queryset = ProductCourseMapping.objects.all()

        if self.instance:
            queryset = queryset.exclude(id=self.instance.id)

        # Prevent duplicate mapping
        if queryset.filter(product=product, course=course).exists():
            raise serializers.ValidationError(
                "Duplicate product-course mapping."
            )

        # Only one primary mapping per product
        if primary_mapping:
            if queryset.filter(product=product, primary_mapping=True).exists():
                raise serializers.ValidationError(
                    "Only one primary mapping per product allowed."
                )

        return data