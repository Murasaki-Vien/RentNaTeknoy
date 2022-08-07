import email
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from App.models import Reviews, User
import math



UserProfile = Blueprint("UserProfile", __name__)


@UserProfile.route("/UserProfile/<MyAcc>")
@login_required
def UserPage(MyAcc):

    UserReviews = Reviews.query.filter_by(user_id=current_user.id).all()

    stars : dict = {
        "NoReviews" : 0,
        "five" : 0,
        "four" : 0,
        "three" : 0,
        "two" : 0,
        "one" : 0
    }

    if UserReviews:
        for review in UserReviews: 
            rating = int(math.floor(float(review.rating)))

            if rating == 5: stars["five"]+=1
            elif rating == 4: stars["four"]+=1
            elif rating == 3: stars["three"]+=1
            elif rating == 2: stars["two"]+=1
            else : 
                stars["one"]+=1
            stars["NoReviews"]+=1 

    return render_template("myaccount.html", email=MyAcc, userreviews=UserReviews, stars=stars)

@UserProfile.route("/about-page/<MyAcc>")
@login_required
def AboutPage(MyAcc):
    return render_template("aboutus.html", email=MyAcc)


@UserProfile.route("/PrivacyNPolicy/<MyAcc>")
@login_required
def PrivacyPolicyPage(MyAcc):
    return render_template("", email=MyAcc)

@UserProfile.route("/TermsNConditions/<MyAcc>")
@login_required
def TermsConditionPage(MyAcc):
    return render_template("", email=MyAcc)

@UserProfile.route("/ContactUs/<MyAcc>")
@login_required
def ContactUsPage(MyAcc):
    return render_template("contactus.html", email=MyAcc)
