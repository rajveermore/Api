from django.contrib import admin

# Register your models here.
from .models import EmployeeDetailsModel

class EMployeeDetailsAdmin(admin.ModelAdmin):
    list_display=['Emp_Id','Emp_FName','Emp_LName','Emp_Dob','Emp_Add','Emp_Gender']


admin.site.register(EmployeeDetailsModel,EMployeeDetailsAdmin)