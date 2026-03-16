from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Vendor
from .serializers import VendorSerializer


# Query parameter documentation
is_active_param = openapi.Parameter(
    'is_active',
    openapi.IN_QUERY,
    description="Filter vendors by active status",
    type=openapi.TYPE_BOOLEAN
)


class VendorListCreateAPIView(APIView):

    @swagger_auto_schema(
        manual_parameters=[is_active_param],
        responses={200: VendorSerializer(many=True)}
    )
    def get(self, request):
        queryset = Vendor.objects.all()

        # Query parameter filter
        is_active = request.GET.get('is_active')
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active)

        serializer = VendorSerializer(queryset, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body=VendorSerializer,
        responses={201: VendorSerializer}
    )
    def post(self, request):
        serializer = VendorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Vendor, pk=pk)


    @swagger_auto_schema(
        responses={200: VendorSerializer}
    )
    def get(self, request, pk):
        vendor = self.get_object(pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body=VendorSerializer,
        responses={200: VendorSerializer}
    )
    def put(self, request, pk):
        vendor = self.get_object(pk)

        serializer = VendorSerializer(vendor, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        request_body=VendorSerializer,
        responses={200: VendorSerializer}
    )
    def patch(self, request, pk):
        vendor = self.get_object(pk)

        serializer = VendorSerializer(
            vendor,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        responses={204: "Vendor deleted successfully"}
    )
    def delete(self, request, pk):
        vendor = self.get_object(pk)
        vendor.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)