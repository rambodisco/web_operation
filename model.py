from config import *

class User(db.Model):
    userid = db.Column('user_id',db.Integer(),primary_key=True)
    name = db.Column('user_name',db.String(50),unique=True)
    email = db.Column('user_email',db.String(50),unique=True)
    password= db.Column('user_pass',db.String(50))


class Student(db.Model):
    rollno = db.Column('roll_no',db.Integer(),primary_key=True)
    s_name = db.Column('stud_name',db.String(50))
    s_email = db.Column('stud_email',db.String(50),unique=True)
    s_dept = db.Column('stud_dept', db.String(50))
    s_fees = db.Column('stud_fees', db.Float())


with app.app_context():
    db.create_all()
    print('Tables created..')