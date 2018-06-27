class Signup():
	i = 0
	user_info = []
	def __init__(self, email, firstname, lastname, username, password):
		self.email = email
		self.firstname = firstname
		self.lastname = lastname
		self.username = username
		self.password = password
		self.i += 1
	def set_email(self):
		self.user_info.append({'email':self.email})
	def set_names(self):
		self.user_info[0].update({'names':self.firstname +" " +self.lastname})
	def set_username(self):
		self.user_info[0].update({'username':self.username})


class Login(Signup):
	
	

		

		
		





 #self.items.update({item_name: quantity})