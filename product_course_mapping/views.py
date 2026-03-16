from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer


product_param = openapi.Parameter(
    'product_id',
    openapi.IN_QUERY,
    description="Filter by product ID",
    type=openapi.TYPE_INTEGER
)

course_param = openapi.Parameter(
    'course_id',
    openapi.IN_QUERY,
    description="Filter by course ID",
    type=openapi.TYPE_INTEGER
)


class ProductCourseMappingListCreateAPIView(APIView):

    @swagger_auto_schema(
        manual_parameters=[product_param, course_param],
        responses={200: ProductCourseMappingSerializer(many=True)}
    )
    def get(self, request):

        queryset = ProductCourseMapping.objects.all()

        product_id = request.GET.get("product_id")
        course_id = request.GET.get("course_id")

        if product_id:
            queryset = queryset.filter(product_id=product_id)

        if course_id:
            queryset = queryset.filter(course_id=course_id)

        serializer = ProductCourseMappingSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ProductCourseMappingSerializer,
        responses={201: ProductCourseMappingSerializer}
    )
    def post(self, request):

        serializer = ProductCourseMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductCourseMappingDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(ProductCourseMapping, pk=pk)

    def get(self, request, pk):

        mapping = self.get_object(pk)
        serializer = ProductCourseMappingSerializer(mapping)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ProductCourseMappingSerializer,
        responses={200: ProductCourseMappingSerializer}
    )
    def put(self, request, pk):

        mapping = self.get_object(pk)
        serializer = ProductCourseMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=ProductCourseMappingSerializer,
        responses={200: ProductCourseMappingSerializer}
    )
    def patch(self, request, pk):

        mapping = self.get_object(pk)

        serializer = ProductCourseMappingSerializer(
            mapping,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        mapping = self.get_object(pk)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)