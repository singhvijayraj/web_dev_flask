from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions (no app binding yet)
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "employee.employee_login"  # Redirect if not logged in

def create_app():
    app = Flask(__name__)
    
    # --- Basic Config ---
    app.config["SECRET_KEY"] = "your_secure_secret_key"  # For sessions & flash messages
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # --- Init extensions ---
    db.init_app(app)
    login_manager.init_app(app)

    # --- Register blueprints ---
    from app.routes.public_routes import public_bp
    from app.routes.employee_routes import employee_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(employee_bp)

    # --- User Loader ---
    from app.models.employee import Employee
    @login_manager.user_loader
    def load_user(user_id):
        # SQLAlchemy loads by primary key automatically
        return Employee.query.get(int(user_id))

    # --- Create tables automatically if not present ---
    with app.app_context():
        db.create_all()

    return app
  # Returns the employee object from DB



