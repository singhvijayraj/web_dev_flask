# Entry point to run Flask app
# run.py
from app import create_app

from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()


app = create_app()

if __name__ == "__main__":
    # Debug=True helps during development
    # In production, use a real WSGI server (e.g., gunicorn)
    app.run(debug=True)
