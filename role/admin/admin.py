from main_files.db import DatabaseManager
from main_files.decorator_func import log_decorator


class Admin:
    def __init__(self):
        self.__database_manager = DatabaseManager()

    @log_decorator
    def show_data(self, data):
        for d in data:
            print(f"ID: {d[7]}, First name: {d[0]}, Last name: {d[1]}, Email: {d[2]}, Gender: {d[3]}, "
                  f"Birthday: {d[4].strftime('%Y-%m-%d')}, Created: {d[6].strftime('%Y-%m-%d %H:%M:%S')}")
        return True

    @log_decorator
    def show_all_users(self) -> bool:
        data = self.__database_manager.get_all_data(table_name='users')
        if data is None or len(data) == 0:
            print("No users found")
            return False
        if not self.show_data(data):
            print("Something went wrong")
            return False
        return True

    @log_decorator
    def show_all_female_users(self):
        data = self.__database_manager.get_data(key_data='female', table_name='users', key='gender')
        if data is None or len(data) == 0:
            print("No users found")
            return False
        if not self.show_data(data):
            print("Something went wrong")
            return False
        return True

    @log_decorator
    def show_all_male_users(self):
        data = self.__database_manager.get_data(key_data='male', table_name='users', key='gender')
        if data is None or len(data) == 0:
            print("No users found")
        if not self.show_data(data):
            print("Something went wrong")
            return False
        return True

    @log_decorator
    def delete_user(self):
        if not self.show_all_users():
            return False
        user_id: int = int(input("Enter user id to delete: "))
        self.__database_manager.delete_data(table_name='users', data_id=user_id)
        return True
