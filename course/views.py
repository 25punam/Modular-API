

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Course
from .serializers import CourseSerializer


# Query parameter documentation
is_active_param = openapi.Parameter(
    'is_active',
    openapi.IN_QUERY,
    description="Filter vendors by active status",
    type=openapi.TYPE_BOOLEAN
)


class CourseListCreateAPIView(APIView):

    def get(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CourseSerializer,
        responses={201: CourseSerializer}
    )
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Course, pk=pk)

    def get(self, request, pk):
        Course = self.get_object(pk)
        serializer = CourseSerializer(Course)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CourseSerializer,
        responses={200: CourseSerializer}
    )
    def put(self, request, pk):
        Course = self.get_object(pk)
        serializer = CourseSerializer(Course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=CourseSerializer,
        responses={200: CourseSerializer}
    )
    def patch(self, request, pk):
        Course = self.get_object(pk)
        serializer = CourseSerializer(Course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Course = self.get_object(pk)
        Course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)