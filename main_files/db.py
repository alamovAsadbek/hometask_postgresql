import contextlib

import psycopg2
from psycopg2 import sql

from main_files.config import config
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
    def create_table(self, table_name: str, table_columns):
        try:
            with self.connect() as cursor:
                query = sql.SQL('CREATE TABLE IF NOT EXISTS {} ({})').format(
                    sql.Identifier(table_name),
                    sql.SQL(', ').join(
                        sql.SQL('{} {}').format(
                            sql.Identifier(col_name),
                            sql.SQL(col_type)
                        ) for col_name, col_type in table_columns
                    )
                )
                cursor.execute(query)
                cursor.connection.commit()
                return True
        except psycopg2.errors.DuplicateDatabase:
            return True
        except psycopg2.DatabaseError:
            return False

    # # create data in users table
    # def append_data_to_users_table(self):
    #     if not self.create_table():
    #         print('Database creation failed')
    #         return False
    #     with self.connect() as cursor:
    #         cursor
