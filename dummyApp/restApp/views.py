from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ServerView(viewsets.ViewSet):
    
    def list(self,request):
            response = None
            responseData = None
            try:
                print "In List Server Controller"
                responseData = {}
                responseData["servers"] = []
                responseData["servers"].append({"name" : "Dummy Server", "os" : "Unix"})
                responseData["servers"].append({"name" : "Production Server", "os" : "CenOS"})
                responseData["servers"].append({"name" : "Test Server", "os" : "Ubuntu"})
                responseData["servers"].append({"name" : "Deployment Server", "os" : "Ubuntu"})
                responseData["servers"].append({"name" : "Mail Server", "os" : "Windows"})
                response = Response(responseData)
                #raise MyExceptions("SERVER_CRASH")
            except MyExceptions as me:
                print me
                response = Response({"msg" : "Fatal Error Occured..."},status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print e
                response = Response({"msg" : "Not able to fetch Servers"},status=status.HTTP_400_BAD_REQUEST)
            return response

class MyExceptions(Exception):

	def __init__(self,value):
		self.value = value

	def __str__(self):
		return str(self.value)
