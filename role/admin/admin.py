from main_files.decorator_func import log_decorator


class Admin:
    @log_decorator
    def show_all_users(self):
        pass

    @log_decorator
    def show_all_female_users(self):
        pass

    @log_decorator
    def show_all_male_users(self):
        pass

    @log_decorator
    def delete_user(self):
        pass
