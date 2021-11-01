# GAME OF THRONES API

## Project setup

### Prerequisites

Apps to install:
- [Git](https://git-scm.com/downloads) (1.7.10 or above)
- Docker
- Docker Compose

### Installation

1. download or clone **develop** branch of the project
```bash
git clone --single-branch --branch master git@github.com:Ricardo50696/got_proj.git
```
2. install and run the project: 
```
docker-compose build
docker-compose up
```
4. run migrations
```bash
docker-compose exec admin python manage.py migrate
```
5. create a user to access the backoffice. Run the command below, and you'll be prompted for a username, email, and password
```bash
docker-compose exec admin python manage.py createsuperuser
```
6. populate GOT episodes
```bash
docker-compose exec admin python manage.py populate_got
```
or import from a fixture
```bash
docker-compose exec admin python manage.py loaddata db.json
```

# Paths

## Endpoints
- Swagger [http://0.0.0.0:8000/api/swagger/](http://0.0.0.0:8000/api/swagger/)
- Redoc [http://0.0.0.0:8000/api/redoc/](http://0.0.0.0:8000/api/swagger/)

## Admin backoffice

- Admin [http://0.0.0.0:9000/admin](http://0.0.0.0:9000/admin)