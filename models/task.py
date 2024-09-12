from helper import db

class Task(db.Model):
    __tablename__ = 'task'

    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(50), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('status.status_id'))

    def to_json(self, user_fullname):
        return{

            'task_id': self.task_id,
            'title': self.title,
            'desc': self.desc,
            'group_id': self.group_id,
            'user_id': self.user_id,
            'user_fullname': user_fullname,
            'status_id': self.status_id,
        }

    def __repr__(self):
        return f'<Task {self.title}>'