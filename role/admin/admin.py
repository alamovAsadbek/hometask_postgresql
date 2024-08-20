from main_files.decorator_func import log_decorator

data_type = '''
1. 
'''


class Admin:
    @log_decorator
    def check_data_type(self):
        pass

    @log_decorator
    def create_table(self):
        table_data: dict = dict()
        table_name: str = input("Table name: ").strip()
        print("Enter column👇: ")
        print("Type exit to exit❌")
        while True:
            column_name: str = input("Column name: ").strip()
            if column_name == "":
                print("Please enter a valid column name.")
                continue
            elif column_name == "exit":
                print("Exit")
                break
            column_type: str = input("Column type: ").strip()
            if column_type == "":
                print("Please enter a valid column type.")
                continue
            elif column_type == "exit":
                print("Exit")
                break
            table_data[column_name] = column_type

        print(table_data)
