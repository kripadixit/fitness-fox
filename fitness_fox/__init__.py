""" 
This class initializes the application
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Initializes the application
db = SQLAlchemy(app)

# Add support for Bootstrap
bootstrap = Bootstrap(app)

from fitness_fox import routes