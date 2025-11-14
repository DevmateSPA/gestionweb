from . import db

class Cliente(db.Model):
    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(20), nullable=False)
    razon_social = db.Column(db.String(150), nullable=False)
    giro = db.Column(db.String(100), nullable=True)
    direccion = db.Column(db.String(200), nullable=True)
    ciudad = db.Column(db.String(100), nullable=True)
    telefono = db.Column(db.String(50), nullable=True)
    fax = db.Column(db.String(50), nullable=True)
    observaciones1 = db.Column(db.String(255), nullable=True)
    debi = db.Column(db.Integer, nullable=True)
    habi = db.Column(db.Integer, nullable=True)
    debe = db.Column(db.BigInteger, nullable=True)
    habe = db.Column(db.BigInteger, nullable=True)
    saldo = db.Column(db.BigInteger, nullable=True)


    def __repr__(self):
        return f'<Cliente {self.razon_social}>'
