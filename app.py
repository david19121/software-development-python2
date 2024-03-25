from flask import Flask,render_template
app = Flask(__name__)


@app.route("/")
def index():
    return "welcome to my python training institute"


@app.route("/add")
def add():
    a=20
    b=40
    c=a+b
    #return "this is the result of my addition: " + str(c)
    return render_template('show.html',finalscore=c)


@app.route("/multiply")
def multiply():
    d=20
    e=40
    f=d*e
    return "this is the result of my mutiplication: " + str(f)


@app.route("/division")
def division():
    g=20
    h=40
    i=20/40
    return "this is my result for division: " + str(i)











if __name__=='__main__':
    app.run(host="127.0.0.1",port=5001)
