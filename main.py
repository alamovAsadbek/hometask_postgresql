from main_files.decorator_func import log_decorator


# auth_menu
@log_decorator
def auth_menu():
    text = '''
1. Register
2. Login
3. Logout
    '''
    print(text)
    try:
        pass
    except ValueError:
        print('Invalid menu')
        auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()


# admin menu
@log_decorator
def admin_menu():
    pass


# developer menu
@log_decorator
def developer_menu():
    pass


# user menu
@log_decorator
def user_menu():
    pass
