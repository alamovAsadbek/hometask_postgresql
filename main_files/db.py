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

    # show all tables
    @log_decorator
    def show_all_tables(self):
        with self.connect() as cursor:
            query = sql.SQL('''
            SELECT table_schema || '.' || table_name
            FROM information_schema.tables
            WHERE table_type = 'BASE TABLE'
            AND table_schema NOT IN ('pg_catalog', 'information_schema')
            ''')
            cursor.execute(query)
            tables = []
            for schema_table in cursor.fetchall():
                full_name = schema_table[0]
                if full_name.startswith('public.'):
                    table_name = full_name.split('.', 1)[1]
                    tables.append(table_name)
            return tables
