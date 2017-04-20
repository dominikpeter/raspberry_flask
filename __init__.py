from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return 'this is a flask test page'

@app.route("/sinus")
def sinus():
    return render_template('sinus.html')



if __name__ == "__main__":
    app.run()
