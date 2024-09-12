from models.userGroup import UserGroup
from models.user import User
from models.group import Group
from helper import db

def invite_user(user_id, group_id):
    user_invited = UserGroup(user_id=user_id, group_id=group_id)
    db.session.add(user_invited)
    db.session.commit()
    return user_invited

def get_user_groups(user_id):
    user_groups = UserGroup.query.filter_by(user_id=user_id).all()
    group_ids = [user_group.group_id for user_group in user_groups]
    groups = Group.query.filter(Group.group_id.in_(group_ids)).join(User).add_entity(User).all()

    return [{ "group": group[0].to_json(), "user": group[1].to_json() } for group in groups]

def to_json(self):
    return{
        'user_group_id': self.user_group_id,
        'user_id': self.user_id,
        'group_id': self.group_id
    }