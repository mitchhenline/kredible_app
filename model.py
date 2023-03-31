"""Models for Kredible app."""

import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A site user."""

    __tablename__ ="users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    company = db.Column(db.String(255))
    admin = db.Column(db.Boolean)

    def __repr__(self):
        return f'User: id={self.id} Name={self.last_name, self.first_name} Company={self.company}'
    
class Advocate(db.Model):
    """An user's advocate."""

    __tablename__ ="advocates"

    adv_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    company = db.Column(db.String(255))
    industry = db.Column(db.String(255))
    company_size = db.Column(db.String(255))
    use_case = db.Column(db.String(255))
    product = db.Column(db.String(255))

    def __repr__(self):
        return f'Advocate: Advocate_ID={self.id} Name={self.last_name, self.first_name} Company={self.company}'


class UserAdv(db.Model):
    """User-advocate relationship table"""

    __tablename__ = "user_adv_relationships"

    user_adv = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey("users.id"))
    adv_id = db.Column(db.Integer, db.ForeignKey("advocates.adv_id"))

    user = db.relationship("User", backref="user_adv_relationships")
    advocate = db.relationship("Advocate", backref="user_adv_relationships")

def connect_to_db(flask_app, db_uri=os.environ["POSTGRES_URI"], echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Database connected.")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)