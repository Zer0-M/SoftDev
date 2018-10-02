'''

Sophia Xia
SoftDev1 pd6
K13 -- Echo Echo Echo
2018-09-27
'''

from flask import Flask, render_template, request, session, url_for, redirect
app = Flask(__name__)

user = "JAMIIII"
pswd = "swordfish"

@app.route("/")
def home():
    # prints <Flask 'app'> 
    print(app)
    return render_template("auth.html")

# default method is GET when POST isn't specified
@app.route("/usrfail")
def wrongusr():
    return render_template("auth.html", ERROR = "SHAME ON YOU, WRONG USERNAME")
@app.route("/pwdfail")
def wrongpwd():
    return render_template("auth.html", ERROR = "SHAME ON YOU, WRONG PASSWORD")
@app.route("/auth", methods=["GET","POST"])
def authenticate():
    print(request.cookies)
    # return "I like watermelon"
    usr = request.form["username"]
    passwd = request.form["password"]
    if usr != user:
        return redirect(url_for("wrongusr"))
    elif usr == user and passwd!=pswd:
        return redirect(url_for("wrongpwd"))
    return render_template("welcome.html", username = usr, password = passwd, sub1 = request.method)

app.debug = True
app.run()
