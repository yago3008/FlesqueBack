from models.user import User
from helper import db

def create_user(fullname, password, email, birth):
    new_user = User(fullname=fullname, password=password, email=email, birth=birth)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def update_user(id, new_fullname=None, new_password=None, new_email=None):
    user = User.query.get(id)
    if not user:
        return None
    
    if new_fullname:
        user.fullname = new_fullname
    if new_email:
        user.email = new_email
    if new_password:
        user.password = new_password
    
    db.session.commit()
    return user


def delete_user(id):
    user = User.query.get(id)
    if not user:
        return None
    
    db.session.delete(user)
    db.session.commit()
    return user

def get_by_id(id):
    return User.query.get(id)