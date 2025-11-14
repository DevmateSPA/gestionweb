from app import db

class GuiaDespacho(db.Model):
    __tablename__ = 'guiadespacho'

    id = db.Column(db.Integer, primary_key=True)
    folio = db.Column(db.String(100), nullable=False, default='')
    rut_cliente = db.Column(db.String(50), nullable=False, default='')
    orden_trabajo = db.Column(db.String(100), nullable=False, default='')
    memo = db.Column(db.String(255), default='')
    factura = db.Column(db.String(100), default='')
    fecha = db.Column(db.DateTime, nullable=False)

    def __init__(self, folio, rut_cliente, orden_trabajo, memo, factura, fecha):
        self.folio = folio
        self.rut_cliente = rut_cliente
        self.orden_trabajo = orden_trabajo
        self.memo = memo
        self.factura = factura
        self.fecha = fecha
