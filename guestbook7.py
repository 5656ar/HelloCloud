from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, CHAR, VARCHAR
from test_ex_1 import Registration_table, Students_table, Teachers_table, Subject_table, session



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:MDDnfo15110@10.104.7.84:5432/testdb'
app.config['SQLALCHEMY_TRACK_MPDIFICATION'] = False


@app.route('/')
def index():
    result = session.query(Students_table.student_id,Students_table.f_name,Students_table.l_name,Registration_table.subject_id,Subject_table.subject_name,Registration_table.grade,Teachers_table.f_tname,Teachers_table.l_tname).outerjoin(Registration_table,Students_table.student_id == Registration_table.student_id).outerjoin(Subject_table,Registration_table.subject_id == Subject_table.subject_id).join(Teachers_table,Subject_table.teacher_id == Teachers_table.teacher_id).all()
    return render_template('index8.html', result=result)



if __name__ == '__main__':
    app.run(host= '0.0.0.0',port= 80,debug=True)
    
