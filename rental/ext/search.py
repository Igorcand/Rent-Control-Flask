from flask_msearch import Search

def init_app(app):
    search = Search()
    search.init_app(app)