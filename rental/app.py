from flask import Flask
from rental.ext import config

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()