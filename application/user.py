from db import user_info

class User():
	user_id = 0
	def __init__(self, email, firstname, lastname, password):
		self.email = email
		self.firstname = firstname
		self.lastname = lastname
		self.password = password
		self.user_id += 1
	def record_user(self):
		user_info['email'].append(self.email)
		user_info['password'].append(self.password)
		user_info['names'].append(self.firstname + ' ' + self.lastname)

        