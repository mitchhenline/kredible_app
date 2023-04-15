"""CRUD operations."""
from model import db, User, UserAdv, Advocate

def get_user_by_email(email) -> User:
    return User.query.filter(User.email == email).first()

def get_relationships_by_email(id):
    return UserAdv.query.filter(UserAdv.id == id)

def get_advocate_by_id(id):
    return Advocate.query.filter(Advocate.adv_id == id).first()