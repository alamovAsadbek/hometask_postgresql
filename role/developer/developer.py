from main_files.db import DatabaseManager
from main_files.decorator_func import log_decorator


class Developer:
    def __init__(self):
        self.__data_type = ['varchar', 'serial primary key', 'date', 'int', 'bigint', 'smallint', 'text', 'timestamp']

    # show all data types
    @log_decorator
    def show_data_type(self) -> None:
        formatted_types = ', '.join(self.__data_type)
        print('\n' + formatted_types + '\n')

    # show all columns
    @log_decorator
    def show_columns(self, columns_data: list) -> None:
        for index, col in enumerate(columns_data):
            print(f'\nColumn {index + 1}: Column name: {col[0]}, Column type: {col[1]}')

    # this function is check unique column
    @log_decorator
    def check_unique(self, data_type: str) -> str:
        while True:
            print(f'1. Unique \t2. Not unique')
            user_input: int = int(input('Choose: '))
            if user_input < 1 or user_input > 2:
                print('Invalid input')
                continue
            elif user_input == 1:
                data_type += ' unique'
            return data_type

    @log_decorator
    def create_table(self):
        database_manager = DatabaseManager()
        columns_data: list = []
        table_name: str = input("Table name: ").strip()
        print("Enter column👇: ")
        while True:
            print("\nType exit to exit❌")
            column_name: str = input("\nColumn name: ").strip().lower()
            if column_name == "":
                print("Please enter a valid column name.")
                continue
            elif column_name == "exit":
                print("Exit")
                break
            print("Enter data type👇")
            self.show_data_type()
            column_type: str = input("Enter data type name: ").strip().lower()
            if column_type == "exit":
                print("Exit")
                break
            elif 'varchar' in column_type:
                column_type = self.check_unique(column_type)
                columns_data.append((column_name, column_type))
            elif column_type in self.__data_type[0] or column_type in self.__data_type:
                column_type = self.check_unique(column_type)
                columns_data.append((column_name, column_type))

            else:
                print("Please enter a valid data type.")
                continue

            self.show_columns(columns_data)

        if database_manager.create_table(table_name=table_name, table_columns=columns_data):
            print("Table created successfully")
            return True
        print("Table already exists")
        return False
