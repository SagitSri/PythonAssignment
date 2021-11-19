from flask import Flask, render_template, redirect, request, url_for, session
from flask.json import jsonify

import validation

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("layouts.html")

@app.route("/register", methods=["POST","GET"])
def register_page():
    if request.method == "POST":
        retVal = validation.validate_register_form_data(request.form)
        print(retVal)
        return retVal

@app.route("/login", methods=["POST","GET"])
def login_page():
    if request.method == "POST":
        usermail = request.form["mail"]
        userpsw = request.form["password"]
        retVal = validation.validate_user(usermail, userpsw)
        print("login",retVal)
        return jsonify(response = "login success") if retVal else jsonify(response="please check credentials")


if __name__ == "__main__":
    app.secret_key = "634512@](adfdsBdeDFDFD!#%"
    app.run(debug=True)