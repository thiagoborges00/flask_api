from flask_pymongo import PyMongo

mongo = PyMongo()# modo não inicializavel

def configure(app):
    mongo.init_app(app)
    
