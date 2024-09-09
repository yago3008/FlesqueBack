from helper import db

class Status(db.Model):
    __tablename__ = 'status'

    status_id = db.Column(db.Integer, primary_key=True)
    current = db.Column(db.String(50), nullable=False)


    def to_json(self):
        return{

            'status_id': self.status_id,
            'current': self.current,
        }

    def __repr__(self):
        return f'<Status {self.status_id}>'