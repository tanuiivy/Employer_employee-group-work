from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Employer(db.Model, SerializerMixin):
    __tablename__ = 'employers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Employer {self.name} - {self.department}>"
