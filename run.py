"""
2x lines between each to be PEP-8 compliant
"""


import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


"""
Creates an instance of the Flask class and stores in variable called app
The first arguement is the name of the app module and we can use __name__
which is a built in Python var
app.route decorator - wjen we browse to root directory it triggers the
function
"""


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

"""
Flask will render the contents of index.html using render_temp
function - when we go to top-level of our domain "/" it returns
the template from index()
"""


@app.route("/")  # This is a top-level view
def index():
    return render_template("index.html")  # Looks in templates dir


@app.route("/about")  # This is the about view
def about():
    data = []  # Blank list to hold data
    with open("data/company.json", "r") as json_data:  # Reads in json data
        data = json.load(json_data)  # loads json data to var
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")  # Angle bracket passes in URL path
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:  # iterates through the loaded json
            if obj["url"] == member_name:  # when url matches member
                member = obj  # sets member to be the ret object data
    return render_template("member.html", member=member)

    """
    Passes in the arguments member.html which is member page template
    second argument (member=member) is the variable (member) and the
    member object created previously
    """


@app.route("/contact", methods=["GET", "POST"])  # This is the contact view
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get(
                "name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


"""
If name is equal to main the host will be set to an environ IP/Port
otherwise a default IP (0.0.0.0) & Port (5000_ am will be used
__main__ is default Python module - if not imported it runs directly
then run the app using the arguments passed
"""


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
