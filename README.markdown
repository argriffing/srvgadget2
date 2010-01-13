Description
-----------

This project serves a small dynamic web application without
requiring root privileges.
Multiple web apps are made available through a basic plugin architecture.
The main purpose of this project is as a template for
developing more useful applications.


Requirements
------------

This project has the following dependencies:

* A recent version of [python](http://www.python.org/) (2.6+).
* The [argparse](http://code.google.com/p/argparse/) module.
* The [cherrypy](http://www.cherrypy.org/) module (3.0+).
* The [epydoc](http://epydoc.sourceforge.net/) documentation program.


Usage
-----

To tell the web app to start listening on 127.0.0.1:8080:

    python run.py

For more options:

    python run.py -h

You might want to run the program [in the background]
(http://apps.carleton.edu/curricular/cs/resources/source/bg_progs/).

When the program is run,
epydoc creates a subdirectory called 'html'
in the current directory.
