import os

from flask import Flask

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    
    @app.route('/hello')
    def hello():
        return 'Hello, there!'
    
    from . import user
    app.register_blueprint(user.bp)
    
    from . import todo
    app.register_blueprint(todo.bp)
    
    return app