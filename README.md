# TSAI - MLOps - Session3

## Learning Objective ##
This week learned about the following topics.
* **What is Containerization?**
  
  A container is an encapsulation of software code with its dependencies so that it is functional, consistent and portable that can be run in any computing environment.

* **Difference between Containerization and Virtualization**

  In virtualization, physical machine is virtualized with technologies such as VMWare and VirtualBox to create separate simulated machines each with its own Operating System.  
  In Containerization, computational bubbles or environments are created on top of a single OS. These environments make each other mutually exclusive and at the same time fully functional and portable.
* **Microservices and Containerization**
  Microservice architecture is based on certain engineering principles that de-couples technological components and eases the complex software development by making smaller specialized modules/components and integrated with APIs.

* Docker
  It is an open source platform to build, deploy and manage Containerized applications in simpler and safer approach.
  * Dockerfile  
    It is blueprint of how docker container will be created. It is file with sequential commands for the container build.
  * Docker images  
    There can be visualized as equivalent to snapshots of containers. It is basically an immutable file with actual code and configurations that creates container upon execution.
  * Docker containers  
    These are actual containers or computations environments created on top of the OS running the application.
  * Docker Hub  
    It is one of the largest public repo of docker images contributed and managed by a large community and organizations.
  * Docker Daemon  
    It is service running on the OS to manage the docker implementations.
  * Docker Registry  
    It is a scalable open source storage and distribution system of docker images.
  * Docker commands  
    To see list of images:  
    ```docker images```  
    To create an image from a specific path:  
    ```docker build -t <img> .```  
    To run an image to create a container:  
    ```docker run -d -p <target port>:<defined port> <img>```  
    To see list of running containers:  
    ```docker ps```  
    To stop a container:  
    ```docker stop <container name or id. partial info is ok>```  
    To delete a container:  
    ```docker rm <container id or name>```  
    To delete an image:  
    ```docker rmi <img>```
  * Docker Networking
  * Docker Storage
  * Docker Compose
  
## Assignment Project ##
The task is to clone the GitHub project https://github.com/imadtoubal/Pytorch-Flask-Starter and make following enhancements to it and deploy to Heroku.
* Add option to select and upload multiple images at a time
* Allow only three images maximum at a time and show message accordingly
* Add dropdown option to navigate to Team/Developer information page
* Add option in dropdown to go to About page of project
* Store previously processed images and show up to 5 latest of them
  
**Changes made in the project**  
* Updated HTML templates to change the UI screens and links
* Used Python Closures technique to persist previously processed images and predicted results
* Updated Dockerfile to use lighter version of base image such as python:3.9.7-slim-buster to reduce docker image size

**Heroku Application Link**

Here is the implemented project on Heroku:
https://docker-pytorch-flask-app.herokuapp.com/
## How to use the project ##
Please follow the steps in order.
* Install docker on your system
* Create Heroku account if not created already
* Git clone the GitHub repo
* Go to local repo directory in terminal
* [Optional] Make changes in the project as per your requirement
* Run ```git add .``` (If any changes made in the project)
* Run ```git commit -m <commit related comment>``` (if any changes made in the project)
* Run ```heroku login```
* Run ```heroku container:login```
* Run ```heroku stack:set container```
* Run ```heroku create yourappname``` (Ignore the step if the app is already existing in Heroku)
* Run ```heroku git:remote -a yourappname```
* Run ```heroku container:push web --app yourappname```
* Run ```heroku container:release web --app yourappname```

Now you can visit the app on Heroku and test the application.
## [Optional] Test Changes in Project ##
If any changes are done in the Project locally you can test it locally before moving to Heroku.

**Test locally without Docker**

* Go to application directory in terminal
* Create and activate a virtual environment
* In virtual environment:
  * Run ```pip install Flask```
  * Run ```pip install torch torchvision```
  * Install any other libraries as per your need
* If windows OS:
  * Run ```set FLASK_APP=app.py```
  * Run ```set FLASK_ENV=development```
  * Run ```flask run```
* If Linux OS:
  * Run ```export FLASK_APP=app.py```
  * Run ```Export FLASK_ENV=development```
  * Run ```flask run```
* Take the local URL and test the app in the browser

**Test locally with Docker**

If the application is locally tested successfully as in the previous step, proceed with following steps.
* Update Dockerfile if required
* Go to app directory path in terminal and run ```docker build -t <dockerimage> .```
* If docker image got successfully created, to run the application execute ```docker run -d -p 5000:80 <dockerimage>```
* To check running container run ```docker ps```
* Go to localhost:5000 in browser to test the application
