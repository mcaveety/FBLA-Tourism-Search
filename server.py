from flask import Flask

app = Flask(__name__)
port = 8080

@app.route("/")
def home_route():
    return "Home page"

app.run(host="localhost", port=port)