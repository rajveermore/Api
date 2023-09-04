from django.shortcuts import render

# Create your views here.
from .models import EmployeeDetailsModel
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import EmployeeSer

class EmployeeView(APIView):
    def get(self,request):
        Emp_obj=EmployeeDetailsModel.objects.all()
        ser_obj=EmployeeSer(Emp_obj,many=True)
        return Response(ser_obj.data)