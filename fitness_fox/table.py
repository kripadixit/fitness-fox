from flask_table import Table, Col


class Results(Table):
	id = Col('Id', show=False)
	firstname = Col('First Name')
	lastname = Col('Last Name')
	email = Col('Email')
	birthdate = Col('Date of Birth')
	weight = Col('Weight')
