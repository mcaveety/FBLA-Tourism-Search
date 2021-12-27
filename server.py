from flask import Flask, render_template, request
import filter

app = Flask(__name__)
port = 8080

@app.route("/", methods=["GET", "POST"])
def home_route():
    if request.method == "GET":
        return render_template("table.html", testing="CSV File Data")
    if request.method == "POST":
        print(request.form.get("name"))
        print(request.form.get("attractionType"))
        print(request.form.get("price"))
        print(request.form.get("groupSize"))
        print(request.form.get("locationRating"))
        filter.filterType("name", request.form.get("name"))
        filter.filterType("type", request.form.get("attractionType"))
        return "Search successful"

app.run(host="localhost", port=port)

