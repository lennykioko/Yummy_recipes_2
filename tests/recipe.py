"""contains logic to handle user's recipes"""


class Recipe(object):
    """class with method allowing for user to create new recipe"""


    def __init__(self, title=None, category=None, description=None):
        """initalizes variables to be used in the class"""
        self.title = title
        self.category = category
        self.description = description

    def new_recipe(self, title, category, description):
        """handles logic to verify data before creating a new recipe"""
        if title != "" and category != "" and description != "":

            global my_recipes

            my_recipes = {}
            my_recipes[title] = {}
            my_recipes[title]['title'] = title
            my_recipes[title]['category'] = category
            my_recipes[title]['description'] = description

            return 'Successfully created new recipe'

        return 'Kindly fill in all fields'
