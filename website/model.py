from . import mongo
from flask_login import UserMixin

# class events(mongo.Model):
#     id = mongo.column(mongo.integer, primary_key=True)
#     name = mongo.column(mongo.string(1000))
#     content = mongo.column(mongo.string(10000))
#     date= mongo.column(mongo.DateTime(timezone=True))

# class user(mongo.Model, UserMixin):
#     id = mongo.column(mongo.integer, primary_key=True)
#     email = mongo.column(mongo.string(150), unique=True)
#     password= mongo.column(mongo.string(150))
#     fullname = mongo.column(mongo.string(150))

