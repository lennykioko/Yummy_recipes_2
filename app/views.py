"""Handles the view function of my MVC design pattern"""

from flask import render_template, request, redirect, session, url_for
from app import app
from users import User, all_users
from recipes import Recipe, all_recipes

user = User()
recipe = Recipe()

@app.route('/')
@app.route('/index')
def index():
    """render the home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """render the about page"""
    return render_template('about.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """render the registration form and handles user input for registration"""
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        message = user.signup(email, username, password, confirm_password)
        if message == "successful account creation":
            session['email'] = email
            session['password'] = password
            return redirect(url_for('recipes'))
        return render_template('signup.html', message=message)

    return render_template('signup.html')


@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    """render the forgot password form and handles user input for acount recovery"""
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        message = user.recover(email, username, password, confirm_password)
        if message == "Sucessfully recovered account":
            session['email'] = email
            session['password'] = password
            return redirect(url_for('recipes'))
        return render_template('forgot.html', message=message)

    return render_template('forgot.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """render the login form and handle user input for logging in"""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        message = user.login(email, password)
        if message == "succcessful login":
            session['email'] = email
            session['password'] = password
            return redirect(url_for('recipes'))
        return render_template('login.html', message=message)
        

    return render_template('login.html')


@app.route('/logout')
def logout():
    """ log out a user by clearing the data saved in session"""
    session.pop('email', None)
    session.pop('password', None)
    return redirect(url_for('index'))


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    """render the add_recipe form and handle the data for a new recipe"""

    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        description = request.form['description']

        message = recipe.create(title, category, description)
        if message == "Recipe created succesfully":
            return redirect(url_for('recipes'))
        return render_template('add_recipe.html', message=message)

    return render_template('add_recipe.html')


@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    """render the recipes page and display saved recipes"""
    return render_template('recipes.html', all_recipes=all_recipes)


@app.route('/edit_recipe/<title>/<category>/<description>', methods=['GET', 'POST'])
def edit_recipe(title='', category='', description=''):
    """edit an already saved recipe"""
    recipe.delete(title)
    context = {"title" : title, "category" : category, "description" : description}
    return render_template('add_recipe.html', **context)

@app.route('/delete_recipe/<title>')
def delete_recipe(title=''):
    recipe.delete(title)
    return redirect(url_for('recipes'))
