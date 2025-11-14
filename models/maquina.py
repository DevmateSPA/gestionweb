from app import db

class Maquina(db.Model):
    __tablename__ = 'maquina'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Maquina {self.codigo} - {self.descripcion}>'
