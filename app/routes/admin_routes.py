# Handles admin pages
from flask import Blueprint, request, render_template, redirect, url_for, flash

# Define admin blueprint
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Admin login page
@admin_bp.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # TEMPORARY: hardcoded credentials
        if username == "admin" and password == "admin123":
            flash("Admin login successful!", "success")
            return redirect(url_for('admin.dashboard'))
        else:
            flash("Invalid admin credentials!", "danger")

    return render_template('admin_login.html')


# Admin dashboard page
@admin_bp.route('/dashboard')
def dashboard():
    return "<h1>Welcome Admin! You can manage notices and users here.</h1>"

