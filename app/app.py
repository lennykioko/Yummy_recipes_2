from flask import Flask, render_template, request, redirect, session, url_for, g

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.before_request
def before_request():
    g.username = None
    g.email = None
    g.password = None
    g.confirm_password = None
    
    if 'username' in session:
        g.username = session['username']
        g.email = session['email']
        g.password = session['password']
        g.confirm_password = session['confirm_password']

    g.title = None
    g.category = None
    g.description = None

    if 'title' in session:
        g.title = session['title']
        g.category = session['category']
        g.description = session['description']



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session['username']  = request.form['username']
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        session['confirm_password'] = request.form['confirmPassword']
        return redirect(url_for('recipes'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == g.email:
            if password == g.password:
                return redirect(url_for('recipes'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    session.pop('password', None)
    session.pop('confirm_password', None)

    return redirect(url_for('home'))


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():

    if request.method == 'POST':

        session['title']  = request.form['title']
        session['category']  = request.form['category']
        session['description']  = request.form['description']

        return redirect(url_for('recipes'))

    return render_template('add_recipe.html')


@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    title = g.title
    category = g.category
    description = g.description
    
    return render_template('recipes.html', title=title, category=category, description=description)

@app.route('/delete_recipe')
def delete_recipe():
    session.pop('title', None)
    session.pop('category', None)
    session.pop('description', None)

    return redirect(url_for('recipes'))

@app.route('/edit_recipe', methods=['GET', 'POST'])
def edit_recipe():
    title = g.title
    category = g.category
    description = g.description

    return render_template('add_recipe.html', title=title, category=category, description=description)






if __name__ == '__main__':
    app.run()