'''

Sophia Xia
SoftDev1 pd6
K13 -- Echo Echo Echo
2018-09-27
'''

from flask import Flask, render_template, request, session, url_for, redirect
app = Flask(__name__)
import os
app.secret_key=os.urandom(32)

user = "JAMIIII"
pswd = "swordfish"

@app.route("/")
def home():
    # prints <Flask 'app'> 
    print(app)
    if 'username' in session:
        return redirect(url_for("authenticate"))
    return render_template("auth.html")

# default method is GET when POST isn't specified
@app.route("/usrfail")
def wrongusr():
    if 'username' in session:
        return redirect(url_for("authenticate"))
    return render_template("auth.html", ERROR = "SHAME ON YOU, WRONG USERNAME")
@app.route("/pwdfail")
def wrongpwd():
    if 'username' in session:
        return redirect(url_for("authenticate"))
    return render_template("auth.html", ERROR = "SHAME ON YOU, WRONG PASSWORD")
@app.route("/auth", methods=["GET","POST"])
def authenticate(): 
    # return "I like watermelon"
    if 'username' in session:
        return render_template("welcome.html", username = session['username'], sub1 = request.method)
    usr = request.form["username"]
    passwd = request.form["password"]
    if usr != user:
        return redirect(url_for("wrongusr"))
    elif usr == user and passwd!=pswd:
        return redirect(url_for("wrongpwd"))
    session['username']=usr
    return render_template("welcome.html", username = usr, sub1 = request.method)

@app.route("/signout")
def logout():
    session.pop("username")
    return render_template("auth.html")

app.debug = True
app.run()
