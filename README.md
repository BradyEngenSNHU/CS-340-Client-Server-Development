# CS-340-Client-Server-Development
This repository includes the main project from my class CS 340 Client Server Development


##  Functionality
This project is for Grazioso Salvare. It provides an easy way to access the database of animals, sort through dogs with specific training requirements, and have the data analyzed with charts. The functionality is shown below. By default the No Filters radio button is toggled. You can see the default state of the website below.

<img width="1586" height="792" alt="image" src="https://github.com/user-attachments/assets/350cb272-efff-4039-9449-6c539f3e07ed" />

The website’s graphs and data table updates when each of the different dog training settings is toggled. The three training settings are Water Rescue, Mountain Rescue, and Disaster Rescue. Below you can see each of the three training settings and the updated data. 

<img width="1583" height="801" alt="image" src="https://github.com/user-attachments/assets/4b66556c-02d0-4ed5-b4a7-cffa6dbd12c2" />

<img width="1574" height="801" alt="image" src="https://github.com/user-attachments/assets/8f2dfcdd-d418-44bb-93a6-b287528cb3dd" />

<img width="1581" height="807" alt="image" src="https://github.com/user-attachments/assets/e2ae6402-add1-47e5-866f-87568e83e63f" />

For some of the settings, the full graphs could not fit into the screenshot. Below is a full screenshot of the graphs when no filters are on.

<img width="1393" height="415" alt="image" src="https://github.com/user-attachments/assets/aea46acf-e9c9-4d20-9c36-33f533aa946f" />

## Tools
This website was made with MongoDB as the main database or the “model” component. MongoDB was chosen because of its simplicity, its flexibility, and it works great with python. MongoDB also has easy horizontally scalability. MongoDB can be paired with PyMongo to have a simple easy way of interacting with the database, this allows for simple and secure CRUD functionality in python without the need for using the Mongo shell. 
The “model” and “view” part of the web app is built in python using the Dash framework. Dash was chosen for its simplicity, scalability, and many tools that is comes with. Dash simplified this project by keeping the whole front end “view” of the project in python, it also keeps the “controller” in the python file by using callbacks and buttons to interact with the CRUD python file to get data from the “model”. 


## Resources
Dash core components: https://dash.plotly.com/dash-core-components
This dash documentation shows how to use dash and it’s basic functionality, and explains everything used in this project. 

PyMongo docs: https://www.mongodb.com/docs/languages/python/pymongo-driver/current/
This PyMongo documentation gives all the details for using PyMongo and this was used to make the CRUD functionality used in the dash app.


## Steps taken to Create this Project
1. The first step to complete this project was in MongoDB. First I created the animals collection for the data, then the animal data was uploaded to the collection and a user account was made for accessing the animals database.
2. Next, the python CRUD module was created. This module was created with PyMongo to provide basic create, read, update, and delete functionality for the Animals database. The user account made in MongoDB was programmed into this CRUD module to connect to the database. This acts as a main part of the “controller” of the MVC pattern.
3. Next the Dash python app was created. This app was created to make the “view” and part of the “controller” of the project. The app features all of the UI elements such as the data table, the pie chart, and the geolocation chart. This also contains calls to the Python CRUD module to get the data from the MongoDB database. 


## Challenges
Some challenges that happened when making this project were getting all the UI elements to work together and look correct. When making the pie chart, it was difficult to get the data looking correct with all the different types of dog breeds there were. The solution was to display the top ten dog breeds, then put the rest into one “other” category on the chart. Another challenge was tying together all the parts of the project and making them all work into the dash app. To solve this I has to ensure that each part worked well with proper functionality and thorough testing. 
