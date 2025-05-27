from app import db
from sqlalchemy_serializer import SerializerMixin

class Employer(db.Model, SerializerMixin):
    __tablename__ = 'employers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)

    # 1-M relationship
    employees = db.relationship('Employee', back_populates='employer', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Employer {self.name}, Department {self.department}>'