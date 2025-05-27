from faker import Faker

from app import app
from models import Employer, Employee, db

with app.app_context():
    fake = Faker()

    # Create 50 employees
    employees = []
    for i in range(50):
        employee = Employee(name=fake.name(), body=fake.job())
        employees.append(employee)

    db.session.add_all(employees)
    db.session.commit()

    # Create 10 employers
    employers = []
    for i in range(10):
        employer = Employer(name=fake.name(), department=fake.bs())
        employers.append(employer)

    db.session.add_all(employers)
    db.session.commit()
