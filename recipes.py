"""Handle data on recipes
Created: 2018
Author: Lenny
"""

all_recipes = {}


class Recipe(object):
    """Contain recipe creation, update and delete methods"""


    def create(self, title='', category='', description=''):
        """create a new recipe"""
        global all_recipes
        if title != '' and category != '' and description != '':
            if title not in all_recipes:
                all_recipes[title] = [title, category, description]
                return "Recipe created succesfully"
            return "Title already exists"
        return "Please fill in all fields"
    
    def update(self, title='', category='', description=''):
        """update an existing recipe"""
        global all_recipes
        if title != '' and category != '' and description != '':
            if title in all_recipes:
                all_recipes[title] = [title, category, description]
                return "Sucessfully updated"
            return "Recipe does not exist"
        return "Please fill in all fields"
    
    def delete(self, title=''):
        """delete an existing recipe"""
        global all_recipes
        if title != '':
            try:
                del all_recipes[title]
                return "Successfully deleted"
            except KeyError:
                return "Recipe does not exist"
        return "Please fill in all fields"
