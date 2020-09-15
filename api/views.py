from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.decorators import parser_classes, api_view
from rest_framework import generics

from sokna.models import SoknaRequest
from daira.models import Mol7aka
from .serializers import SoknaSerializer, Mol7akaSerializer


class SoknaList(generics.ListCreateAPIView):
    queryset = SoknaRequest.objects.all()
    serializer_class = SoknaSerializer

    def get_queryset(self):
        queryset = SoknaRequest.objects.all()
        CIN = self.request.query_params.get('user', None)
        if CIN is not None:
            queryset = queryset.filter(CIN=CIN)
        else:
            return []
        return queryset


class SoknaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoknaRequest.objects.all()
    serializer_class = SoknaSerializer


class Mol7akaList(generics.ListAPIView):
    queryset = Mol7aka.objects.all()
    serializer_class = Mol7akaSerializer
