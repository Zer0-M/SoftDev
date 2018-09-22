from flask import Flask,render_template
app = Flask(__name__) #create instance of class Flask
import randoccgen
occdict=randoccgen.generateDict('\\data\\occupations.csv')
keys=list(occdict.keys())
values=[]
for key in keys:
    values.append(occdict[key])

@app.route("/") #assign fxn to route
def hello_world():
    return "No hablo queso!"

@app.route("/occupations")
def occupationtable():
    return render_template("tabletemplate.html",head0='Job Class',head1='Percentage',collection=occdict)

app.debug = True
app.run()
