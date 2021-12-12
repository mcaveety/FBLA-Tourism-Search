from flask import Flask, render_template

app = Flask(__name__)
port = 8080

@app.route("/")
def home_route():
    return "Home page"

@app.route("/test")
def test_route():
    return render_template("table.html", testing="This is the table text")

app.run(host="localhost", port=port)

