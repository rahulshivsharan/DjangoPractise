from MyModels import Student
from MyModels import Subject
from rest_framework import serializers


class StudentSerialize(serializers.Serializer):
	first_name = serializers.CharField(max_length=200)
	middle_name = serializers.CharField(max_length=200)
	last_name = serializers.CharField(max_length=200)

class Student_Serializer(serializers.BaseSerializer):
	def to_representation(self,obj):
		return {
			"first_name" : obj.first_name,
			"last_name" : obj.last_name,
		}
