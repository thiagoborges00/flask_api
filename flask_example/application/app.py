from flask import Flask
from application.config import configure

#só cria o app
def create_app():
    app = Flask(__name__)
    configure(app)
    return app



#execute  FLASK_ENV=development flask run
## ou pode colocar as variveis em um .env
#  