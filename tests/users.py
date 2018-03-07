"""Handle credentials of all users
Created: 2018
Author: Lenny
"""
import re

all_users = {}


class User(object):
    """Contain user signup and login methods"""


    def signup(self, email='', username='', password='', confirm_password=''):
        """verify signup credentials and add them to the all_users dictionary"""
        global all_users
        if email != '' and username != '' and password != '' and confirm_password != '':
            if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
                if email not in all_users.keys():
                        if len(password) >= 8:
                            if password == confirm_password:
                                all_users[email] = [email, username, password, confirm_password]
                                return "successful account creation"

                            return "Password not equal to confirm_password"
                        return "Password needs to be at least 8 charcters long"
                return "Email already exists"
            return "Invalid Email"
        return "Please fill in all fields"


    def login(self, email='', password=''):
        """verify login credentials loginthe user"""
        global all_users
        if email != '' and password != '':
            if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
                if email in all_users.keys():
                    if password.strip() == all_users[email][2]:
                        return "succcessful login"

                    return "Invalid password"
                return "Email does not exists"
            return "Invalid Email"
        return "Please fill in both fields"
