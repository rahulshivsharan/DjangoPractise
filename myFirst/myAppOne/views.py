from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
import datetime
import esb_Services as esb 
import json
import sys
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from captcha.image import ImageCaptcha
from MyModels import Student
from MyREST as rest


def getStudentList(request):
    studentObj = Student("Alajandro","Gonzales")
    student_ser = rest.StudentSerializer(studentObj)
    return HttpResponse(student_ser.data)	



def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hi(request):
	html = "<h3 style='color:blue'>This is 'Hi' from app 'AppOne'</h3>"
	return HttpResponse(html)

def getCustomerInfo(request):
	response_data = {}
	try:
		customerId = request.GET["custid"]
		
		if customerId and  customerId.strip():
			print "CUSTOMER ID IS ",customerId
			response_data = esb.getCustomerInfo(customerId)
			print "RESPONSE-ESB ",response_data	
		else:
			resonse_data = {"error" : {
				"msg" : "NO_CUSTOMER_ID_IN_URL"
			}}

	except Exception as e:
		print "UNEXPECTED ERROR"
		response_data = {"error" : {
			"msg" : "ERROR_INVOKING_ESB_SERVICE"
		}}

	return StreamingHttpResponse(json.dumps(response_data),content_type="application/json")


def createLead(request):
	response_Msg = ""
	try:
		last_name = request.POST["customer_name"]
		print "LAST_NAME >>>>  ",last_name
		subject = request.POST["subject"]
		email = request.POST["customer_email"]
		lead_source = "Website"
		phoneNumber = request.POST["customer_phoneNo"]
		message = request.POST["msg"]	

		response_Msg = esb.createLead(last_name,subject,email,phoneNumber,message)
		print "RESPONSE IN createLead ",response_Msg

	except Exception as e:
		print "Exception occured in esb service createLead"
		response_Msg = "ESB_SERVICE_ERROR"

	return HttpResponse(response_Msg,content_type="text/html")

def provisionUser(request):
	try:
		customerName = request.POST["provision_customerName"]
		customerEmail = request.POST["provision_customerEmail"]
		customerPassword = request.POST["provision_customerPassword"]
		customerOTP = request.POST["provision_customerOTP"]
		customerPhoneNo = request.POST["provision_customerPhoneNo"]

		response = esb.provisionUser(customerName,customerEmail,customerPassword,customerOTP,customerPhoneNo)
		
	except Exception as e:
		print "Exception is invoking ESB service 'provisionUser' ",e
		response = {
			"provisionaccountResponse" : {
				"code" : "400",
				"msg" : "ESB_SERVICE_ERROR"
			}
		} 

	return StreamingHttpResponse(json.dumps(response),content_type="application/json")


def myCaptchaLoader(request):
	to_json_response = dict()
	image = None
	try:
		print "IN CAPTCHA METHOD....."
            	to_json_response['status'] = 1
		image = ImageCaptcha(fonts=['Ubuntu-B.ttf', 'UbuntuMono-R.ttf'])
		
		image.write('1234','out.png')	
		print "CAPTCHA CREATED..."	
	except:	
		print "\nException OCCURED",sys.exc_info()[0]

	return StreamingHttpResponse(json.dumps(to_json_response),content_type="application/json")

# Create your views here.


