from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'employee.employee_login'  # Redirect here if login required

def create_app():
    app = Flask(__name__)

    # -----------------------------
    # Configurations
    # -----------------------------
    app.config['SECRET_KEY'] = 'your_secure_secret_key'  # For sessions & flash
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # -----------------------------
    # Initialize extensions
    # -----------------------------
    db.init_app(app)
    login_manager.init_app(app)

    # -----------------------------
    # Import and register blueprints
    # -----------------------------
    from app.routes.public_routes import public_bp
    from app.routes.employee_routes import employee_bp
    from app.routes.admin_routes import admin_bp  # Optional if you have admin

    app.register_blueprint(public_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(admin_bp)  # Remove if not ready yet

    return app

# -----------------------------
# User loader for Flask-Login
# -----------------------------
from app.models.employee import Employee  # Make sure Employee model exists and implements UserMixin
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))  # Returns the employee object from DB



