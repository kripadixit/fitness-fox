from sqlalchemy import Column, Integer, String
from flask_table import Table, Col
from fitness_fox import db


class User(db.Model):
	

	id = db.Column(db.Integer, primary_key=True)
	firstnameDb = db.Column(db.String(50), unique=False)
	lastnameDb = db.Column(db.String(50), unique=False)
	emailDb = db.Column(db.String(50), unique=False)
	passwordDb = db.Column(db.String(50), unique=False)	
	workoutsDb = db.relationship('Workout', backref='author', lazy=True)


	def __init__(self, firstname, lastname, email, password):

		self.firstnameDb = firstname
		self.lastnameDb = lastname
		self.emailDb = email
		self.passwordDb = password

	def __repr__(self):
		return f"User('{self.firstnameDb}', '{self.lastnameDb}', '{self.emailDb}', '{self.passwordDb}', '{self.lastnameDb}')"

class Workout(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	activityDb = db.Column(db.String(50), unique=False)
	dateDb = db.Column(db.Date, nullable=True)
	timeDb = db.Column(db.Time, nullable=True)
	minutesDb  = db.Column(db.Integer)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __init__(self, activityDb, activity_date, activity_time,activity_mins, user_id):
		self.activityDb = activityDb
		self.dateDb = activity_date
		self.timeDb = activity_time
		self.minutesDb = activity_mins
		self.user_id = user_id

	def __repr__(self):
		return f"User('{self.activityDb}', '{self.dateDb}', '{self.timeDb}', '{self.minutesDb}', '{self.user_id}')"