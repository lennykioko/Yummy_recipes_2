"""tests logic for handling user's recipes"""

import unittest

from recipe import Recipe

class RecipeTestCase(unittest.TestCase):
    """class with methods to test recipe logic given different user data"""


    def setUp(self):
        """calls the Recipe class form the member module"""
        self.myrecipe = Recipe()

    def test_successful_recipe(self):
        """tests a successful recipe addition"""
        result = self.myrecipe.new_recipe('fried beans', 'dinner',
                                          'fry beans in hot oil for an hour')
        self.assertEqual(result, 'Successfully created new recipe', msg='Invalid recipe data')

    def test_empty_field(self):
        """tests for any missing field"""
        result = self.myrecipe.new_recipe('fried beans', '', 'fry beans in hot oil for an hour')
        self.assertEqual(result, 'Kindly fill in all fields', msg='Empty field')
