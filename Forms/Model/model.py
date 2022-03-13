from mongoengine import  Document, StringField, IntField, DateTimeField
from flask_mongoengine import MongoEngine

db = MongoEngine()

class User(db.Document):
    user_name = db.StringField(required=True, max_length=100, unique=True)
    state = db.StringField(required=True, max_length=100)
    city = db.StringField(required=True, max_length=100)
    pincode = db.IntField(required=True,)