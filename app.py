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
    from routes.cliente import bp as cliente_bp
    from routes.proveedor import bp as proveedor_bp
    from routes.grupo import bp as grupo_bp
    from routes.producto import bp as producto_bp
    from routes.maquina import bp as maquina_bp
    from routes.operario import bp as operario_bp
    from routes.impresion import bp as impresion_bp
    from routes.encuadernacion import bp as encuadernacion_bp
    from routes.fotomecanica import bp as fotomecanica_bp
    from routes.guiadespacho import bp as guiadespacho_bp
    from routes.factura import bp as factura_bp
    from routes.notacredito import bp as notacredito_bp
    from routes.documentonulo import bp as documentonulo_bp

    app.register_blueprint(login_bp, url_prefix='/login')
    app.register_blueprint(principal_bp, url_prefix='/')
    app.register_blueprint(banco_bp, url_prefix='/banco')
    app.register_blueprint(cliente_bp, url_prefix='/cliente')
    app.register_blueprint(proveedor_bp, url_prefix='/proveedor')
    app.register_blueprint(grupo_bp, url_prefix='/grupo')
    app.register_blueprint(producto_bp, url_prefix='/producto')
    app.register_blueprint(maquina_bp, url_prefix='/maquina')
    app.register_blueprint(operario_bp, url_prefix='/operario')
    app.register_blueprint(impresion_bp, url_prefix='/impresion')
    app.register_blueprint(encuadernacion_bp, url_prefix='/encuadernacion')
    app.register_blueprint(fotomecanica_bp, url_prefix='/fotomecanica')
    app.register_blueprint(guiadespacho_bp,url_prefix='/guiadespacho')
    app.register_blueprint(factura_bp,url_prefix='/factura')
    app.register_blueprint(notacredito_bp,url_prefix='/notacredito')
    app.register_blueprint(documentonulo_bp,url_prefix='/documentonulo')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)