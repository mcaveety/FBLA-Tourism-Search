from flask import Flask, render_template, request
import filter

app = Flask(__name__)
port = 8080

@app.route("/", methods=["GET", "POST"])
def home_route():
    if request.method == "GET":
        return render_template("table.html", array=filter.fltData)
    if request.method == "POST":
        print(request.form.get("name"))
        print(request.form.get("type"))
        print(request.form.get("price"))
        print(request.form.get("groupSize"))
        print(request.form.get("rating"))

        return "Search successful"

app.run(host="localhost", port=port)

