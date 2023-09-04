from rest_framework import serializers
from . models import EmployeeDetailsModel



class EmployeeSer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeDetailsModel
        fields="__all__"