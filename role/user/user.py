from main_files.db import DatabaseManager
from main_files.decorator_func import log_decorator


class User:
    def __init__(self, user_data):
        self.database_manager = DatabaseManager()
        self.data = user_data

    @log_decorator
    def profile(self):
        self.data = self.database_manager.get_data(table_name='users', key_data=self.data, key='email')[0]
        print(f'First name: {self.data[0]}\nLast name: {self.data[1]}\n'
              f'Email: {self.data[2]}\nGender: {self.data[3]}, '
              f'Birthday: {self.data[4].strftime("%Y-%m-%d")}')
        return True
