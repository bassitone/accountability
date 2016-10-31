#!/Users/charles/Documents/Code/accountability/flask/bin/python3
from app import app

app.run(debug = True)
app.config.from_object('config')
