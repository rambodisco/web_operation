from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:ram123@localhost/mydatabase'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
