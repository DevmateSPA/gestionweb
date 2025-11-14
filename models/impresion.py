from app import db

class Impresion(db.Model):
    __tablename__ = 'impresion'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    valorpormil = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f'<Impresion {self.codigo} - {self.descripcion}>'
