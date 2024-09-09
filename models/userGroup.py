from helper import db

class UserGroup(db.Model):
    __tablename__ = 'userGroup'

    user_group_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'))


    def to_json(self):
        return{

            'user_group_id': self.user_group_id,
            'user_id': self.user_id,
            'group_id': self.group_id,
        }

    def __repr__(self):
        return f'<Status {self.user_group_id}>'