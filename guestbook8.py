from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, CHAR, VARCHAR


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:MDDnfo15110@10.104.7.84:5432/testdb'
app.config['SQLALCHEMY_TRACK_MPDIFICATION'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'Students'
    student_id = Column(CHAR(13),primary_key=True, nullable=False)
    f_name = Column(VARCHAR(30), nullable=False)
    l_name = Column(VARCHAR(30), nullable=False)
    e_mail = Column(VARCHAR(50),nullable=False)



  
@app.route('/')
def index():

    result = Student.query.all()
    # result += result1
    return render_template('index8.html', result=result)

@app.route('/sign')
def sign():
    return render_template('sign7.html')



if __name__ == '__main__':
    app.run(host= '0.0.0.0',port= 80,debug=True)
    
