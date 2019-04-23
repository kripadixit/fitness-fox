
""" This module is responsible for providing 
	an interface with the database.
	We imported sqlalchemy library which 
	would allow us to work with database. 
	Db was the name of the database session. 
	It was imported from main fitness fox 
	application.
"""
from sqlalchemy import Column, Integer, String
from flask_table import Table, Col
from fitness_fox import db

""" User class provided structure to User 
	table in the database. It also provides 
	method to view and add data to the database
"""
class User(db.Model):
	
	/*** The below lists attributes of the User Table ***/ 

	id = db.Column(db.Integer, primary_key=True) #Primary Key
	firstnameDb = db.Column(db.String(50), unique=False) #First Name
	lastnameDb = db.Column(db.String(50), unique=False) #LastName
	emailDb = db.Column(db.String(50), unique=False) #Email
	passwordDb = db.Column(db.String(50), unique=False)	#Password

	# The below code creates 1 to many relationship with the Workout Table
	workoutsDb = db.relationship('Workout', backref='author', lazy=True)

"""
	The below function allowed us to add the User data into the database.
	 Once user signed up on   the website, the below piece of code 
	 would add the data into the database under the User table 
"""
	def __init__(self, firstname, lastname, email, password):

		self.firstnameDb = firstname #add firstname
		self.lastnameDb = lastname #add lastname
		self.emailDb = email #add email
		self.passwordDb = password #add password

"""
	The below function allowed us to view the User data 
	in the command prompt. The order of viewing is dictated
	by the return statement in the function. 
"""
	def __repr__(self):
		return f"User('{self.firstnameDb}', '{self.lastnameDb}', '{self.emailDb}', '{self.passwordDb}', '{self.lastnameDb}')"


"""
	Workout class provided structure to Workout table in the database.
	It also provides method to view and add data to the database.
"""
class Workout(db.Model):
	
	id = db.Column(db.Integer, primary_key=True) # Primary Key
	activityDb = db.Column(db.String(50), unique=False) # Type of Workout
	dateDb = db.Column(db.Date, nullable=True) # Date of Workout
	timeDb = db.Column(db.Time, nullable=True) # Time of workout
	minutesDb  = db.Column(db.Integer) # Minutes of workout
	# The below code maps user_id  to id attribute in User Table
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

"""
	The below function allowed us to add the Workout data into the database. 
	Once the user added his workout in the website, the below 
	piece of code would add the data into 
	the database under Workout table
"""

	def __init__(self, activityDb, activity_date, activity_time,activity_mins, user_id):
		self.activityDb = activityDb # add workout type
		self.dateDb = activity_date # add date of workout
		self.timeDb = activity_time # add time
		self.minutesDb = activity_mins # add minutes
		self.user_id = user_id # backreference user id from user table

""" 
	The below function allowed us to view the Workout data
	in the command prompt. The order of viewing is 
	dictated by the return statement in the function. 
"""
	def __repr__(self):
		return f"User('{self.activityDb}', '{self.dateDb}', '{self.timeDb}', '{self.minutesDb}', '{self.user_id}')"