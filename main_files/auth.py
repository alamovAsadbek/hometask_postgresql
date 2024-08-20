import hashlib
from datetime import datetime

from main_files.decorator_func import log_decorator


class Auth:
    def __init__(self):
        self.__admin_email = 'alamovasad@gmail.com'
        self.__developer_email = 'alamovasad55@gmail.com'
        self.__created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S').__str__()

    # login

    @log_decorator
    def login(self) -> bool:
        email: str = input('Email: ').strip()
        password: str = hashlib.sha256(input("Password: ").strip().encode('utf-8')).hexdigest()
        return True

    # register

    @log_decorator
    def register(self) -> bool:
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
        return True