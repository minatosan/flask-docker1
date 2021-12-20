from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from form_model_app import form_model_app

db=SQLAlchemy(form_model_app)
Migrate(form_model_app,db)

#export FLASK_APP = models.py
#flask db init
# flask db migrate -m first_commit
#flask db upgrade

class Member(db.Model):
  __tablename__="members"

  id = db.Column(db.Integer,primary_key=True)
  name=db.Column(db.text)
  age=db.Column(db.Integer)
  comment=db.Column(db.Text)

  def __init__(self,name,age,comment):
    self.name = name
    self.age = age
    self.comment = comment
