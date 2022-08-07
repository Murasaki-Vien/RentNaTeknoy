from flask import Blueprint, render_template, request, redirect, url_for
from App import db
from App.models import User
from flask_login import login_required, login_user, logout_user

Forms = Blueprint("Forms", __name__)


@Forms.route("/Sign-in", methods=['GET', 'POST'])
def SigninPage():
    if request.method =="POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        
        if email != "":
            if user:
                if password == user.password:
                    login_user(user)
                    return redirect(url_for("Dashboard.dashboardPage", MyAcc=email))
        
    return render_template("signin.html")

@Forms.route('/Sign-in/TermsOfUse')
def TermsOfUsePage():
    return render_template()

@Forms.route("/Sign-in/PrivacyPolicy")
def PrivacyPolicyPage():
    return render_template()

@Forms.route("/Log-out")
@login_required
def LogOutPage():
    logout_user()
    return redirect(url_for("Home.HomePage"))


