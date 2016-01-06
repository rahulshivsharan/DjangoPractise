from django.db import models

class Student(object) :

	def __init__(self,first_name,middle_name,last_name,subject_list=None):
		self.first_name = first_name
		self.last_name = last_name
		self.middle_name = middle_name
		if subject_list is None:
			self.subject_list = subject_list

class Subject(object) : 
	def __init__(self,name):
		self.name = name
