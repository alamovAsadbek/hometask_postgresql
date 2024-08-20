from main_files.decorator_func import log_decorator


class User:
    def __init__(self, user_data: dict):
        self.data = user_data

    @log_decorator
    def profile(self):
        print(f'First name: {self.data.get("first_name")}\nLast name: {self.data.get("last_name")}\n'
              f'Email: {self.data.get("email")}\nGender: {self.data.get("gender")}, '
              f'Birthday: {self.data.get("birthday")}')
        return True
