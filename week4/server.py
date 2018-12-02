from flask import Flask

from req import get_weather

citi_id = 524901
apikey = 
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    print(__name__)
    return "Hi!"