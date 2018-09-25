#EmptyFlask- Mohammed Jamil, Isaac Jon
#SoftDev1 pd06
#K#10 -- Jinja Tuning
#2018-09-24   


from flask import Flask,render_template
from util import randoccgen #use the python file from assignment 3 as a module in order to use its functions(name changed for easier use)
app = Flask(__name__) #create instance of class Flask
occDict=randoccgen.generateDict('data/occupations.csv') #create a dictionary from the occupations csv

@app.route("/")
def landingPage():
    return'''
    <h1>Welcome</h1>
    <br>
    <a href='/occupations'><h3>See Occupations</h3></a>'''

@app.route("/occupations")
def occTable():
    randOcc=randoccgen.getOccupation() #randomly generate an occupation weighted by percentage
    randOccURL = occDict[randOcc][1] #get the url for associated with randomly selected occupation in the csv
    return render_template("tabletemplate.html",title="Job Picker",Heading="Randomly Selected Job For The Needy",head0='Job Class',head1='Percentage',head2='URL',collection=occDict,occ=randOcc,url=randOccURL)

app.debug = True
app.run()
