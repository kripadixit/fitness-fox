from flask import render_template, request
from datetime import datetime
from datetime import timedelta
from fitness_fox import app
from flask_sqlalchemy import SQLAlchemy
from fitness_fox.models import Workout
from fitness_fox import db
from sqlalchemy import and_, func
import sqlalchemy as sa

@app.route('/AddActivity.html')
def setValue():
    return render_template('AddActivity3.html')

@app.route('/AddActivity.html', methods=['POST'])
def getValue():
	activity_date = request.form['activity_date']
	activity_time = request.form['activity_time']
	activity_name = request.form['activity']
	activity_mins = request.form['mins']
	activity_date = datetime.strptime(activity_date, '%Y-%m-%d').date()
	activity_time = datetime.strptime(activity_time, '%H:%M').time()

	workout = Workout(activity_name, activity_date, activity_time, activity_mins)
	db.session.add(workout)
	db.session.commit()
	return render_template('Success1.html')

@app.route('/')
@app.route('/Chart.html')
def view():
	from_date = datetime.now() - timedelta(days=7)
	to_date = datetime.now()
	weekData = db.session.query(Workout.dateDb, db.func.sum(Workout.minutesDb).label("minutesDb")).filter(Workout.dateDb <= to_date).filter(Workout.dateDb >= from_date).group_by(func.date(Workout.dateDb)).order_by(Workout.dateDb).all()
	labels = []
	values = []
	for c in weekData:
	   values.append(c.minutesDb)
	   labels.append(c.dateDb.strftime("%Y-%m-%d"))
	return render_template('Chart1.html', max=90, values=values, labels=labels)

@app.route('/Success.html')
def successPage():
	return render_template('Success1.html')
