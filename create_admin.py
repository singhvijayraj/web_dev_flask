from app import create_app, db
from app.models.employee import Employee
from werkzeug.security import generate_password_hash

app = create_app()
with app.app_context():
    db.create_all()  # Ensure tables exist

    existing = Employee.query.filter_by(username="admin").first()
    if existing:
        print("Admin already exists.")
    else:
        e = Employee(username="admin", password=generate_password_hash("admin123"))
        db.session.add(e)
        db.session.commit()
        print("Admin created successfully!")

