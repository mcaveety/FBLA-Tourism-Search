# Import Flask for running & rendering the webpage
# Import filter Python file for use in filtering based on user input
from flask import Flask, render_template, request
import filter

# An instance of the Flask class is created
app = Flask(__name__)
port = 8080

# Main page URL is set to the default
# HTTP methods set so data can be sent & received
@app.route("/", methods=["GET", "POST"])
def home_route():
    # HTTP method type is checked
    if request.method == "GET":
        # On page load, the full table data is displayed
        return render_template("table.html", list=filter.data)
    if request.method == "POST":
        # On form submission, the data is filtered
        fltData = filter.data
        fltOptions = {}
        for element_id, value in request.form.items():
            if value == "0" or value == "":
                continue

            fltData = filter.locationsFilter(element_id, value, fltData)
            fltOptions.update({element_id:value})

        # Filtered table is returned
        # Selected options are displayed
        # Converting the dictionary to a list allows length detection
        fltData = list(fltData)
        #fltOptions = list(fltOptions)
        return render_template("table.html", list=fltData, options=fltOptions)

# Help & Information page URL is set
# HTTP methods default so data is received only
@app.route("/info")
def info_route():
    return render_template("info.html")

app.run(host="localhost", port=port)

