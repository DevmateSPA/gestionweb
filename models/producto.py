from app import db

class Producto(db.Model):
    __tablename__ = 'producto'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    grupo = db.Column(db.Integer, nullable=False)
    stmi = db.Column(db.Integer, nullable=False)  # stock mínimo
    papel = db.Column(db.Integer, nullable=False)
    dime = db.Column(db.Integer, nullable=False)  # dimensiones
    enin = db.Column(db.Integer, default=0)
    punp = db.Column(db.Integer, default=0)
    sain = db.Column(db.Integer, default=0)
    saldo = db.Column(db.Integer, default=0)
    salida = db.Column(db.Integer, default=0)
    entrada = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Producto {self.codigo} - {self.descripcion}>'
