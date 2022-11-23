from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from firstapp.serializers import EmployeeSerilizer

# Create your views here.
def welcome_view(request):
    return HttpResponse("<h2 style='color:red'>Welcome to Django</h2>")

@api_view(['POST'])
def add_employee(request):
    print(request.data)
    serilizer = EmployeeSerilizer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()  # it will either insert or update the record in the database(insert query)
        return Response(serilizer.data,status=HTTP_200_OK)
    return Response(serilizer.errors,status=HTTP_400_BAD_REQUEST)