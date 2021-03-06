"""Test the recipes module
Created: 2018
Author: Lenny
"""

import unittest
from recipes import Recipe


class RecipeTests(unittest.TestCase):
    """Contain methods to test creating, updating and deleting"""


    def setUp(self):
        """set up important variables that will be available within all methods"""
        self.recipe = Recipe()
        self.existing_recipe = self.recipe.create('Grilled Chicken', 'chicken', 'grill the chicken')

    def test_no_empty_field(self):
        """test for successful recipe creation"""
        new = self.recipe.create('Chapati', 'chapo', 'fry the chapati')
        self.assertEqual(new, "Recipe created succesfully")

    def test_empty_field(self):
        """test for empty field in recipe creation"""
        new = self.recipe.create('Grilled Chicken', '', 'grill the chicken')
        self.assertEqual(new, "Please fill in all fields")

    def test_existing_title(self):
        """test for recipe creation using an existing title"""
        new = self.recipe.create('Grilled Chicken', 'chicken', 'grill the chicken')
        self.assertEqual(new, "Title already exists")

    def test_successful_update(self):
        """test for successful recipe update"""
        update = self.recipe.update('Grilled Chicken', 'lunch manenos', 'grill the chicken')
        self.assertEqual(update, "Sucessfully updated")

    def test_empty_update_field(self):
        """test for empty field in recipe update"""
        update = self.recipe.update('', 'lunch manenos', 'grill the chicken')
        self.assertEqual(update, "Please fill in all fields")

    def test_update_non_existing_title(self):
        """test for recipe creation using an existing title"""
        update = self.recipe.update('Homemeade bread', 'bread', 'bake the bread')
        self.assertEqual(update, "Recipe does not exist")

    def test_successful_deletion(self):
        """test for successful recipe deletion"""
        delete = self.recipe.delete('Grilled Chicken')
        self.assertEqual(delete, "Successfully deleted")

    def test_empty_delete_field(self):
        """test for empty field in recipe deletion"""
        delete = self.recipe.delete('')
        self.assertEqual(delete, "Please fill in all fields")

    def test_delete_non_existing(self):
        """test deleting a recipe that does not exist"""
        delete = self.recipe.delete('Sukuma Wiki')
        self.assertEqual(delete, "Recipe does not exist")

if __name__ == '__main__':
    unittest.main()
