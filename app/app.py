"""contains the backend logic of the flask app"""

from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = "63jHZ6MIur"

@app.route('/')
def home():
    """renders the home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """renders the about page"""
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """renders the registration form and handles user input for registration"""
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        session['confirm_password'] = request.form['confirmPassword']
        return redirect(url_for('recipes'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """renders the login form and handles user input for logging in"""
    if request.method == 'POST':
        if 'email' in session:
            return redirect(url_for('recipes'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    """ logs out a user by clearing the data saved in session"""
    session.pop('username', None)
    session.pop('email', None)
    session.pop('password', None)
    session.pop('confirm_password', None)

    return redirect(url_for('home'))


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    """renders the add_recipe form and handles the data for a new recipe"""

    if request.method == 'POST':

        session['title'] = request.form['title']
        session['category'] = request.form['category']
        session['description'] = request.form['description']

        return redirect(url_for('recipes'))

    return render_template('add_recipe.html')


@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    """renders the recipes page displaying saved recipes"""

    if 'title' in session:
        title = session['title']
        category = session['category']
        description = session['description']

        return render_template('recipes.html', title=title, category=category,
                               description=description)

    return render_template('recipes.html')

@app.route('/delete_recipe')
def delete_recipe():
    """deletes a recipe by clearing the data saved in session"""
    session.pop('title', None)
    session.pop('category', None)
    session.pop('description', None)

    return redirect(url_for('recipes'))

@app.route('/edit_recipe', methods=['GET', 'POST'])
def edit_recipe():
    """edits an already saved recipe"""

    if 'title' in session:
        title = session['title']
        category = session['category']
        description = session['description']

        return render_template('add_recipe.html', title=title, category=category,
                               description=description)

    return redirect(url_for('add_recipe'))


if __name__ == '__main__':
    app.run(debug=True)
