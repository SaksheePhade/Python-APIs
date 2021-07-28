import flask
import random

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>UID Generator : "+str(random.randint(1,1000000))+"</h1>"

app.run()