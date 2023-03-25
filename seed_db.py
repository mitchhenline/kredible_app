import os
from flask import Flask
from model import db, connect_to_db, User

app = Flask(__name__)

connect_to_db(app)

# Drop existing database
try:
    os.system("dropdb -U postgres kredible_app")
    os.system("createdb -U postgres kredible_app")

# Recreate the kredible database
except:
    os.system("createdb kredible_app")

db.create_all()

# Users

user1 = User(email = "mitch@grannys.com", password = "goaggies", first_name = "Mitch", last_name = "Henline", company = "Granny's Gourmet Grilled Cheese", admin = True)
user2 = User(email = "tanner@grannys.com", password = "goaggies", first_name = "Tanenr", last_name = "Randall", company = "Granny's Gourmet Grilled Cheese", admin = True)

db.session.add_all([
    user1,
    user2
])

db.session.commit()

