from flask import Flask, render_template, request
import filter

app = Flask(__name__)
port = 8080

@app.route("/", methods=["GET", "POST"])
def home_route():
    if request.method == "GET":
        return render_template("table.html", array=filter.data)
    if request.method == "POST":
        fltData = filter.data # filter.data is the original dataset
        for element_id, value in request.form.items():
            print(element_id, value) # just to see its looping
            if value == "0" or value == "":
                continue

            fltData = filter.locationsFilter(element_id, value, fltData)

        return render_template("table.html", array=fltData)

app.run(host="localhost", port=port)

