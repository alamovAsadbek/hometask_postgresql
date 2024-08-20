from main_files.db import DatabaseManager
from main_files.decorator_func import log_decorator


class Developer:
    def __init__(self):
        self.__data_type = ['varchar', 'serial primary key', 'date', 'int', 'bigint', 'smallint', 'text', 'timestamp']
        self.__database_manager = DatabaseManager()

    # show all data types
    @log_decorator
    def show_data_type(self) -> None:
        formatted_types = ', '.join(self.__data_type)
        print('\n' + formatted_types + '\n')

    # show all columns
    @log_decorator
    def show_columns(self, columns_data: list) -> None:
        print('\n')
        for index, col in enumerate(columns_data):
            print(f'Column {index + 1}: Column name: {col[0]}, Column type: {col[1]}')
        return None

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

    # create new table
    @log_decorator
    def create_table(self) -> bool:
        all_tables = self.__database_manager.show_all_tables()
        columns_data: list = []
        table_name: str = input("Table name: ").strip().lower()
        if table_name in all_tables:
            print('Table already exists')
            return False
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

        if self.__database_manager.create_table(table_name=table_name, table_columns=columns_data):
            print("Table created successfully")
            return True
        print("Table already exists")
        return False

    # show all tables
    @log_decorator
    def show_table(self) -> bool:
        all_tables: list = self.__database_manager.show_all_tables()
        for index, table in enumerate(all_tables):
            print(f'\nTable {index + 1}: Table name: {table}')
        return True

    # add column to table
    @log_decorator
    def add_column(self) -> bool:
        all_tables: list = self.__database_manager.show_all_tables()
        self.show_table()
        choose_table: str = input("\nEnter table name: ").strip().lower()
        if choose_table in all_tables:
            column_name: str = input("Column name: ").strip().lower()
            self.show_data_type()
            column_type: str = input("Column type: ").strip().lower()
            if column_type in self.__data_type[0] or column_type in self.__data_type:
                if self.__database_manager.add_column(table_name=choose_table, column_name=column_name,
                                                      column_type=column_type):
                    print("Column added successfully")
                    return True
                print("Column already exists")
                return False
            else:
                print("Data type invalid")
                return False
        else:
            print('Table does not exist')
            return False

    # remove column
    @log_decorator
    def remove_column(self) -> bool:
        is_there = False
        all_tables: list = self.__database_manager.show_all_tables()
        self.show_table()
        choose_table: str = input("\nEnter table name: ").strip().lower()
        if choose_table in all_tables:
            all_column = self.__database_manager.show_all_column(table_name=choose_table)
            self.show_columns(all_column)
            choose_column: str = input("\nEnter column name: ").strip().lower()
            for col in all_column:
                if col[0] == choose_column:
                    is_there = True
            if not is_there:
                print("Column does not exist")
                return False
            if self.__database_manager.delete_column(table_name=choose_table, column_name=choose_column):
                print("Column removed successfully")
                return True
            print("Column removed failed")
            return False
        else:
            print("Table not found")
            return False

    # change column data type
    @log_decorator
    def change_column_type(self):
        pass
