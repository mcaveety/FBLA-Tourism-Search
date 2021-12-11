from flask import Flask, render_template

app = Flask(__name__)
port = 8080

@app.route("/")
def home_route():
    return "Home page"

@app.route("/test")
def test_route():
    return render_template("table.html", otter="cheese")

app.run(host="localhost", port=port)

