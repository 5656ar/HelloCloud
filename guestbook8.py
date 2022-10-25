from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Date, CHAR, VARCHAR, ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:BQEhbz67958@10.104.9.222:5432/testdb'
app.config['SQLALCHEMY_TRACK_MPDIFICATION'] = False

db = SQLAlchemy(app)

class Comments(db.Model):
    __tablename__ = 'Aomtedz'
    student_id = Column(CHAR(13),ForeignKey('Students.student_id'), nullable=False)
    subject_id = Column(VARCHAR(15), ForeignKey('Subject.subject_id'), nullable=False)
    year = Column(CHAR(4), nullable=False)
    semester = Column(CHAR(1), nullable=False)
    grade = Column(CHAR(2), primary_key=True)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port= 80,debug=True)
    
