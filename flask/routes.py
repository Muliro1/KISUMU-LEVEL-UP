from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm
from db import dummy_users

app = Flask(__name__)

app.config['SECRET_KEY'] = 'relapse92'

dummy_data = [{
	'author': 'Michael Muliro',
	'title': 'First post',
	'info': 'This is the first post',
	'date_posted': 'une 27th 2018'
},
{
	'author': 'Hayley Williams',
	'title': 'First post',
	'info': 'This is the second post',
	'date_posted': 'une 27th 2018'
}]



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', dummy_data = dummy_data)

@app.route('/info')
def info():
	return render_template('about.html', title = 'About page')

@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash('Account created for {}'.format(form.username.data))
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Registration Page', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data in dummy_users['emails'] and form.password.data in dummy_users['passwords']:
			flash('You are now logged in as {}'.format(dummy_users['usernames']))
			return redirect(url_for('home'))
	return render_template('login.html', title = 'Login Page', form = form)

if __name__ == '__main__':
    app.run(debug=True)
