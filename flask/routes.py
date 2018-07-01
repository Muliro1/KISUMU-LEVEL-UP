from flask import Flask, render_template, url_for, flash, redirect, request, session
from forms import LoginForm, RegistrationForm
import os



app = Flask(__name__)

app.config['SECRET_KEY'] = 'relapse92'


database = {}
user_id = len(database) + 1



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', database = database)

@app.route('/info')
def info():
	return render_template('about.html', title = 'About page')

@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		database.update({'username':form.username.data})
		flash('Account created for {}'.format(form.username.data))
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Registration Page', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit() and request.method ==  'POST':
		session['username'], session['email'] == form.username.data, form.email.data
		if form.username.data in database:
			flash('You are now logged in as {}'.format(form.username.data))
			return redirect(url_for('home'))
	return render_template('login.html', title = 'Login Page', form = form)

@app.route('/logout', methods = ['GET', 'POST'])
def logout():
	session.pop('username', None)
	session.pop('email', None)
	return redirect(url_for('login'))


if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug = True)
    
