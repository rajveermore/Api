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
    
    def post(self,request):
        ser_obj=EmployeeSer(data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data,status=status.HTTP_201_CREATED)
        return Response(ser_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        emp_obj=EmployeeDetailsModel.objects.get(pk=pk)
        ser_obj=EmployeeSer(emp_obj,data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data,status=status.HTTP_201_CREATED)
        return Response(ser_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,pk):
        Emp_obj=EmployeeDetailsModel.objects.get(pk=pk)
        ser_obj=EmployeeSer(Emp_obj,data=request.data,partial=True)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data,status=status.HTTP_201_CREATED)
        return Response(ser_obj.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        Emp_obj=EmployeeDetailsModel.objects.get(pk=pk)
        ser_obj=EmployeeSer(Emp_obj)#to show which data get deleted
        Emp_obj.delete()
        return Response(ser_obj.data,status=status.HTTP_204_NO_CONTENT)
