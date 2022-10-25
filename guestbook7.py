from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:BQEhbz67958@10.104.9.222:5432/testdb'
app.config['SQLALCHEMY_TRACK_MPDIFICATION'] = False

db = SQLAlchemy(app)

class Comments(db.Model):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    comment = Column(String)

@app.route('/')
def index():
    result = Comments.query.all()
    return render_template('index7.html', result=result)



if __name__ == '__main__':
    app.run(host= '0.0.0.0',port= 80,debug=True)
    
