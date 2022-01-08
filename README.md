# FBLA-Tourism-Search

***

### 2021-2022 FBLA Project
Created by Michelle McAveety at Freedom High School for the FBLA Coding and Programming competition

***

### Purpose
A program created to assist in searching popular tourist attractions in the state of Florida

### Features

+ Lists all available tourist attractions
+ Filter the list search by attraction name, type, group size, rating, and price
+ 185 entries to search through
+ Help & Information page provided for additional details on the program
+ Data file backs up each time the program is run to locations2.json

***
### Disclaimers

+ All attraction name, address, telephone, and description data was accessed from https://www.florida-backroads-travel.com/florida-tourist-attractions.html
+ Entries were omitted in scenarios where the aforementioned data was missing or inconsistent
+ Data was unaltered except to improve clarity or program functionality.
+ Attraction type, group size, rating, and price data were generated for purposes of program search functionality. 
+ Attraction type was assigned algorithmically where "museum" or "park" was present in attraction name. Remaining entries were manually assigned attraction types.
+ Attraction price was algorithmically assigned based on attraction description and manually checked for accuracy.
+ Attraction group size was algorithmically assigned based on attraction type. In instances where attraction type was "other", group size was manually assigned.
+ Attraction rating was pseudorandomly assigned to each entry.