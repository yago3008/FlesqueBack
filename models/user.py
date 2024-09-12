from helper import db
from dataclasses import dataclass

@dataclass
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    birth = db.Column(db.String(80), nullable=False)

    def to_json(self):
        return{

            'id': self.id,
            'fullname': self.fullname,
            'password': self.password,
            'email': self.email,
            
        }

    def __repr__(self):
        return f'<User {self.fullname}>' 