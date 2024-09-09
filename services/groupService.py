from flask import session
from models.group import Group
from models.user import User
from helper import db

def create_group(name, admin_id):
    new_group = Group(name=name, admin_id=admin_id)
    db.session.add(new_group)
    db.session.commit()
    return new_group

def verify_admin(group_id, admin_id):
    group = Group.query.filter_by(group_id=group_id).first()
    if group and group.admin_id == admin_id:
        return True
    return False

def define_group(group_id):
   session['group_id'] = group_id
   return session['group_id']



