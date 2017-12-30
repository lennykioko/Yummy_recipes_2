"""tests logic for handling website users"""

import unittest

from member import Member


class MemberTestCase(unittest.TestCase):
    """class with methods to test website user logic given different user data"""


    def setUp(self):
        """calls the Member class form the member module"""
        self.myMembership = Member()

    def test_successful_registration(self):
        """tests a successful registration"""
        result = self.myMembership.register('lenny', 'lennykmutua@gmail.com',
                                            'secretive', 'secretive')
        self.assertEqual(result, 'Successful Registration', msg='Invalid registration credentials')

    def test_empty_field(self):
        """tests for any missing field during registration"""
        result = self.myMembership.register('', 'lennykmutua@gmail.com',
                                            'secretive', 'secretive')
        self.assertEqual(result, 'Kindly fill in all fields',
                         msg='Invalid registration credentials')

    def test_invalid_username(self):
        """tests for an invalid username (less than 3 characters)
        during registration
        """
        result = self.myMembership.register('L', 'lennykmutua@gmail.com',
                                            'secretive', 'secretive')
        self.assertEqual(result, 'Username should be at least 3 characters',
                         msg='username too short')

    def test_invalid_email(self):
        """tests for an invalid email address (does not satisfy email regex)
        during registration
        """
        result = self.myMembership.register('lenny', 'lenny', 'secretive', 'secretive')
        self.assertEqual(result, 'Invalid email address', msg='Invalid email address')

    def test_invalid_password(self):
        """tests for an invalid password (less than 8 characters) during registration"""
        result = self.myMembership.register('lenny', 'lennykmutua@gmail.com',
                                            'secret', 'secret')
        self.assertEqual(result, 'Password should have at least 8 characters',
                         msg='Password too short')

    def test_unmatching_passwords(self):
        """tests for an unmatching password and confirm
        password during registration
        """
        result = self.myMembership.register('lenny', 'lennykmutua@gmail.com',
                                            'password', 'secretive')
        self.assertEqual(result, 'Ensure password and confirm_password are identical',
                         msg='unmatching passwords')

    def test_successful_login(self):
        """tests a successful login"""
        self.myMembership.register('lenny', 'lennykmutua@gmail.com', 'secretive', 'secretive')
        result = self.myMembership.login('lennykmutua@gmail.com', 'secretive')
        self.assertEqual(result, 'Successful login', msg='failed login')

    def test_login_invalid_email(self):
        """tests for an invalid email address (does not match registration email) during login"""
        self.myMembership.register('lenny', 'lennykmutua@gmail.com', 'secretive', 'secretive')
        result = self.myMembership.login('lenny@gmail.com', 'secretive')
        self.assertEqual(result, 'Invalid Email address', msg='invalid login email')

    def test_login_invalid_password(self):
        """tests for an invalid password (does not match registration password) during login"""
        self.myMembership.register('lenny', 'lennykmutua@gmail.com', 'secretive', 'secretive')
        result = self.myMembership.login('lennykmutua@gmail.com', 'password')
        self.assertEqual(result, 'Invalid password', msg='invalid login password')
