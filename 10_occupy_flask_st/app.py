from flask import Flask,render_template
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def hello_world():
    return "No hablo queso!"

@app.route("/my_foist_template")
def temptest():
    return render_template("template.html",collection=[0,1,1,2,3,5,8])

app.debug = True
app.run()
