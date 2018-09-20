#Mohammed Jamil
#SoftDev1 pd06
#K#08 -- Fill Yer Flask
#2018-09-20

from flask import Flask
app = Flask(__name__) #instantiates the Flask class using a constructor

@app.route('/')
def home():
    return '''
    <h1><a href="/0">Page 0</a></h1><br>
    <h1><a href="/1">Page 1</a></h1><br>
    <h1><a href="/2">Page 2</a></h1><br>
    '''

@app.route('/0')
def pg0():
    return '<img src="https://q4j2g5j9.stackpathcdn.com/ddg-dream/0e3fe939bb5884b1de989ad1994289a7e3a3515b.jpg" alt=https://q4j2g5j9.stackpathcdn.com/ddg-dream/0e3fe939bb5884b1de989ad1994289a7e3a3515b.jpg><br>Created using DeepDreamGenerator'
@app.route('/1')
def pg1():
    return '<img src="https://q4j2g5j9.stackpathcdn.com/ddg-dream/acad13f30d5a7e78da2836168a833a0b73c085bc.jpg" alt=https://q4j2g5j9.stackpathcdn.com/ddg-dream/0e3fe939bb5884b1de989ad1994289a7e3a3515b.jpg><br>Created using DeepDreamGenerator'
@app.route('/2')
def pg2():
    return '<img src="https://q4j2g5j9.stackpathcdn.com/ddg-dream/77abcf601565f6cdad7f5f510560d37373bc183a.jpg" alt=https://q4j2g5j9.stackpathcdn.com/ddg-dream/77abcf601565f6cdad7f5f510560d37373bc183a.jpg><br>Created using DeepDreamGenerator'

app.debug = True
app.run()