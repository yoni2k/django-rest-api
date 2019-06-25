# Profiles REST API

## What types of APIs provides:
* `/admin` - for adiministrations, having regular and admin users, being able to see different tables from admin API
* `/profile` - for managing users (getting a list, getting specific one, adding, deleting, updating)
* `/login` - for user authentication
* `/feed` - for user statuses (getting a list, getting specific one, adding, deleting, updating)

## Technical Django framework / REST framework features used:
* Working with Admin interface of Django framework
* Working with models to create a few tables in the database and migrations to update the Django framework database, connecting tables with foreign key
* Working with multiple applications and urls
* Working with views and overriding APIView and ViewSet (using Routers)
* Working with serializers for input of data and data validation, like ModelSerializer
* Working with permissions 
* Working with filters (by search)
* Working wiht token authentications
* Working with permissions to allow specific actions for specific users (mostly changing own info)
* Having some fields auto-generated, some read-only, some write only

## Also done as part of the course not related to Django and Rest APIs
* Working with Vagrant and Oracle Virtual box to create a stable known environment (on ubuntu)
* Working with .gitignore files
* Working with Python PIP with requrements.txt prerequisites file
* Working with Python in Atom IDE
* Working with HTTP POST, PUT, GET, PATCH and DELETE methods
