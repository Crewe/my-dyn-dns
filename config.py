# config.py
# Configuation file for the database connection

database = 'database_name'
username = 'database_username'
password = 'database_password'


def connectionString():
    return "postgresql+psycopg2://" + username + ":" + password + "@/" + database
