#Mohammed Jamil
#SoftDev1 pd6
#K#13 -- Echo Echo Echo
#2018-09-23
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def hello_world():
   print(app)
   return render_template("forms.html",
                          title="Authentication", 
                          heading="Hello")
@app.route("/auth", methods=["GET","POST"])
def authenticate():
    print(app)
    print(request)
    print(request.headers)#gets the HTML headers
    print(request.args)#creates an immutable dictionary with the arguments from a GET request
    print(request.method)#gets the request method
    #print(request.form)#creates an immutable dicitonary with the arguments from a POST request
    name=request.form["username"]
    return render_template("Greeting.html",
                            title="Greeting",
                            Greeting="Oh Hai ",
                            username=name,#the username is received from the dictionary request.args created
                            requestmethod=request.method) #request.method gets the method via which the request received
   

app.debug = True
app.run()
