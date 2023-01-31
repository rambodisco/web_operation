from model import *
from flask import render_template,request,session

app.secret_key="login"
@app.route('/login')
def login1():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template('register.html')

'''
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        formdata=request.form
        errors=[]
        if not formdata.get('username'):
            errors.append('User name cannot be empty')
        if not formdata.get('email'):
            errors.append('email cannot be empty')
        if not formdata.get('password'):
            errors.append('password cannot be empty')

        if errors:
            return render_template('register.html',errors=errors)

        try:
            user= User( name = formdata.get('username'),
                        email = formdata.get('email'),password = formdata.get('password'))
            db.session.add(user)
            db.session.commit()
        except:
            return render_template('register.html', message='already user present please try different name...')

        return render_template('register.html',message= 'user add successfully')

    return render_template('register.html')
'''

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/inner-page.html')
def inner():
    return render_template("inner-page.html")

@app.route('/portfolio-details.html')
def portfolio():
    return render_template("portfolio-details.html")

@app.route('/login',methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if (username=="ram" and password=="123"):
            session['email']= username
            return render_template("add_data.html",email=username)
        else:
            msg="invalid username/ password"
            return render_template("login.html",msg=msg)

@app.route('/add-stud',methods=['GET'])
@app.route('/stud-save',methods=['GET','POST'])
def add_student():
    if request.method == 'POST':
        formdata = request.form
        print(formdata)

        errors = []
        if not formdata.get('sname'):
            errors.append("Student Name Cannot be Empty")
        if not formdata.get('semail'):
            errors.append("Student Email Cannot be Empty")
        if not formdata.get('sfees'):
            errors.append("Student fees Cannot be Empty")
        else:
            try:
                s_fees = float(formdata.get('sfees'))
                if s_fees<=0:
                    errors.append('Invalid Fees')
            except:
                errors.append('Invalid Fees')

        if errors:
            return render_template('add_data.html', smessage=errors)

        student = Student(rollno=formdata.get('rno'),s_name=formdata.get('sname'),s_email=formdata.get('semail'),
        s_fees=s_fees,s_dept=formdata.get('sdept'))
        db.session.add(student)
        db.session.commit()
        return render_template('add_data.html', message="Student Added Successfully...")

    return render_template('add_data.html')

@app.route('/stud-list')
def list_student():
    return render_template('list_data.html',slist=Student.query.all())

@app.route('/stud-edit/<int:rno>')
@app.route('/stud-edit/',methods = ['POST'])
def update_student(rno=None):
    if request.method == 'GET':
        student = Student.query.filter_by(rollno=rno).first()
        return render_template('update_data.html',record = student)
    else:
        formdata = request.form
        rno = formdata.get('rno')
        student = Student.query.filter_by(rollno=rno).first()
        student.s_name = formdata.get('sname')
        student.s_email = formdata.get('semail')
        student.s_fees = formdata.get('sfees')
        student.s_dept = formdata.get('sdept')
        db.session.commit()
        return render_template('list_data.html', slist=Student.query.all())


