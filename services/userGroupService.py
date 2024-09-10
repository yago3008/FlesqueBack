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
    groups = Group.query.filter(Group.group_id.in_(group_ids)).all()

    group_data = list(map(lambda g: g.to_json(), groups))

    return [group for group in group_data]

def to_json(self):
    return{
        'user_group_id': self.user_group_id,
        'user_id': self.user_id,
        'group_id': self.group_id
    }