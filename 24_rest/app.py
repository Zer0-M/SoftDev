'''
  Mohammed Jamil
  SoftDev1 pd06
  K#24: A RESTful Journey Skyward
  M 2018-11-14
'''
from flask import Flask,render_template
import urllib.request as request
import urllib.parse as parse
import json
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def root():
    with request.urlopen("https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo") as nasa:
        dict=json.load(nasa)
    imgurl=dict["hdurl"]
    explain=dict["explanation"]
    #print(imgurl)
    #print(explain)
    return render_template("template.html",img=imgurl,explanation=explain)

app.debug = True
app.run()
