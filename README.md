# Democrance

This is Democrance demo which allow customer to create Quote and converted it to a policy

## Technologies stack overview

The project is a microservice web application developed using the following core technologies on the backend:

- Python 3.8.1
- Django framework 4.0.4
- PostgresSQL

## Dev env installation

Docker and docker-compose is a must.
Bootstrap all requirements with:

```bash
docker-compose up -d
```

Source code will be mounted in the api containers.

When adding new requirements in to the project, be sure to rebuild images with:

```bash
docker-compose build --no-cache
```

or

```bash
docker-compose up -d --build
```

Running app will be available at: http://localhost:8000/api/v1/

## Code style

The project is using Black formatter for automatic code formatting and Flake8 for style checking.

```bash
black .
flake8 .
```

## Command

This command will automatically init the DB with an admin user it will run with in docker-compose you don't have to run it manually
```bash
python manage.py create_admin
```

## Admin User

Default admin user will be created and the credentials are
```bash
"username": "admin"
"password": "admin"
```
