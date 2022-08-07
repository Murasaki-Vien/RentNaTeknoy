from flask import Blueprint, render_template

Home = Blueprint("Home", __name__)



@Home.route("/")
@Home.route("/home")
def HomePage():
    return render_template("home.html")

@Home.route("/about-page")
def AboutPage():
   return render_template("aboutus.html")

@Home.route("/privacyNPolicy")
def PrivacyPolicyPage():
    return render_template()

@Home.route("/TermsNConditions")
def TermsConditionPage():
    return render_template()

@Home.route("/ContactUs")
def ContactUsPage():
    return render_template("contactus.html")



# @Home.route("/<path:path>")
# def ErrorPage(path):
#     return "<h1>Hello Word</h1>"