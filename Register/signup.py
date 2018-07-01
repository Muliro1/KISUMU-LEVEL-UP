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
