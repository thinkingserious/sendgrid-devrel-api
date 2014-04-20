def create_app():
    from flask import Flask
    from .api_1_0 import api_blueprint as api_1_0_blueprint
    from .api_1_0 import api
    app = Flask(__name__)
    app.register_blueprint(api_1_0_blueprint)
    api.init_app(app)
    return app