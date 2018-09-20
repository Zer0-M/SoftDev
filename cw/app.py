from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def hello_world():
    return "<a href=/static/a.html>No hablo queso!</a>"

app.debug = True
app.run()
