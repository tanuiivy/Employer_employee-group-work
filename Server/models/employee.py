from app import db

class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    department = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)

    # Foreign key to Employer
    employer_id = db.Column(db.Integer, db.ForeignKey('employers.id'))

    def __repr__(self):
        return f"<Employee {self.name} - {self.role}>"
