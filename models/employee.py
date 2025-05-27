from app import db
from sqlalchemy_serializer import SerializerMixin

class Employee(db.Model, SerializerMixin):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    department = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)

    # Foreign key to Employer
    employer_id = db.Column(db.Integer, db.ForeignKey('employers.id'), nullable=False)

    # 1-M relationship
    employer = db.relationship('Employer', back_populates='employees')

    def __repr__(self):
        return f'<Employee {self.name}, Email {self.email}, Department {self.department}, Role {self.role}, Salary {self.salary}>'    