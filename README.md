![banner](https://i.imgur.com/RuiyIOR.jpg)

# AirBnB clone
This is a console application designed to mimic some of the functionalities of the popular online vacation rental marketplace, Airbnb. With this app, users can view, create, update, and delete properties and their corresponding attributes such as location, users, amenities, reviews, price, and more.

## Requirements of the project
To do this project we had to learn:
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is _*args_ and how to use it
* What is _**kwargs_ and how to use it
* How to handle named arguments in a function
* How to do a unittest

## The console
This command line interpreter can:

* Manage objects: create, update, destroy, etc...
* Retrieve an object from a file, a database etc...
* Do some operations on objects (count, compute stats, etc...)
* Update attributes of an object

## Getting started
At first, you have to clone this repository in your machine using this command:

```bash
$ git clone https://github.com/sezfabian/AirBnB_clone.git
```

Then, go inside it:
```bash
$ cd AirBnB_clone
```

Finally, you can use the console this way:
```bash
$ ./console.py
```

## Usage
Interactive mode
```bash
$ ./console.py

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
(hbnb) quit
$
```

Non interactive mode
```bash
$ echo "help" | ./console.py

(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```

## Available commands and its usage:

| Command       |              Syntax                       |     Output                |
| :------------ | :---------------------------------------: | ------------------------: |
| EOF           | EOF                                       | Exit interpreter          |
| all           | all [class_name]                          | Displays every instance   |
|               |                                           | of class name             |
| count         | count [class_name]                        | Counts the instances of   |
|               |                                           | specified class           |
| create        | create [class_name]                       | create a new instance with|
|               |                                           | specified name            |
| destroy       | destroy [class_name] [object_id]          | Deletes all attributes of |
|               |                                           | class_name.object_id      |
| help          | help [option]                             | Shows the help for        |
|               |                                           | specified option          |
| quit          | quit                                      | Exit interpreter          |
| show          | show [class_name] [object_id]             | Displays all attributes   |
| update        | update [class_name] [object_id]           | Modifies specified        |
|               | [update_key] [update_value]               | attribute                 |

