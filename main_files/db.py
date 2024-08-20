import psycopg2

from config import config


def connect():
    global connection
    try:
        connection = None
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        cursor.execute('SELECT VERSION()')
        cursor.fetchone()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f'Error: {error}')
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    connect()
