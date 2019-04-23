from flask import render_template, request
from datetime import datetime
from datetime import timedelta
from fitness_fox import app
from flask_sqlalchemy import SQLAlchemy
from fitness_fox.models import Workout
from fitness_fox.models import User
from fitness_fox import db
from sqlalchemy import and_, func
import sqlalchemy as sa
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, request

log = {"username" : ""}

@app.route('/AddActivity.html')
def setValue():
	if log["username"] == "":
		return redirect(url_for('getlogin'))
	return render_template('AddActivity3.html')

@app.route('/login.html/', methods=['GET'])
def getlogin():
	return render_template('login.html')

@app.route('/login.html/', methods=['POST'])
def postlogin():
	
	username = request.form['username']
	password = request.form['password']
	
	error = None
	if(username == 'admin@tamu.edu' and password == 'password'):
		log["username"] = username
		return redirect(url_for('getmanagerView'))

	userDb = User.query.filter_by(emailDb=username).first()
	print (userDb)
	if userDb == None or userDb.passwordDb != password:
		error = 'Invalid Credentials. Please try again.'
		return render_template('login.html', error = error)
	log["username"] = username
	print (log["username"])
	return redirect(url_for('view'))

@app.route('/register.html/', methods=['GET'])
def getRegister():
	return render_template('register.html')

@app.route('/register.html/', methods=['POST'])
def postRegister():

	error = None
	firstname = request.form['firstname']
	lastname = request.form['lastname']
	user = request.form['user']
	password = request.form['password']

	userDb = User.query.filter_by(emailDb=user).first()
	print (userDb)

	if userDb is  None:
		user = User(firstname, lastname, user, password)
		db.session.add(user)
		db.session.commit()
	else:
		error = 'User already exits. Please try again.'
		return render_template('register.html', error = error)

	return redirect(url_for('successRegistationPage'))

@app.route('/Logout.html/', methods=['GET'])
def logout():
	log["username"] = ""
	return render_template('Logout.html')

@app.route('/AdminLogout.html/', methods=['GET'])
def adminLogout():
	log["username"] = ""
	return render_template('AdminLogout.html')

@app.route('/AddActivity.html', methods=['POST'])
def getValue():
	if log["username"] == "":
		return redirect(url_for('getlogin'))

	activity_date = request.form['activity_date']
	activity_time = request.form['activity_time']
	activity_name = request.form['activity']
	activity_mins = request.form['mins']
	activity_date = datetime.strptime(activity_date, '%Y-%m-%d').date()
	activity_time = datetime.strptime(activity_time, '%H:%M').time()
	user_id = User.query.filter_by(emailDb=log["username"]).first().id
	workout = Workout(activity_name, activity_date, activity_time, activity_mins, user_id)
	db.session.add(workout)
	db.session.commit()
	return render_template('Success1.html')

@app.route('/')
@app.route('/homepage.html')
def homepage():
	myUser = log["username"]
	return render_template('homepage.html', user = myUser)

@app.route('/Chart.html')
def view():
	if log["username"] == "":
		return redirect(url_for('getlogin'))
	from_date = datetime.now() - timedelta(days=7)
	to_date = datetime.now()
	user_Id = User.query.filter_by(emailDb=log["username"]).first().id
	weekData = db.session.query(Workout.dateDb, db.func.sum(Workout.minutesDb).label("minutesDb")).filter(Workout.dateDb <= to_date).filter(Workout.dateDb >= from_date).filter(Workout.user_id == user_Id).group_by(func.date(Workout.dateDb)).order_by(Workout.dateDb).all()
	labels = []
	values = []
	for c in weekData:
	   values.append(c.minutesDb)
	   labels.append(c.dateDb.strftime("%Y-%m-%d"))
	return render_template('Chart.html', max=90, values=values, labels=labels)

@app.route('/Success.html')
def successPage():
	if log["username"] == "":
		return redirect(url_for('getlogin'))
	return render_template('Success1.html')

@app.route('/SuccessRegistration.html')
def successRegistationPage():
	return render_template('SuccessRegistration.html')

@app.route('/ManagerView.html/', methods=['GET'])
def getmanagerView():
	if log["username"] == "":
		return redirect(url_for('getlogin'))
	return render_template('Manager_view.html')

@app.route('/ManagerView.html/', methods=['POST'])
def postmanagerView():
	if log["username"] == "":
		return redirect(url_for('getlogin'))
	
	from_date = request.form['from_date']
	from_date = datetime.strptime(from_date, '%Y-%m-%d').date()
	to_date = request.form['to_date']
	to_date = datetime.strptime(to_date, '%Y-%m-%d').date()
	
	#user = db.session.query(User, Workout).join(Workout).filter(Workout.dateDb <= to_date).filter(Workout.dateDb >= from_date).order_by(Workout.dateDb).all()
	user = db.session.query(Workout, User).join(Workout).filter(Workout.dateDb <= to_date).filter(Workout.dateDb >= from_date).order_by(Workout.dateDb).all()
	for row in user:
		print (row.Workout.minutesDb)
	#user = db.session.query(User).all()
	#user = db.session.query(User).join(Workout).all()
	
	return render_template('Manager_view.html', myUser = user)

