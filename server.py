from flask import Flask, render_template, request

app = Flask(__name__)
port = 8080

@app.route("/", methods=["GET", "POST"])
def home_route():
    if request.method == "GET":
        return render_template("table.html", testing="CSV File Data")
    # Should this be an IF statement?
    if request.method == "POST":
        print(request.form.get("name"))
        print(request.form.get("attractionType"))
        print(request.form.get("townName"))
        print(request.form.get("groupSize"))
        print(request.form.get("locationRating"))
        return "Search successful"

app.run(host="localhost", port=port)

