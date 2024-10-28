from app import db
from datetime import datetime, timezone


class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f'<User {self.username}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'created_at': self.created_at
        }
    