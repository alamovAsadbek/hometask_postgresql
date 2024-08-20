import threading

from main_files.db import DatabaseManager
from main_files.decorator_func import log_decorator


class Admin:
    def __init__(self):
        self.__data_type = ['varchar', 'serial primary key', 'date', 'int', 'bigint', 'smallint', 'text', 'TIMESTAMP']

    # show all data types
    @log_decorator
    def show_data_type(self) -> None:
        formatted_types = ', '.join(self.__data_type)
        print('\n' + formatted_types + '\n')

    # show all columns
    @log_decorator
    def show_columns(self):
        pass

    @log_decorator
    def create_table(self):
        database_manager = DatabaseManager()
        columns_data: list = []
        table_name: str = input("Table name: ").strip()
        print("Enter column👇: ")
        print("Type exit to exit❌")
        while True:
            column_name: str = input("\nColumn name: ").strip()
            if column_name == "":
                print("Please enter a valid column name.")
                continue
            elif column_name == "exit":
                print("Exit")
                break
            print("Enter data type👇")
            self.show_data_type()
            column_type: str = input("Enter data type name: ").strip().lower()
            if 'varchar' in column_type:
                columns_data.append((column_name, column_type))
            elif column_type in self.__data_type[0] or column_type in self.__data_type:
                columns_data.append((column_name, column_type))
            elif column_type == "exit":
                print("Exit")
                break
            else:
                print("Please enter a valid data type.")
                continue
            for index, col in enumerate(columns_data):
                print(f'\nColumn {index + 1}: Column name: {col[0]}, Column type: {col[1]}')

        threading.Thread(target=database_manager.create_table, args=(table_name, columns_data)).start()
        print("Table created successfully")
        return True


if __name__ == '__main__':
    admin = Admin()
    admin.create_table()
