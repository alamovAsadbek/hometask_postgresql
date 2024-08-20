from main_files.decorator_func import log_decorator

data_type='''
1. 
'''
class Admin:
    @log_decorator
    def check_data_type(self):
        pass

    @log_decorator
    def create_table(self):
        table_name: str = input("Table name: ").strip()
