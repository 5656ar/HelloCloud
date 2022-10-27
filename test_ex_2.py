from sqlalchemy import CHAR, VARCHAR, Column, Integer, ForeignKey
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Registration_table(db.Model):
    __tablename__ = 'Registration'
    id = db.Column(Integer, primary_key=True)
    student_id = db.Column(CHAR(13), nullable=False)
    subject_id = db.Column(VARCHAR(15), nullable=False)
    year = db.Column(CHAR(4), nullable=False)
    semester = db.Column(CHAR(1), nullable=False)
    grade = db.Column(CHAR(2))

    def __repr__(self):
        return '<User(student_id = {}, subject_id = {}, year = {}, semester ={}, grade={})>'.format(self.student_id, \
            self.subject_id, self.year , self.semester, self.grade)
    


