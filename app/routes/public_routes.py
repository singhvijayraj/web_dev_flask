# Handles public pages
# app/routes/public_routes.py
from flask import Blueprint, render_template

public_bp = Blueprint("public", __name__)

@public_bp.route("/")
def home():
    return render_template("home.html")

@public_bp.route("/notices")
def notices():
    """
    Public notices page (will later fetch notices from DB)
    """
    return render_template("notices.html")

@public_bp.route("/queries")
def queries():
    """
    Public query submission + status check page
    """
    return render_template("queries.html")

@public_bp.route("/employee-login")
def employee_login():
    """
    Employee login page (will later add authentication)
    """
    return render_template("employee_login.html")

