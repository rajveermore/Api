from django.db import models

# Create your models here.
class EmployeeDetailsModel(models.Model):
    Emp_Id=models.IntegerField(primary_key=True)
    Emp_FName=models.CharField(max_length=30)
    Emp_LName=models.CharField(max_length=30)
    Emp_Dob=models.DateField()
    Emp_Add=models.CharField(max_length=40)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Emp_Gender= models.CharField(max_length=1, choices=GENDER_CHOICES)
