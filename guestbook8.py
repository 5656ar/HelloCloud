from test_ex_1 import Registration_table
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:BQEhbz67958@10.104.9.222:5432/testdb'
app.config['SQLALCHEMY_TRACK_MPDIFICATION'] = False

db = SQLAlchemy(app)



@app.route('/')
def index():
    result = Registration_table.query.all()
    return render_template('index7.html', result=result)

@app.route('/sign')
def sign():
    return render_template('sign7.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']
    signature = Comments(name=name, comment=comment)
    db.session.add(signature)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port= 80,debug=True)
    
