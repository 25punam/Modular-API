

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Certification
from .serializers import CertificationSerializer


# Query parameter documentation
is_active_param = openapi.Parameter(
    'is_active',
    openapi.IN_QUERY,
    description="Filter vendors by active status",
    type=openapi.TYPE_BOOLEAN
)


class CertificationListCreateAPIView(APIView):

    def get(self, request):
        queryset = Certification.objects.all()
        serializer = CertificationSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CertificationSerializer,
        responses={201: CertificationSerializer}
    )
    def post(self, request):
        serializer = CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CertificationDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Certification, pk=pk)

    def get(self, request, pk):
        Certification = self.get_object(pk)
        serializer = CertificationSerializer(Certification)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CertificationSerializer,
        responses={200: CertificationSerializer}
    )
    def put(self, request, pk):
        Certification = self.get_object(pk)
        serializer = CertificationSerializer(Certification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=CertificationSerializer,
        responses={200: CertificationSerializer}
    )
    def patch(self, request, pk):
        Certification = self.get_object(pk)
        serializer = CertificationSerializer(Certification, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Certification = self.get_object(pk)
        Certification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)