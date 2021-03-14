from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase


CREATE_DB = "CREATE DATABASE exam2"

CONFIG = {
    "user": "postgres",
    "password": "coderslab",
    "host": "127.0.0.1",
}

DB_USER = "postgres"
DB_PASSWORD = "coderslab"
DB_HOST = "127.0.0.1"

try:
    cnx = connect(**CONFIG)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DB)
        print("Database created")
    except DuplicateDatabase as e:
        print("Database exists ", e)
    cnx.close()
except OperationalError as e:
    print("Connection Error: ", e)