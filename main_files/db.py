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

    # show all tables
    @log_decorator
    def check_table(self, table_name: str):
        try:
            with self.connect() as cursor:
                cursor.execute('''''')
                print(f'Table {table_name} has been dropped')
        except psycopg2.errors.DuplicateDatabase:
            print(f'Table {table_name} already exists')
            return True
        except psycopg2.DatabaseError:
            print("Error while connecting to database")
            return False

    # create table
    @log_decorator
    def create_table(self):
        with self.connect() as cursor:
            cursor.execute('CREATE TABLE ')
