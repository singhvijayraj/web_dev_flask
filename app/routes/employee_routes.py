from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, logout_user, login_user, current_user
from app.models.employee import Employee
from app.models.notice import Notice
from werkzeug.security import check_password_hash
from app import db

employee_bp = Blueprint("employee", __name__, template_folder="../templates")

@employee_bp.route("/employee/login", methods=["GET", "POST"])
def employee_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = Employee.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("employee.employee_dashboard"))
        flash("Invalid username or password")
    return render_template("employee_login.html")


@employee_bp.route("/employee/dashboard")
@login_required
def employee_dashboard():
    notices = Notice.query.order_by(Notice.created_at.desc()).all()
    return render_template("employee_dashboard.html", notices=notices)


@employee_bp.route("/employee/add_notice", methods=["GET", "POST"])
@login_required
def add_notice():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        new_notice = Notice(title=title, content=content)
        db.session.add(new_notice)
        db.session.commit()

        flash("Notice added successfully")
        return redirect(url_for("employee.employee_dashboard"))

    return render_template("add_notice.html")


@employee_bp.route("/employee/logout")
@login_required
def employee_logout():
    logout_user()
    return redirect(url_for("employee.employee_login"))
