from main_files.db import DatabaseManager
from main_files.decorator_func import log_decorator


class Admin:
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



