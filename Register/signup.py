class Signup():
	user_id = 0
	user_info = {'email':[], 'names':[], 'password':[]}
	def __init__(self, email, firstname, lastname, password):
		self.email = email
		self.firstname = firstname
		self.lastname = lastname
		self.password = password
		self.user_id += 1
	def set_email(self):
		self.user_info['email'].append(self.email)
	def set_password(self):
		self.user_info['password'].append(self.password)
	def set_name(self):
		self.user_info['names'].append(self.firstname + ' ' + self.lastname)
	
class LogIn(Signup):
	def verify(self, email, password):
		if self.email in self.user_info['email'] and self.password in self.user_info['password']:
			return 'You are now logged in as {}'.format(self.user_info['names'][self.user_id])

 


	
	

		

		
		





 #self.items.update({item_name: quantity})
