from flask_login import UserMixin

# Dummy user database for now — later will use SQLite
USERS = {
    "admin": {"password": "admin123"}  # In production: use hashed passwords
}

class Employee(UserMixin):
    def __init__(self, username):
        self.id = username

    @staticmethod
    def validate_login(username, password):
        user = USERS.get(username)
        if user and user["password"] == password:
            return Employee(username)
        return None
