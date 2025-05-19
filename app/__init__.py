from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    from .api.users import api_users
    app.register_blueprint(api_users)

    return app
