from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "OTT Student Demo — Running on Free App Service!"
