# Import Flask for running & rendering the webpage
# Import filter Python file for use in filtering based on user input
from flask import Flask, render_template, request
import filter

# An instance of the Flask class is created
app = Flask(__name__)
port = 8080

# Page URL is set and HTTP methods are defined
@app.route("/", methods=["GET", "POST"])
def home_route():
    # HTTP method type is checked
    if request.method == "GET":
        # On page load, the full table data is displayed
        return render_template("table.html", array=filter.data)
    if request.method == "POST":
        # On user input submission, the filtered data is generated
        fltData = filter.data
        for element_id, value in request.form.items():
            if value == "0" or value == "":
                continue

            fltData = filter.locationsFilter(element_id, value, fltData)

        return render_template("table.html", array=fltData) # Filtered table is returned

app.run(host="localhost", port=port)

