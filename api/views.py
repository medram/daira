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


class SoknaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = SoknaRequest.objects.all()
	serializer_class = SoknaSerializer


class Mol7akaList(generics.ListAPIView):
	queryset = Mol7aka.objects.all()
	serializer_class = Mol7akaSerializer 


# @csrf_exempt
# @api_view(['GET', 'POST'])
# @parser_classes([MultiPartParser, FormParser])
# def create_sokna(req):
# 	if req.method == 'POST':
# 		# print(req._request.POST)
# 		# data = MultiPartParser().parse(req)
# 		serializer = SoknaSerializer(data=req._request.POST)

# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data, status=201)
# 		return JsonResponse(serializer.errors, status=400)


# def sokna_detail(req, id):
# 	try:
# 		sokna = SoknaRequest.objects.get(pk=id)
# 	except :
# 		return HttpResponse(status=400)

# 	serializer = SoknaSerializer(sokna)

# 	if req.method == 'GET':
# 		return JsonResponse(serializer.data, safe=False)

# 	return HttpResponse(status=400)