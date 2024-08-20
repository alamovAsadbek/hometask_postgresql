from main_files.auth import Auth
from main_files.decorator_func import log_decorator
from role.developer.developer import Developer


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
        auth = Auth()
        user_input: int = int(input('Choose menu: '))
        if user_input == 1:
            print('\nHome -> Register\n')
            pass
        elif user_input == 2:
            print('\nHome -> Login\n')
            print('Developer email: alamovasad55@gmail.com | \tDeveloper password: 0000')
            print('Admin email: alamovasad@gmail.com | \tAdmin password: 0000\n')
            result_login = auth.login()
            if not result_login['is_login']:
                print('Login failed.')
                auth_menu()
            elif result_login['role'] == 'developer':
                developer_menu()
            elif result_login['role'] == 'admin':
                admin_menu()
        elif user_input == 3:
            print("Goodbye!")
            return
        else:
            print('Invalid input')
            auth_menu()
    except ValueError:
        print('Invalid menu')
        auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()


# admin menu
@log_decorator
def admin_menu():
    text = '''
1. show all users
2. show all female users
3. show all male users
4. delete user
5. logout
    '''
    print(text)
    try:
        user_input: int = int(input('Choose menu: '))
        if user_input == 1:
            print('\nHome -> Show all users\n')
            pass
        elif user_input == 2:
            print('\nHome -> Show all female users\n')
            pass
        elif user_input == 3:
            print('\nHome -> Show all male users\n')
            pass
        elif user_input == 4:
            print('\nHome -> Delete user\n')
            pass
        elif user_input == 5:
            auth_menu()
        else:
            print('Invalid input')
            admin_menu()
    except ValueError:
        print('Invalid input')
        admin_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_menu()


# developer menu
@log_decorator
def developer_menu():
    text = '''
1. Create table
2. Add column to table
3. Remove column from table
4. Change column data type
5. Delete table
6. Show all tables
7. Logout
    '''
    print(text)
    try:
        developer = Developer()
        user_input: int = int(input('Choose menu: '))
        if user_input == 1:
            print('\nHome -> Create table\n')
            developer.create_table()
            developer_menu()
        elif user_input == 2:
            print('\nHome -> Add column to table\n')
            developer.add_column()
            developer_menu()
        elif user_input == 3:
            print('\nHome -> Remove column from table\n')
            developer.remove_column()
            developer_menu()
        elif user_input == 4:
            print('\nHome -> Change column data type\n')
        elif user_input == 5:
            print('\nHome -> Delete table\n')
        elif user_input == 6:
            print('\nHome -> Show all tables\n')
            developer.show_table()
            developer_menu()
        elif user_input == 7:
            pass
        else:
            print('Invalid input')
            developer_menu()
    except Exception as e:
        print(f'Error: {e}')
        developer_menu()


# user menu
@log_decorator
def user_menu():
    pass


if __name__ == '__main__':
    auth_menu()
