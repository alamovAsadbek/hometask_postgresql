import hashlib
from datetime import datetime

from main_files.db import DatabaseManager
from main_files.decorator_func import log_decorator


class Auth:
    def __init__(self):
        self.__admin_email = 'alamovasad@gmail.com'
        self.__admin_password = hashlib.sha256('0000'.encode('utf-8')).hexdigest()
        self.__developer_email = 'alamovasad55@gmail.com'
        self.__developer_password = hashlib.sha256('0000'.encode('utf-8')).hexdigest()
        self.__created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S').__str__()
        self.__database_manager = DatabaseManager()
        self.__active_user = None

    # login

    @log_decorator
    def login(self) -> dict:
        email: str = input('Email: ').strip()
        password: str = hashlib.sha256(input("Password: ").strip().encode('utf-8')).hexdigest()
        if email == self.__admin_email and password == self.__admin_password:
            return {'is_login': True, 'role': 'admin'}
        elif email == self.__developer_email and password == self.__developer_password:
            return {'is_login': True, 'role': 'developer'}
        get_user = self.__database_manager.get_data(table_name='users', key_data=email, key='email')
        if get_user is None:
            print('Email or Password is incorrect!')
            return {'is_login': False}
        elif get_user[0][2] == email and get_user[0][5] == password:
            print('Login successful!')
            return {'is_login': True, 'role': 'user', 'email': email}
        print('Email or Password is incorrect!')
        return {'is_login': False}

    # register

    @log_decorator
    def register(self) -> bool:
        columns = ['first_name', 'last_name', 'email', 'password', 'gender', 'birthday', 'created_at']
        first_name = input('First name: ').strip()
        last_name = input('Last name: ').strip()
        email = input('Email: ').strip()
        print("Choose gender: ")
        print("1.Male\t2.Female\t")
        gender: int = int(input("Gender: "))
        while True:
            if gender < 1 or gender > 2:
                print("Gender must be between 1 and 2")
                continue
            elif gender == 1:
                gender: str = 'male'
            elif gender == 2:
                gender: str = 'female'
            break
        birthday: str = input('Birthday (yyyy-mm-dd): ').strip()
        password = hashlib.sha256(input("Password: ").strip().encode('utf-8')).hexdigest()
        confirm_password: str = hashlib.sha256(input("Confirm Password: ").strip().encode('utf-8')).hexdigest()
        while password != confirm_password:
            print("Passwords do not match")
            password = hashlib.sha256(input("Password: ").strip().encode('utf-8')).hexdigest()
            confirm_password: str = hashlib.sha256(input("Confirm Password: ").strip().encode('utf-8')).hexdigest()
        values = [first_name, last_name, email, password, gender, birthday, self.__created_at]
        self.__database_manager.add_data(table_name='users', columns=columns, values=values)
        print("Registered!")
        return True
