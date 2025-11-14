from app import db
from datetime import datetime

class Factura(db.Model):
    __tablename__ = 'factura'

    id = db.Column(db.Integer, primary_key=True)
    folio = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.Date, default=datetime.utcnow)

    rutcliente = db.Column(db.String(50), nullable=False)
    guia1 = db.Column(db.String(50), default='')
    guia2 = db.Column(db.String(50), default='')
    guia3 = db.Column(db.String(50), default='')
    guia4 = db.Column(db.String(50), default='')
    guia5 = db.Column(db.String(50), default='')

    ordentrabajo = db.Column(db.String(100), default='')
    fechavencimiento = db.Column(db.String(20), default='')
    tipocredito = db.Column(db.Integer, default=0)
    neto = db.Column(db.Integer, default=0)
    iva = db.Column(db.Integer, default=0)
    total = db.Column(db.Integer, default=0)
    habe = db.Column(db.Integer, default=0)
    notacredito = db.Column(db.Integer, default=0)

    memo = db.Column(db.String(255), default='')
    tipo = db.Column(db.String(50), default='')

    ot01 = db.Column(db.String(50), default='')
    ot02 = db.Column(db.String(50), default='')
    ot03 = db.Column(db.String(50), default='')
    ot04 = db.Column(db.String(50), default='')
    ot05 = db.Column(db.String(50), default='')

    op01 = db.Column(db.String(50), default='')
    op02 = db.Column(db.String(50), default='')
    op03 = db.Column(db.String(50), default='')
    op04 = db.Column(db.String(50), default='')
    op05 = db.Column(db.String(50), default='')

    peli = db.Column(db.String(100), default='')
    plan = db.Column(db.String(100), default='')

    def __repr__(self):
        return f'<Factura {self.folio}>'
