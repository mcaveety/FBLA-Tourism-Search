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
        filteredData = filter.data  # starts with all location data
        filteredOptions = {}  # for storing the user's selections

        # Skips any unused filters
        for element_id, value in request.form.items():
            if value == "0" or value == "":
                continue

            # Calls the filtering function with the search (type/entry/data to check)
            filteredData = filter.locationsFilter(element_id, value, filteredData)
            # Stores the user's selection
            filteredOptions.update({element_id:value})

        # Filtered table is returned
        # Selected options are displayed
        filteredData = list(filteredData)  # Converting the generator to a list allows length detection
        return render_template("table.html", list=filteredData, options=filteredOptions)

# Help & Information page URL is set
# HTTP methods are default so data is received only
@app.route("/info")
def info_route():
    return render_template("info.html")

# Flask app is run, allowing access of the webpage
app.run(host="localhost", port=port)

