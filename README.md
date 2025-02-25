# Weather Query Django Project

This project is a Django-based application that queries weather information. It can be deployed manually or using Docker.

Before running this project, ensure you have the following tools installed:

- **Python 3.8+**
- **pgAdmin4** for PostgreSQL
- **Docker** (for Docker installation)
- **Docker Compose** (for Docker installation)


## 1. Setup

### Clone the repository

Clone the project from GitHub to your local machine:

```bash
git clone https://github.com/lolochek/django_weather_project
```

And then move to the project directory:

```bash
cd django_weather_project
```


## 2. Deployment

### Option 1: Docker installation

#### 1.1 Setup enviroment variables

You can set enviroment variables in docker-compose.yml:

```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_DB: your_db    # The name of your database
      POSTGRES_USER: your_user    # Your database username
      POSTGRES_PASSWORD: your_password   # Your database password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      DATABASE_HOST: db
      DATABASE_PORT: 5432    # The port your PostgreSQL instance is listening on (default is 5432)
      DATABASE_NAME: your_db     # The name of your database
      DATABASE_USER: your_user    # Your database username
      DATABASE_PASSWORD: your_password    # Your database password

volumes:
  postgres_data:
```
Ensure you replace **your_password**, **your_db**, **your_user** and other values with the appropriate credentials and settings specific to your environment.

#### 1.2 Build and run docker container

To create the container use:

```bash
docker-compose up --build
```

#### 1.3 Make database migrations

To run the container in the background, use the following command:

```bash
docker-compose up -d
```

Once the containers are running, you need to apply the migrations to set up the database schema:

```bash
docker-compose exec web python manage.py migrate
```

### Option 2: manual intallation

#### 2.1 Install dependencies

Required dependencies are described in the requirements.txt file. For installation, use the following command:

```bash
pip install -r requirements.txt
```

#### 2.2 Setup enviroment variables

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Database engine
        'NAME': 'your_db',  # The name of your database
        'USER': 'your_user',  # Your database username
        'PASSWORD': 'your_password',  # Your database password
        'HOST': 'localhost',  # The host where your database is running
        'PORT': '5432',  # The port your PostgreSQL instance is listening on (default is 5432)
    }
}
```
Ensure you replace **your_password**, **your_db**, **your_user** and other values with the appropriate credentials and settings specific to your environment.

#### 2.3 Make database migrations

Now that the database is set up and the settings are configured, run the Django migrations to create the necessary tables in the database:

```bash
python manage.py makemigrations
python manage.py migrate
```
Also you can create superuser (optional) using:

```bash
python manage.py createsuperuser
```

#### 2.4 Run Django server

Start Django server:

```bash
python manage.py runserver
```
This will start the application.


## 3 Access the application

The web application should now be running on http://localhost:8000/weather. You can open this URL in your web browser.
The web application features a form for entering the name of a city. After clicking the "Search" button, the current weather information for the specified city is displayed. 
Each search query is recorded in the database, allowing users to keep track of their searches. Users can view their search history by clicking the "View Search History" button.

