# auth_menu
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
def admin_menu():
    pass


# developer menu
def developer_menu():
    pass


# user menu
def user_menu():
    pass
