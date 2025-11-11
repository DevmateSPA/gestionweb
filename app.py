from flask import Flask
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from models import banco

    with app.app_context():
        db.create_all()

    from routes.login import bp as login_bp
    from routes.principal import bp as principal_bp
    from routes.banco import bp as banco_bp
    app.register_blueprint(login_bp, url_prefix='/login')
    app.register_blueprint(principal_bp, url_prefix='/')
    app.register_blueprint(banco_bp, url_prefix='/banco')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)