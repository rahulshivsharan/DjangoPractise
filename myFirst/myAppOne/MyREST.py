from MyModels import Student
from rest_framework import serializers

class StudentSerialize(serializers.Serializer):
	firstName = serializers.CharField(max_length=200)
	lastName = serializers.CharField(max_length=200)
		
