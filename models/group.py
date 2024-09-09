from helper import db
from sqlalchemy import func

class Group(db.Model):
    __tablename__ = 'groups'

    group_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    admin_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def to_json(self):
        return{

            'group_id': self.group_id,
            'name': self.name,
            'created_at': self.created_at,
            'admin_id': self.admin_id,
        }

    def __repr__(self):
        return f'<Group {self.name}>'