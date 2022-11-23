from rest_framework import serializers
from firstapp.models import Employee

class EmployeeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('emp_id','emp_name','mobile_no')
