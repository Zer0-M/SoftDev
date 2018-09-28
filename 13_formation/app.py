from flask import Flask,render_template,request
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def hello_world():
   print(app)
   return render_template("forms.html")
@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    #print(request.args[0])
    #print(request.header)
    return "Waaa hooo HAAH"
   

app.debug = True
app.run()
