from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer


course_param = openapi.Parameter(
    'course_id',
    openapi.IN_QUERY,
    description="Filter by course ID",
    type=openapi.TYPE_INTEGER
)

certification_param = openapi.Parameter(
    'certification_id',
    openapi.IN_QUERY,
    description="Filter by certification ID",
    type=openapi.TYPE_INTEGER
)


class CourseCertificationMappingListCreateAPIView(APIView):

    @swagger_auto_schema(
        manual_parameters=[course_param, certification_param],
        responses={200: CourseCertificationMappingSerializer(many=True)}
    )
    def get(self, request):

        queryset = CourseCertificationMapping.objects.all()

        course_id = request.GET.get("course_id")
        certification_id = request.GET.get("certification_id")

        if course_id:
            queryset = queryset.filter(course_id=course_id)

        if certification_id:
            queryset = queryset.filter(certification_id=certification_id)

        serializer = CourseCertificationMappingSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CourseCertificationMappingSerializer,
        responses={201: CourseCertificationMappingSerializer}
    )
    def post(self, request):

        serializer = CourseCertificationMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseCertificationMappingDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(CourseCertificationMapping, pk=pk)

    def get(self, request, pk):

        mapping = self.get_object(pk)
        serializer = CourseCertificationMappingSerializer(mapping)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CourseCertificationMappingSerializer,
        responses={200: CourseCertificationMappingSerializer}
    )
    def put(self, request, pk):

        mapping = self.get_object(pk)
        serializer = CourseCertificationMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=CourseCertificationMappingSerializer,
        responses={200: CourseCertificationMappingSerializer}
    )
    def patch(self, request, pk):

        mapping = self.get_object(pk)

        serializer = CourseCertificationMappingSerializer(
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