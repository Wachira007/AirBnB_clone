0x00. AirBnB clone - The console

0x01 Introduction

A team project to build a clone of AirBnB.

The console is a command interpreter to manage objects abstraction between objects and how they are stored.

To see the fundamental background of the project visit the Wiki.

The console will perform the following tasks:

    create a new object
    retrive an object from a file
    do operations on objects
    destroy an object

Storage

All the classes are handled by the Storage engine in the FileStorage Class.

0x02 Environment

    Style guidelines:
        pycodestyle (version 2.7.*)
        PEP8

All the development and testing was runned over an operating system Ubuntu 20.04 LTS using programming language Python 3.8.3. The editors used were VIM 8.1.2269, VSCode 1.6.1 and Atom 1.58.0 . Control version using Git 2.25.1.

0x03 Installation

git clone https://github.com/Mdigo12/AirBnB_clone.git

Change (cd) to the AirBnb directory and run the comman below

 ./console.py

Execution

In non-interactive mode

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

In the interactive mode

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

0x04 Testing

Python Unit Tests

    unittest module
    File extension .py
    Files and folders star with test_
    Organization:for models/base.py, unit tests in: tests/test_models/test_base.py
    Execution command: python3 -m unittest discover tests
    or: python3 -m unittest tests/test_models/test_base.py

run test in interactive mode

echo "python3 -m unittest discover tests" | bash

run test in non-interactive mode

To run the tests in non-interactive mode, and discover all the test, you can use the command:

python3 -m unittest discover tests



 
