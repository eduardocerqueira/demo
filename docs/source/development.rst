.. _development:


Setup development environment
=============================


Source Code
-----------

::

    $ git clone https://github.com/eduardocerqueira/demo.git


Installation
------------

Option 1: Start it on RPM
`````````````````````````

For development purposes, install following dependencies:

* python = 2.7
* python-pip

* Run the following ::

    $ workon demo
    $ pip install -r requirements/devel.txt


Option 2: Start it on virtualenv
````````````````````````````````

* After that, run ::

    $ pip install virtualenvwrapper

  and setup according to 'Setup' steps in ``/usr/bin/virtualenvwrapper.sh``.
  Then run ::

    $ mkvirtualenv demo --system-site-packages

* Run the following ::

    $ workon demo
    $ pip install -r requirements/devel.txt

  to activate *demo* virtualenv and install all the dependencies.


Option 3: Start it on Docker
````````````````````````````

* Install Docker: see the `official installation
  guide <https://docs.docker.com/installation/>`_ for details. Generally, it
  might be enough to run install it with ``yum`` and the run it. ::

    $ sudo yum install docker-engine
    $ sudo service docker start

* Use this command to build a new image ::

    $ sudo docker build -t <YOUR_NAME>/demo <the directory your Dockerfile is located>

* Run the container ::

    $ docker run -it -P -v $PWD:$PWD <YOUR_NAME>/demo python $PWD/driver.py --help

* Check the address

  #. Find the address of the docker machine (127.0.0.1 --> DOCKER_HOST).

  #. Find the mapped port of your running container ::

       $ sudo docker ps -l --> PORT

* Access it by visiting ``DOCKER_HOST:PORT`` in your web browser.

