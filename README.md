# BackendAssignment

The project is created as assignment.

## Installation

```shell
# Clone the repo
git clone https://github.com/dextrop/BackendAssignment
cd BackendAssignment/

# Make sure you have created a virtual environment before starting to setup

# Install Dependencies 
pip3 install -r requirements.txt
```

## Migration

Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.
Before starting migration make sure postgres is running properly on port 5432 also replace

```
'NAME': 'DB_NAME',
'USER': 'DB_USER',
'PASSWORD': 'DB_PASSWORD'
```

variables from `BackendAssignment/settings.py` as per desire configration.

Once DB settings are properly configure use the below command to run migration for the server

```
python3 manage.py makemigrations api
python3 manage.py migrate
```

## Run Server

Once installation & migrations are done user can run the server. To run server use below command

```python3 manage.py runserver 0.0.0.0:8000```

## Testing

Once could find postman script for testing the server under `tools/postman`. Use postman to test the API's