from flask import Flask
from flask_bootstrap import Bootstrap
# from .frontend import frontend
# from .nav import nav

app = Flask(__name__)
#app.config.from_object('config')
from app import views
Bootstrap(app)
# app.register_blueprint(frontend)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

# nav.init_app(app)
