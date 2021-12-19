from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

base_dir = os.path.dirname(__file__)


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(base_dir,'migrate_data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

Migrate(app,db)

#flask db init
#flask db migrate
#flask db upgrade




class Person(db.Model):
  __tablename__ ='persons'

  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.Text)
  age=db.Column(db.Integer)

  def __init__(self,name,age):
    self.name = name
    self.age = age

    def __str__(self):
      return f"id={self.id},name={self.name},age={self.age}"


@app.route('/')
def index():
    return "Hello world!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)