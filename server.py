from flask import Flask, render_template, request
import filter

app = Flask(__name__)
port = 8080

@app.route("/", methods=["GET", "POST"])
def home_route():
    if request.method == "GET":
        return render_template("table.html", array=filter.data)
    if request.method == "POST":
        fltData = filter.data
        filters = "Filtered by: "
        for element_id, value in request.form.items():
            print(element_id, value)
            if value == "0" or value == "":
                continue

            fltData = filter.locationsFilter(element_id, value, fltData)
        #     filters = element_id + ": " + value + " , "
        #
        # filters = filter.displayTypes(fltData, filters)
        # print(filters)
        return render_template("table.html", array=fltData)

app.run(host="localhost", port=port)


