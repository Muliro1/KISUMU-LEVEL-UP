from user import User
from db import user_info
import requests


class Signup():
	def Interface(self):
		command = input('type R to register, L to login and Q to quit: ')
		while command != 'Q':
			if command == 'R':
				self.register()
				break
			elif command == 'L':
				self.login()
				break
	def register(self):
	    email = input('please type in your email: ')
	    firstname = input('please type in your firstname: ')
	    lastname = input('please type in your lastname: ')
	    password = input('please type in your password: ')
	    new_user = User(email, firstname, lastname, password)
	    new_user.record_user()
	def login(self):
	    email = input('please type in your email: ')
	    password = input('please type in your password: ')
	    if email in user_info['email'] and password in user_info['password']:
	    	print('you are now logged in as {}'.format(user_info['names'][User.user_id]))
	    	return
	    print('you need to register before logging iin')
	





















	'''	self.user_info['email'].append(self.email)
	def set_password(self):
		self.user_info['password'].append(self.password)
	def set_name(self):
		self.user_info['names'].append(self.firstname + ' ' + self.lastname)
	
class LogIn(Signup):
	
	This class inherits from the signup class 
	and extends the functionality to include logging in
	
	def verify(self, email, password):
		if self.email in self.user_info['email'] and self.password in self.user_info['password']:
			return 'You are now logged in as {}'.format(self.user_info['names'][self.user_id])
		return('You need to register as a user before logging in')'''

 

