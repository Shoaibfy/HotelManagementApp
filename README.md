# HotelManagementApp
### Prerequisites

You need to install the following packages for backend:

```
asgiref==3.2.3
Django==3.0.1
django-cors-headers==3.2.0
django-jsonfield==1.4.0
djangorestframework==3.11.0
pkg-resources==0.0.0
pytz==2019.3
six==1.13.0
sqlparse==0.3.0
psycopg2==2.7.4

```
### Installation

Clone the repository

```
git clone https://github.com/Shoaibfy/HotelManagementApp/.git
```

Setting up your virtual environment:

```
python3 -m venv .evnv
```

Activating Virtual  Environment

```
source .env/bin/activate
```
Once the repository is cloned and virtual environment set up, go to the directory where the requirements.txt(Catalogue-management-system/backend/) is and type the following code in your terminal:

```
pip install requirements.txt
```

### Database setup

If all requirements are installed, then Postgres database must be set up as per stated below.

Activating postgres
```
sudo su postgres

```
Get in to postgres shell
```
sqlite

```
To create a database for our Django project
```
CREATE DATABASE Hoteldb;

```
Create a database user which we will use to connect to and interact with the database. Set the password.
```
CREATE USER admin WITH PASSWORD 'admin';

```
Now, all we need to do is give our database user access rights to the database we created
```
GRANT ALL PRIVILEGES ON DATABASE Hoteldb TO admin;

```
Before running server make sure all migrations done. To exucute all migration
```
python3 manage.py migrate
python3 manage.py makemigrations

```

## Overall detail
```
Database Name: Hoteldb
Username: admin
Password: admin

```

Then to run the server, go to the directory '/Trip-Control/tripcontrol' and type the following code in terminal:

```
python3 manage.py runserver
```
