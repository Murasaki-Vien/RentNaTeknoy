from flask import Blueprint, render_template,request
from flask_login import login_required, current_user
from sqlalchemy import null
from App.models import RentalListing, Reviews, User
from App import db 

Dashboard = Blueprint("Dashboard", __name__)


@Dashboard.route("/dashboard/<MyAcc>", methods=["POST", "GET"] )
@login_required 
def dashboardPage(MyAcc):

    rentalListing = RentalListing.query.all()
    if request.method == "POST":
        sorting = request.form.get("sort_by")
        if sorting == "Price":
            rentalListing = RentalListing.query.order_by(RentalListing.price.asc())
        elif sorting == "Distance":
            rentalListing = RentalListing.query.order_by(RentalListing.distance.asc())
        elif sorting == "All":
            rentalListing = RentalListing.query.all()

    return render_template("dashboard.html", email=MyAcc, rental_listing = rentalListing)

@Dashboard.route("/about-page/<MyAcc>")
@login_required
def AboutPage(MyAcc):
    return render_template("aboutus.html", email=MyAcc)

@Dashboard.route("/PrivacyNPolicy/<MyAcc>")
@login_required
def PrivacyPolicyPage(MyAcc):
    return render_template("", email=MyAcc)

@Dashboard.route("/TermsNConditions/<MyAcc>")
@login_required
def TermsConditionPage(MyAcc):
    return render_template("", email=MyAcc)

@Dashboard.route("/ContactUs/<MyAcc>")
@login_required
def ContactUsPage(MyAcc):
    return render_template("contactus.html", email=MyAcc)


@Dashboard.route("/RL-Reviews/<MyAcc>/<AppartmentName>", methods=["POST", "GET"])
@login_required
def RLReviewsPage(MyAcc, AppartmentName):
    
    rentalListing = RentalListing.query.filter_by(appartmentName=AppartmentName).first()

    if request.method == "POST":
        comment = request.form.get("comment") 
        rating = request.form.get("rate")
        if rating != None:
            rating = int(rating)
        else:
            rating = 0
        
        if comment != "":
            rev = Reviews(
                data=comment,
                rating=rating,
                rentlisting_id=rentalListing.id,
                user_id=current_user.id
            )
            db.session.add(rev)
            db.session.commit()


    user = User.query.all()
    review = Reviews.query.all()

    return render_template("RLInfo.html", 
            email=MyAcc, 
            AppartmentName=AppartmentName,
            rent=rentalListing, 
            users=user,
            reviews=review)


# @Home.route("/<path:path>")
# def ErrorPage(path):
#     return "<h1>Hello Word</h1>"