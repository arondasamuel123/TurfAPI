# Turf API
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Description
This is an API backend created for the Capstone Project. This API makes use of Django rest framework, as well as JWT Authentication using Django rest framework. This project shows the use of APIViews and serializers and the two work together to build a REST API.As well as other concepts learnt in the course as a whole.


## Author

Samuel Aronda

## Frontend Repo

## Deployed app


## DB diagram
![Turf](https://user-images.githubusercontent.com/31355212/78124539-7e95b900-7418-11ea-804c-85401af10a60.png)




# Installation

## Clone
    
```bash
    git clone https://github.com/arondasamuel123/TurfAPI.git
    
```
##  Create virtual environment
```bash
    python3.6 -m venv --without-pip virtual
    
```
## Activate virtual and install requirements.txt
```bash
   $ source virtual/bin/activate
   $ pip install - requirements.txt
    
```
## Run initial migration
```bash
   $ python3.6 manage.py makemigrations fullstack
   $ python3.6 manage.py migrate
    
```


## Run app
```bash
   $ python3 manage.py runserver
    
```


## API Endpoints
    POST /api/user- Sign up users
    POST /api/token/- Login users
    POST /api/v1/turf- Create a turf
    GET  /api/v1/turfs- Get all turfs
    GET  /api/v1/turf/id - Get turf by id
    PUT  /api/v1/turf/id- Update turf by id
    POST /api/v1/booking/id - Creating a booking by turf id
    GET api/v1/booking/id - Get a booking by turf id
    PATCH /api/v1/booking/id- Update a booking by turf id
    GET /api/v1/view/id- Get a booking by user id
    DELETE /api/v1/view/id- Delete a booking by user id
    GET /api/v1/tournaments- Get all tournaments
    GET /api/v1/tourna/id- Get  a tornament for a turf
    POST /api/v1/tournament/id- Create a tournament for a turf
    POST,GET,PUT /api/v1/schedule/<int:pk>- Create,update and get a schedule for a turf
    POST api/v1/join/id - Join a tournament
    GET api/v1/join/id - Get team in tournament
    
## Known Bugs


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Technologies Used
    Django
    PostgreSQL
    Django Rest Framework




