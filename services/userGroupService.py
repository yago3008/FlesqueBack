from models.userGroup import UserGroup
from models.user import User
from helper import db

def invite_user(user_id, group_id):
    user_invited = UserGroup(user_id=user_id, group_id=group_id)
    db.session.add(user_invited)
    db.session.commit()
    return user_invited

def get_user_groups(user_id):
    groups = UserGroup.query.filter_by(user_id=user_id).all()
    return [group.group_id for group in groups]

def to_json(self):
    return{
        'user_group_id': self.user_group_id,
        'user_id': self.user_id,
        'group_id': self.group_id
    }