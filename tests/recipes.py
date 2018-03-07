"""Handle data on recipes
Created: 2018
Author: Lenny
"""

recipes = {}


class Recipe(object):
    """Contain recipe creation, update and delete methods"""


    def create(self, title='', category='', description=''):
        """create a new recipe"""
        global recipes
        if title != '' and category != '' and description != '':
            recipes[title] = [title, category, description]
            return "Recipe created succesfully"
        return "Please fill in all fields"
    
    def update(self, title='', category='', description=''):
        """update an existing recipe"""
        global recipes
        if title != '' and category != '' and description != '':
            recipes[title] = [title, category, description]
            return "Sucessfully updated"
        return "Please fill in all fields"
    
    def delete(self, title='', category='', description=''):
        """delete an existing recipe"""
        global recipes
        if title != '' and category != '' and description != '':
            try:
                del recipes[title]
                return "Successfully deleted"
            except KeyError:
                return "Recipe does not exist"
        return "Please fill in all fields"
