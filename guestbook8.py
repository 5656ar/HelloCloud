from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from test_ex_1 import Registration_table

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:BQEhbz67958@node37003-bunnapon.proen.app.ruk-com.cloud:11260/testdb'
app.config['SQLALCHEMY_TRACK_MPDIFICATION'] = False

db = SQLAlchemy(app)



@app.route('/')
def index():
    result = Registration_table.query.all()
    return render_template('index8.html', result=result)

@app.route('/sign')
def sign():
    return render_template('sign7.html')

@app.route('/process', methods=['POST'])
def process():

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port= 80,debug=True)
    
