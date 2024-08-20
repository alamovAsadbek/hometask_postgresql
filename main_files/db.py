import contextlib

import psycopg2

from config import config
from main_files.decorator_func import log_decorator


class DatabaseManager:

    # connect database
    @contextlib.contextmanager
    def connect(self):
        try:
            connection = None
            params = config()
            connection = psycopg2.connect(**params)
            cursor = connection.cursor()
            yield cursor
            cursor.close()
            if connection is not None:
                connection.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(f'Error: {error}')

    # create users table
    @log_decorator
    def create_users_table(self):
        try:
            with self.connect() as cursor:
                cursor.execute('''CREATE TABLE IF NOT EXISTS USERS (
                id serial PRIMARY KEY,
                first_name varchar(50) not null,
                last_name varchar(50) not null,
                email varchar(50) unique not null,
                gender varchar(50) not null,
                birthday date not null,
                password varchar(500) not null,
                created_at timestamp not null, 
                );
                ''')
                cursor.connection.commit()
                print(f'Table has been created')
        except psycopg2.errors.DuplicateDatabase:
            print(f'Table already exists')
            return True
        except psycopg2.DatabaseError:
            print("Error while connecting to database")
            return False

    # create data in users table
    def append_data_to_users_table(self):
        pass
