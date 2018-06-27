class Signup():
	'''
	This class implements a user registration functionality 
	by using a dictionary and lists to store user information
	'''
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
	'''
	this class in herits from the Signup class
	and extends functionality by adding the ability
	to log in
	'''
	def verify(self, email, password):
		if self.email in self.user_info['email'] and self.password in self.user_info['password']:
			return 'You are now logged in as {}'.format(self.user_info['names'][self.user_id])
		return('You have to register in order to log in')


	
	

		

		
		





 #self.items.update({item_name: quantity})
