from app import db

class Operario(db.Model):
    __tablename__ = 'operario'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<Operario {self.codigo} - {self.nombre}>'
