import contextlib

import psycopg2

from config import config
from main_files.decorator_func import log_decorator


class DatabaseManager:

    # connect database
    @contextlib.contextmanager
    def connect(self):
        global connection
        try:
            connection = None
            params = config()
            connection = psycopg2.connect(**params)
            cursor = connection.cursor()
            yield cursor
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(f'Error: {error}')
        finally:
            if connection is not None:
                connection.close()

    # create table
    @log_decorator
    def create_table(self, table_name: str, data_type):
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
                print(f'Table {table_name} has been created')
        except psycopg2.errors.DuplicateDatabase:
            print(f'Table {table_name} already exists')
            return True
        except psycopg2.DatabaseError:
            print("Error while connecting to database")
            return False


if __name__ == '__main__':
    DatabaseManager().create_table('users')
