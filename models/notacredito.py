from app import db
from datetime import datetime

class NotaCredito(db.Model):
    __tablename__ = "notacredito"

    id = db.Column(db.Integer, primary_key=True)
    folio = db.Column(db.String(50), nullable=False)
    rut_cliente = db.Column(db.String(50), nullable=False)
    factura = db.Column(db.String(50), nullable=False)
    neto = db.Column(db.Integer, nullable=False)
    iva = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    memoria = db.Column(db.String(255))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<NotaCredito {self.folio}>"
