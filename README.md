## AirBnB
The acronym AirBnB means: "Air Bed and Breakfast,” is a service that lets property owners rent out their spaces to travelers looking for a place to stay.
The goal of this project AriBnB clone, is to deploy on a server, a simple copy of the AirBnB website.

###Project Description
(1)	This project is aim at developing an entire web application that simulates the behavior of the Airbnb platform. 
To proceed, we start with the Console/Interpreter. Then,
(2)	We proceed to the front-end(website) which shows the static and dynamic product of the project to the user. And next,
(3) 	We create a connection between the modules being created and database or files that stores the data being used. Finally,
(4)	We  create an API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them). 

## Console/Interpreter
This console or command interpreter provides us with a framework that enables us manipulate data without a visual interface, such as the Shell wich is perfect for development and debbuging

This command interpreter allows us to:
create the data model.
manage (create, update and destroy) objects via a console.
store and persist objects to a file (JSON file).

by running codes that:

=> Starts  the program `$ ./console.py`
=> Use the program `(hbnb) code`
	 example : `
		(hbnb) echo "hello world"
		(hbnb) hello world

## Front-end + Module & Data Storage + Api
All these are achieved simultaneouly as file creations progresses.



##Files and Directiries needed.

/models directory constains all classes used for the project.
basemodel.py file contains the base class (BaseModel) of all models in the project:

user.py - file contains the User class.
state.py - file contains the State class.
city.py - file contains the Cityclass.
amenity.py - file contains the Amenity class.
place.py - file contains the Place class.
review.py - file contains the Review class.
/models/engine directory contains the class that handles JASON serialization and deserialization.
file_storage.py - file contains FileStorage class.

/tests directory contains all unit test cases for this project.

console.py the console contains the entry point of the command interpreter.
