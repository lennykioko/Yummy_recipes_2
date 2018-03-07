"""Test the users module
Created: 2018
Author: Lenny
"""

import unittest
from users import User


class UserTests(unittest.TestCase):
    """Contain methods to test user signup and login"""


    def setUp(self):
        """set up important variables that will be available within all methods"""
        self.user = User()
        self.login_credentials = self.user.signup('lennykioko@gmail.com', 'lenny', 'mysecret', 'mysecret')
    
    def test_no_empty_field(self):
        """test a successful signup"""
        account = self.user.signup('markmutua@gmail.com', 'lenny', 'mysecret', 'mysecret')
        self.assertEqual(account, "successful account creation")
    
    def test_empty_field(self):
        """test for any empty field during signup"""
        account = self.user.signup('lennykmutua@gmail.com', '', 'mysecret', 'mysecret')
        self.assertEqual(account, "Please fill in all fields")

    def test_invalid_email(self):
        """test for an email that doesn't match email regex"""
        account = self.user.signup('lennykmutuagmail.com', 'lenny', 'mysecret', 'mysecret')
        self.assertEqual(account, "Invalid Email")

    def test_existing_email(self):
        """test for signup using an existing email"""
        account = self.user.signup('lennykmutua@gmail.com', 'lenny', 'mysecret', 'mysecret')
        account_2 = self.user.signup('lennykmutua@gmail.com', 'mark', 'mysecret2', 'mysecret2')
        self.assertEqual(account_2, "Email already exists")

    def test_good_password(self):
        """test for password that is at least 8 charcters long"""
        account = self.user.signup('nickmwenda@gmail.com', 'nick', 'mysecret', 'mysecret')
        self.assertEqual(account, "successful account creation")
    
    def test_short_password(self):
        """test for password that is shorter than 8 charcters long"""
        account = self.user.signup('lionelmessi@gmail.com', 'nick', 'cret', 'cret')
        self.assertEqual(account, "Password needs to be at least 8 charcters long")
    
    def test_correct_confirm_password(self):
        """test for confirm password that is identical to password"""
        account = self.user.signup('cristianjames@gmail.com', 'chris', 'mysecret', 'mysecret')
        self.assertEqual(account, "successful account creation")

    def test_wrong_confirm_password(self):
        """test for confirm password that is different from password"""
        account = self.user.signup('mikemyles@gmail.com', 'chris', 'mysecret', 'mysecret10')
        self.assertEqual(account, "Password not equal to confirm_password")

    def test_successful_login(self):
        """test for successful login"""
        login = self.user.login('lennykioko@gmail.com', 'mysecret')
        self.assertEqual(login, "succcessful login")

    def test_empty_login_field(self):
        """test for any empty field during login"""
        login = self.user.login('lennykioko@gmail.com', '')
        self.assertEqual(login, "Please fill in both fields")

    def test_invalid_login_email(self):
        """test for an email that doesn't match email regex"""
        login = self.user.login('lennykiokogmail.com', 'mysecret')
        self.assertEqual(login, "Invalid Email")
    
    def test_email_not_exist(self):
        """test for login using a non-existent email"""
        login = self.user.login('lennymureithi@gmail.com', 'mysecret')
        self.assertEqual(login, "Email does not exists")

    def test_invalid_login_password(self):
        """test for login using an invalid password"""
        login = self.user.login('lennykioko@gmail.com', 'mysecret233')
        self.assertEqual(login, "Invalid password")
  

if __name__ == '__main__':
    unittest.main()
   