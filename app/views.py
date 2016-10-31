from flask import render_template
from app import app
from datetime import datetime
# TODO: Create forms classes in a separate file.  Then import them here

# Begin homepage.  / or /index TBD
@app.route('/index')
@app.route('/')
def index():
    greet = "Welcome!\n" # What about templates?  We'll do them later
    message = greet + "I'm Accountability.  What can I help you with?\n"

    return render_template('index.html', current_time=datetime.utcnow())

# Dynamic shell for user pages
@app.route('/user/<name>')
def user(name):
    message = "<h1> Hi there, %s!</h1>" #Again, do the h1 tags in templates
    return render_template('user.html', name = name)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    my_name = None

    login = LoginForm()
