from app import app

# Begin homepage.  / or /index TBD
@app.route('/index')
@app.route('/')
def index():
    greet = "<h1>Welcome!</h1>\n" # What about templates?  We'll do them later
    message = greet + "<h2>I'm Accountability.  What can I help with?</h2>\n"

    return message

# Dynamic shell for user pages
@app.route('/user/<name>')
def user(name):
    message = "<h1> Hi there, %s!</h1>" #Again, do the h1 tags in templates
    return message
