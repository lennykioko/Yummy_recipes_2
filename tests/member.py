"""contains logic to handle website users"""

import re


class Member(object):
    """class with methods allowing for user registration and login"""


    def __init__(self, username=None, email=None, password=None, confirm_password=None):
        """initalizes variables to be used in the class"""
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def register(self, username, email, password, confirm_password):
        """handles logic to verify data before registering a new user"""

        if username != "" and email != "" and password != "" and confirm_password != "":
            if len(username) >= 3:
                if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
                    if len(password) >= 8 and len(confirm_password) >= 8:
                        if password == confirm_password:

                            password = password.strip()
                            confirm_password = confirm_password.strip()

                            global registered_users

                            registered_users = {}
                            registered_users[email] = {}
                            registered_users[email]['username'] = username
                            registered_users[email]['email'] = email
                            registered_users[email]['password'] = password
                            registered_users[email]['confirm_password'] = confirm_password

                            return 'Successful Registration'

                        return 'Ensure password and confirm_password are identical'

                    return 'Password should have at least 8 characters'

                return 'Invalid email address'

            return 'Username should be at least 3 characters'

        return 'Kindly fill in all fields'


    def login(self, email, password):
        """handles logic to login an already registered users"""

        if email in registered_users:
            password = password.strip()
            if password == registered_users[email]['password']:
                return 'Successful login'

            return 'Invalid password'

        return 'Invalid Email address'
