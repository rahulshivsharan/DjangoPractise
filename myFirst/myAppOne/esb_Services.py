import requests as req
import json

ESB_ENDPOINT = 'http://localhost:8124'

# Get Customer Info API
def getCustomerInfo(customerId):
	payload = {'custid' : customerId}
	customerResponseObj = {}
	url = ESB_ENDPOINT + "/getCustInfo"
	try:
		r = req.get(url,params=payload);
		print (r.url)
		#print "the json response ",r.json()

		# the output will be {'customerinfo ' : {} }
		customerResponseObj = r.json()
	except  req.exceptions.RequestException as e:
		print e
		customerResponseObj = {"ErrorMsg" : "Error Connecting getCustInfo"}
	return customerResponseObj


# OTP Generation API
def generateOtp(emailId,mobileNo):
	url = ESB_ENDPOINT + "/sendOtp"
	OTP_GENERATED = False
	try:
		requestBody = {
			"user" : {
				"email" : emailId,
				"mobile" : mobileNo
			}
		}
		
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		
		res = req.post(url,data=json.dumps(requestBody),headers=headers)
		print "URL : ",res.url
		print "RESPONSE-CODE ",res.status_code

		if res.status_code == 200:
			OTP_GENERATED = True
	
	except  req.exceptions.RequestException as e:
		print e
		OTP_GENERATED = False

	return OTP_GENERATED


# Provision User
def provisionUser(customer_name,customer_emailId,customer_password,otp,customer_phoneNo):
	userProvisionStatus = False	
	url = ESB_ENDPOINT + "/provisionUser"
	responseObj = {}	
	try:
		requestBody = {
			"provisionaccount" : {
				"name" : customer_name,
				"email" : customer_emailId,
				"password" : customer_password,
				"otp" : otp,
				"phonenumber" : customer_phoneNo 
			}
		}
		
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		res = req.post(url,data=json.dumps(requestBody),headers=headers)
		
		print "URL : ",res.url
		print "RESPONSE-CODE ",res.status_code
		'''
		if (res.status_code != 200 and res.status_code != 202) :
			userProvisionStatus = True
			responseObj = res.json()
			
			responseError = responseObj["provisionaccountResponse"]["msg"]
			if "OTP" in responseError:
				print "INVALID OTP"
		
		else : 
			userProvisionStatus = False
		'''
			
		responseObj = res.json()

	except  req.exceptions.RequestException as e:
		print e
		userProvisionStatus = True
		responseObj = {
			"provisionaccountResponse" : {
				"msg" : "ESB INVOCATION ERROR",
				"code" : "400"
			}
		}

	return responseObj


# Create Lead API
def createLead(customerName,subject,email,phoneNumber,message):
	leadExists = False
	tenantExists = False
	contactExists = False
	errorResponse = ""
	requestAccepted=False
	responseMsg = ""
	url = ESB_ENDPOINT + "/crm/createLead"
	try:
	
		requestBody = { 
				"createlead" : {
					"last_name" : customerName,
					"subject" : subject,
					"email1" : email,
					"lead_source" : "Website",
					"phone_mobile" : phoneNumber,
					"message" : message
				}
		}
	
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	
	
		res = req.post(url,data=json.dumps(requestBody),headers=headers)
	
		print "POST URL ",res.url
		print "RESPONSE CONTENT ",res.json()
		responseJSON = res.json()
		
		if res.status_code == 201: 
			print ">>>>> ",responseJSON["blah"]["e"]
			requestAccepted = True
			responseMsg = "LEAD_CREATION_SUCCESS"
		else:
			errorResponse = responseJSON["ErrorResponse"]["msg"]
			print "Error Response : ",errorResponse
			requestAccepted = False

		if ((requestAccepted is False) and ("Lead" in errorResponse)):
			leadExists = True
			responseMsg = "LEAD_EXIST"

		elif ((requestAccepted is False) and  ("Contact" in errorResponse)):
			contactExists = True
			responseMsg = "CONTACT_EXIST"

		elif ((requestAccepted is False) and  ("Tenant" in errorResponse)):
			tenantExists = True	
			responseMsg = "TENANT_EXIST"
		
		elif (requestAccepted is False):
			responseMsg = "UNKNOWN_ERROR"
		else:
			pass
	
		print "RESPONSE CODE ",res.status_code
		print "LEAD EXISTS ",leadExists
		print "CONTACT Exists ",contactExists
		print "TENANT exists ",tenantExists

	except req.exceptions.RequestException as e:
		print e
		requestAccepted = False
		responseMsg = "ESB_SERVICE_ERROR"	
		
	return responseMsg


#print "Customer Info output ",getCustomerInfo(100)

#print "CREATE-LEAD ",createLead("Jimmy Page","This is dummy mail","Jimmy@ril.com","9867934525","From Jio Website")

#print "GENERATE OTP ",generateOtp("ninad.kulkarni@ril.com","9867934525")

#print "PROVISION USER ",provisionUser("Vishesh Parekh","vishesh.parekh@ril.com","vishesh234@1","1234","9867934525")
