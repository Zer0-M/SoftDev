'''
  Mohammed Jamil
  SoftDev1 pd06
  K#26: Getting More REST
  M 2018-11-16
'''
import urllib.request as urlrequest
import urllib.parse as parse
import json

from flask import Flask,render_template,request

import houndify

app = Flask(__name__) #create instance of class Flask
clientId = "4Ia6G6lVW6GHxEsfidCnZw=="  
clientKey = "rNbQtAI1ceW2Ims2eGRWv2gZcYDHEwOOwKQPt2DshzJK7EHgte_CnSnWKaE1vGEljN8YdI_QnvPXhgSi7-y4FA==" 
userId = "Admin"

@app.route("/") #assign fxn to route
def root():
    client = houndify.TextHoundClient(clientId, clientKey, userId)
    response = client.query("tell me a joke")
    joke=response["AllResults"][0]["WrittenResponse"]
    response = client.query("weather in NY")
    weather=response["AllResults"][0]["WrittenResponse"]

    url="https://ipapi.co/8.8.8.8/json/"
    req=urlrequest.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    urlobj=urlrequest.urlopen(req)
    ipdata=json.load(urlobj)

    url_stub="https://holidayapi.com/v1/holidays?key={0}&country=US&year=2018&month=10"
    key="fa7fd31b-351d-4863-aa5a-597f059959a4"
    complete_url=url_stub.format(key)
    req=urlrequest.Request(complete_url,headers={'User-Agent': 'Mozilla/5.0'})
    urlobj=urlrequest.urlopen(req)
    holidata=json.load(urlobj)
    print(holidata["holidays"])
    holidaylist=holidata["holidays"]
    #print(response)
    print(joke)
    print(weather)
    print(ipdata)
    loc=ipdata['city']+', '+ipdata['region']

    return render_template("template.html",weather=weather,joke=joke,ip=ipdata['ip'],loc=loc,holidays=holidaylist)


if __name__ == "__main__":
  app.debug = True
  app.run()
