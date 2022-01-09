# FBLA-Tourism-Search

## 2021-2022 FBLA Project
Created by Michelle McAveety at Freedom High School for the FBLA Coding and Programming competition

***

### Purpose
+ A program created to assist in searching through popular tourist attractions in the state of Florida
+ Aims to provide a large selection of attractions and search options, creating meaningful results

### Features

+ Lists all available tourist attractions
+ Filter the list search by attraction name, type, group size, rating, and price
+ Allows easy filtering through accessible dropdown menus
+ Non-case-sensitive searching
+ Displays additional information such as attraction descriptions, addresses, and phone numbers
+ 185 entries to search through
+ Help & Information page provided for additional details on the program
+ Data file backs up each time the program is run to locations2.json

***

### Instructions to Run

1. Head to the Releases section for this repository and download "Florida_Tourist_Attractions.exe" [(Version 1.0.0)](https://github.com/meepowlz/FBLA-Tourism-Search/releases/tag/v1.0.0)
2. Double-click the file to run it. A popup dialog may appear stating that "Windows protected your PC". Click "More info", then "Run anyway"
3. A black box command line will open. This indicates that the program is running. Open your internet browser of choice (ex. Google Chrome, Firefox, Internet Explorer, etc.)
4. Head to the URL listed in the command line, [http://localhost:8080/](http://localhost:8080/)
5. Interact with the program as desired
6. To terminate the program, close the command line window, or press CTRL + C when in the window

***
### Data Sources & Other Credits

**Data**
+ All attraction name, address, telephone, and description data was accessed from https://www.florida-backroads-travel.com/florida-tourist-attractions.html
+ Entries were omitted in scenarios where the aforementioned data was missing or inconsistent
+ Data was unaltered except to improve clarity or program functionality
+ Attraction type, group size, rating, and price data were generated for purposes of program search functionality 
+ Attraction type was assigned algorithmically where "museum" or "park" was present in attraction name. Remaining entries were manually assigned attraction types
+ Attraction price was algorithmically assigned based on attraction description and manually checked for accuracy
+ Attraction group size was algorithmically assigned based on attraction type. In instances where attraction type was "other", group size was manually assigned
+ Attraction rating was pseudorandomly assigned to each entry

**Credits**
Written in Python, HTML, and CSS, using .json format to store data
+ A segment of code used in filter.py was taken from https://stackoverflow.com/a/13790741
+ Flask used to run the local webserver https://flask.palletsprojects.com/en/2.0.x/
+ Jinja was used for HTML templating https://jinja.palletsprojects.com/en/3.0.x/
+ PyInstaller was used to bundle the program into a .exe file for easy use
