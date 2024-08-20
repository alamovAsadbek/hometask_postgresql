from main_files.decorator_func import log_decorator


class User:
    def __init__(self, user_data: dict):
        self.data = user_data

    @log_decorator
    def profile(self):
        pass
