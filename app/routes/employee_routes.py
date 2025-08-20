from flask import Blueprint, request, render_template, redirect, url_for, flash
from app import db
from app.models.notice import Notice

# Define blueprint
employee_bp = Blueprint('employee', __name__, url_prefix='/employee')

# Employee login route
@employee_bp.route('/login', methods=['GET', 'POST'])
def employee_login():
    """
    Employee login page.
    Currently uses hardcoded credentials for testing.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # TEMPORARY hardcoded credentials
        if username == "employee" and password == "employee123":
            flash("Login successful!", "success")
            return redirect(url_for('employee.dashboard'))
        else:
            flash("Invalid username or password", "danger")

    return render_template('employee/employeelogin.html')


# Dashboard: List all notices
@employee_bp.route('/dashboard')
def dashboard():
    """
    Employee dashboard showing all notices.
    """
    notices = Notice.query.order_by(Notice.date_created.desc()).all()
    return render_template('employee_dashboard.html', notices=notices)


# Add a new notice
@employee_bp.route('/add_notice', methods=['GET', 'POST'])
def add_notice():
    """
    Add a new notice to the database.
    """
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        if not title or not content:
            flash("Title and Content cannot be empty!", "danger")
            return redirect(url_for('employee.add_notice'))

        new_notice = Notice(title=title, content=content)
        db.session.add(new_notice)
        db.session.commit()
        flash("Notice added successfully!", "success")
        return redirect(url_for('employee.dashboard'))

    return render_template('add_notice.html')


# Delete a notice
@employee_bp.route('/delete_notice/<int:notice_id>', methods=['POST'])
def delete_notice(notice_id):
    """
    Delete a notice by ID.
    """
    notice = Notice.query.get_or_404(notice_id)
    db.session.delete(notice)
    db.session.commit()
    flash("Notice deleted successfully!", "info")
    return redirect(url_for('employee.dashboard'))

