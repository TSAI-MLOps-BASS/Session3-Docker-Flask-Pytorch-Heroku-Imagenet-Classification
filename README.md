# TSAI - MLOps - Session3

## Learning Objective ##
This week learned about the following topics.
* Difference between Containerization and Virtualization
* Microservices and Containerization
* How does Containerization work?
* Docker
  * Dockerfile
  * Docker images
  * Docker containers
  * Docker Hub
  * Docker Daemon
  * Docker Registry
  * Docker commands
  * Docker Networking
  * Docker Storage
  * Docker Compose
  
## Assignment Project ##
The task is to clone the Github project https://github.com/imadtoubal/Pytorch-Flask-Starter and make following enhancements to it and deploy to Heroku.
* Add option to select and upload multiple images at a time
* Allow only three images maximum at a time and show message accordingly
* Add dropdown option to navigate to Team/Developer information page
* Add option in dropdown to go to About page of project
* Store previously processed images and show up to 5 latest of them

Here is the implemented project on Heroku:
https://docker-pytorch-flask-app.herokuappv2.com/
## How to use the project ##
Please follow the steps in order.
* Install docker on your system
* Create Heroku account if not already created
* Git clone the github repo
* Go to local repo in command prompt
* Run ```heroku login```
* Run ```heroku container:login```
* Run ```heroku create yourappname```
* Run ```heroku stack:set container```
* Run ```heroku container:push web --app yourappname```
* Run ```heroku container:release web --app yourappname```
Now you can visit the app on Heroku and test the application.