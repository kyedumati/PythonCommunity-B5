from django.db import models
# Model

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=20)


# create table employee(emp_id int(20),emp_name varchar(20),,mobileno varchar(20))
