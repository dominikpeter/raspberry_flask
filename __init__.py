from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return 'this is a flask test page'

@app.route("/sinus")
def sinus(name=None):
    return render_template('sinus.html', name=name)



if __name__ == "__main__":
    app.run()
