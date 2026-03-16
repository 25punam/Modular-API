from rest_framework import serializers
from .models import VendorProductMapping


class VendorProductMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorProductMapping
        fields = '__all__'

    def validate(self, data):

        vendor = data.get('vendor')
        product = data.get('product')
        primary_mapping = data.get('primary_mapping')

        queryset = VendorProductMapping.objects.all()

        # Exclude current object during update
        if self.instance:
            queryset = queryset.exclude(id=self.instance.id)

        # Prevent duplicate vendor-product mapping
        if queryset.filter(vendor=vendor, product=product).exists():
            raise serializers.ValidationError(
                "Duplicate vendor-product mapping."
            )

        # Allow only one primary mapping per vendor
        if primary_mapping:
            if queryset.filter(vendor=vendor, primary_mapping=True).exists():
                raise serializers.ValidationError(
                    "Only one primary mapping per vendor allowed."
                )

        return data