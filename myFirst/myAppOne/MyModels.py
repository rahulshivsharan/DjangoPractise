class Student :
	def __init__(self,first_name=None,last_name=None):
		self.first_name = first_name
		self.last_name = last_name

	def __str__(self):
		str = "The Full name of student is "+self.first_name+" "+self.last_name
		return str 

