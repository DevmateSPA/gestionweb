from . import db

class Banco(db.Model):
    __tablename__ = 'banco'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Banco {self.nombre}>'