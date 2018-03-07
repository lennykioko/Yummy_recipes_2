"""contains logic to handle user's recipes"""


class Recipe(object):
    """class with method allowing for user to create new recipe"""


    def __init__(self, title=None, category=None, description=None):
        """initalizes variables to be used in the class"""
        self.title = title # pragma: no cover
        self.category = category # pragma: no cover
        self.description = description # pragma: no cover

    def new_recipe(self, title, category, description):
        """handles logic to verify data before creating a new recipe"""
        if title != "" and category != "" and description != "": # pragma: no cover

            global my_recipes # pragma: no cover

            my_recipes = {} # pragma: no cover
            my_recipes[title] = {} # pragma: no cover
            my_recipes[title]['title'] = title # pragma: no cover
            my_recipes[title]['category'] = category # pragma: no cover
            my_recipes[title]['description'] = description # pragma: no cover

            return 'Successfully created new recipe'
        return 'Kindly fill in all fields'
