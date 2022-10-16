from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class meta:
        model = Student
        field = '__all__'