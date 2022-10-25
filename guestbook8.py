from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:BQEhbz67958@10.104.9.222:5432/testdb'
app.config['SQLALCHEMY_TRACK_MPDIFICATION'] = False

db_uri = 'sqlite:///Ex2.sqlite3'
Base = declarative_base()
engine = create_engine(db_uri, echo=False)
Session = sessionmaker(bind=engine)
session = Session()


class Member(Base):
    __tablename__ = 'member'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    join_date = Column(DateTime, nullable=False)
    vip = Column(Boolean, nullable=False)
    number = Column(Float, nullable=False)

@app.route('/')
def index():
    result = Member.query.all()
    return render_template('index8.html', result=result)

@app.route('/sign')
def sign():
    return render_template('sign8.html')

@app.route('/process', methods=['POST'])
def process():
    user = Member(
    name='Toddy',
    description='im testing this',
    vip=True,
    join_date=datetime.date.today(),
    number=45.0
    )
    session.add(user)
    session.commit()


if __name__ == '__main__':
    app.run(host= '0.0.0.0',port= 80,debug=True)
    
