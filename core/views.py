from django.shortcuts import render
from rest_framework import generics, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Designer, BuyerRequest
from .serializers import (
    DesignerSerializer,
    DesignerRegisterSerializer,
    DesignerLoginSerializer,
    BuyerRequestSerializer,
)

class DesignerRegisterView(generics.CreateAPIView):
    queryset = Designer.objects.all()
    serializer_class = DesignerRegisterSerializer


class DesignerLoginView(APIView):
    def post(self, request):
        serializer = DesignerLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DesignerListView(generics.ListAPIView):
    queryset = Designer.objects.all()
    serializer_class = DesignerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['location', 'specialty', 'first_name', 'last_name', 'business_name']


class BuyerRequestCreateView(generics.CreateAPIView):
    queryset = BuyerRequest.objects.all()
    serializer_class = BuyerRequestSerializer
