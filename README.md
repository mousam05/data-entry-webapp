# data-entry-webapp
A simple web application using Flask in Python for entering and searching data in remote MySQL database

### Setting up

This project is written in Python 3. The following packages (and their dependencies) must be installed:
* `flask`
* `MySQLdb`
* `datetime`

### Running the project

Clone the project. Then run the following command in a terminal:
`python3 run.py`

Next, open a browser, type `127.0.0.1:5000` in the address bar, and hit enter. You will see a webpage containing some forms and buttons. This is the main (and only) webpage of the project. Your computer must be connected to the internet to communicate with the MySQL server. That's it!

### The experience

When I read the problem statement, the first thought in my mind was the Flask web framework in Python, since I have earlier used the same in a [previous project](https://github.com/mousam05/restaurant-aggregator) of mine and Flask is a simple way of interacting with GET, POST requests from Python.

Using some tutorials on the web, I quickly designed the web forms on the webpage and added minimal UI enhancements to maintain a simple and clear interface.

Then, the next step was to code the business logic behind the webpage. There were two parts: inserting/updating the database, and retrieving from the database. I wrote two separate functions for this.

Once I was done with the database handling part, I moved on to the web requests part. Flask makes it very easy to write handlers for web forms. Essentially, when the *submit* buttons are pressed, I am just calling the database handlers I wrote earlier. The page is refreshed and the results/status from the earlier operation are shown as a message at the bottom of the page.

The challenging part of this project was the testing. I had to test for all scenarios, like connection errors with the database, invalid data entered in the form, etc. This proved to be the most time-consuming part (a couple of hours).

### Screenshots

Entering data in the web form:

![](https://github.com/mousam05/data-entry-webapp/blob/master/entering_data.png "Image1")

On successful insertion:

![](https://github.com/mousam05/data-entry-webapp/blob/master/entered_success.png "Image2")

Searching for a record that exists:

![](https://github.com/mousam05/data-entry-webapp/blob/master/search1.png "Image3")
![](https://github.com/mousam05/data-entry-webapp/blob/master/search_found.png "Image4")

Searching for a record that does not exist:

![](https://github.com/mousam05/data-entry-webapp/blob/master/search2.png "Image5")
![](https://github.com/mousam05/data-entry-webapp/blob/master/search_not_found.png "Image6")


