'''
  Mohammed Jamil
  SoftDev1 pd06
  K#25: Getting More REST
  M 2018-11-14
'''
import urllib.request as urlrequest
import urllib.parse as parse
import json

from flask import Flask,render_template,request

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign fxn to route
def root():
    with urlrequest.urlopen("https://api.nasa.gov/planetary/apod?api_key=TDM6AF2YTEDMeHkBmrDxTgWmzDZypeuiQ5iiYVmI") as nasa:
        dict=json.load(nasa)
    imgurl=dict["hdurl"]
    explain=dict["explanation"]
    url_stub="https://tastedive.com/api/similar?q=hot+fuzz&info=1&k="
    key="323717-Undecide-FM497OZT"
    newurl=url_stub+key
    print(newurl)
    req=urlrequest.Request(newurl,headers={'User-Agent': 'Mozilla/5.0'})
    urlobj=urlrequest.urlopen(req)
    data=json.load(urlobj)
    print(data)
    print(data['Similar']['Results'][1])
    #print(imgurl)
    #print(explain)
    return render_template("template.html",img=imgurl,explanation=explain,name=data['Similar']['Results'][1]['Name'],summary=data['Similar']['Results'][1]['wTeaser'],video=data['Similar']['Results'][1]['yID'])

app.debug = True
app.run()
