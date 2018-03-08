"""Handles the views of my MVC design pattern"""

from flask import render_template, request, redirect, session, url_for
from app import app

@app.route('/')
def home():
    """render the home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """render the about page"""
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """render the registration form and handles user input for registration"""
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        session['confirm_password'] = request.form['confirmPassword']
        return redirect(url_for('recipes'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """render the login form and handle user input for logging in"""
    if request.method == 'POST':
        if 'email' in session:
            return redirect(url_for('recipes'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    """ log out a user by clearing the data saved in sessions"""
    session.pop('username', None)
    session.pop('email', None)
    session.pop('password', None)
    session.pop('confirm_password', None)

    return redirect(url_for('home'))


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    """render the add_recipe form and handle the data for a new recipe"""

    if request.method == 'POST':

        session['title'] = request.form['title']
        session['category'] = request.form['category']
        session['description'] = request.form['description']

        return redirect(url_for('recipes'))

    return render_template('add_recipe.html')


@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    """render the recipes page and display saved recipes"""

    if 'title' in session:
        title = session['title']
        category = session['category']
        description = session['description']

        return render_template('recipes.html', title=title, category=category,
                               description=description)

    return render_template('recipes.html')

@app.route('/delete_recipe')
def delete_recipe():
    """delete a recipe by clearing the data saved in sessions"""
    session.pop('title', None)
    session.pop('category', None)
    session.pop('description', None)

    return redirect(url_for('recipes'))

@app.route('/edit_recipe', methods=['GET', 'POST'])
def edit_recipe():
    """edit an already saved recipe"""

    if 'title' in session:
        title = session['title']
        category = session['category']
        description = session['description']

        return render_template('add_recipe.html', title=title, category=category,
                               description=description)

    return redirect(url_for('add_recipe'))
