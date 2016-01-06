from django.http import HttpResponse
import datetime
from MyModels import Student
from MyModels import Subject
from . import MyREST as rest
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import pdb

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def say_hello(request):
	html = "<h2>This is my First \"Hello\" from Django App</h2>"
	return HttpResponse(html)

def getStudent(request):
    studentObj = Student(first_name="Alajandro",last_name="Gonzales")
    student_ser = rest.StudentSerialize(studentObj)
    json = JSONRenderer().render(student_ser.data)	
    return HttpResponse(json)	

def getStudentList(request):
    my_list = []
    my_list.append(Student(first_name="Alajandro",middle_name="Santana",last_name="Gonzales"))
    my_list.append(Student(first_name="Timothy",middle_name="Carlos",last_name="Robins"))
    my_list.append(Student(first_name="Nathan",middle_name="Nick",last_name="Mathews"))
    my_list.append(Student(first_name="John",middle_name="Nelson",last_name="Kennedy"))
    my_list.append(Student(first_name="Tom",middle_name="Kenny",last_name="Cruise"))
    my_list.append(Student(first_name="Jerry",middle_name="Sanvile",last_name="McGuire"))
    my_list.append(Student(first_name="Jason",middle_name="San",last_name="Statham"))
    
    student_list = []
    
    for student in my_list:
    	student_ser = rest.StudentSerialize(student)
    	student_list.append(student_ser.data.copy())

    json = JSONRenderer().render(student_list)
    return HttpResponse(json)

	
def get_student_list(request):
    
    my_list = []
    my_list.append(Student(first_name="Alajandro",middle_name="Santana",last_name="Gonzales"))
    my_list.append(Student(first_name="Timothy",middle_name="Carlos",last_name="Robins"))
    my_list.append(Student(first_name="Nathan",middle_name="Nick",last_name="Mathews"))
    my_list.append(Student(first_name="John",middle_name="Nelson",last_name="Kennedy"))


    subject_list = []
    subject_list.append(Subject(name="Computer Science"))		
    subject_list.append(Subject(name="Physics"))		
    subject_list.append(Subject(name="Chemistry"))

    my_list.append(Student(first_name="Jason",middle_name="San",last_name="Statham",subject_list=subject_list))
    my_list.append(Student(first_name="Tom",middle_name="Kenny",last_name="Cruise",subject_list=subject_list))
    my_list.append(Student(first_name="Jerry",middle_name="Sanvile",last_name="McGuire",subject_list=subject_list))

    student_list = []
    for student in my_list:
    	student_ser = rest.StudentSerialize(student)
    	student_list.append(student_ser.data.copy())


    json = JSONRenderer().render(student_list)
    return HttpResponse(json)

def get_student_list_2(request):
   
    my_list = []
    subject_list = []
    subject_list.append(Subject(name="Computer Science"))		
    subject_list.append(Subject(name="Physics"))		
    subject_list.append(Subject(name="Chemistry"))
		
    my_list.append(Student(first_name="Alajandro",middle_name="Santana",last_name="Gonzales",subject_list=None))
    my_list.append(Student(first_name="Timothy",middle_name="Carlos",last_name="Robins",subject_list=None))
    
    student_list = []
    for student in my_list:
    	student_ser = rest.Student_Serializer(student)
    	student_list.append(student_ser.data.copy())


    json = JSONRenderer().render(student_list)
    return HttpResponse(json)

@api_view(['GET'])
def server(request):
	return Response({
		"server" : {
			"name" : "My_Server",
			"id" : "sdc53rg343fsvcsw434r3rh5",
			"volumes" : [{
				"name" : "MyVolumes",
				"id" : "23f3tvw4f2wf3fvsc2"
			},{
				"name" : "MyWallet",
				"id" : "23f3tvw4f2wf3fvsc2"
			},{
				"name" : "DumpBuck",
				"id" : "23f3tvw4f2wf3fvsc2"
			}]
		}
	})
