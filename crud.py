"""CRUD operations."""
from model import db, User

def get_user_by_email(email) -> User:
    return User.query.filter(User.email == email).first()