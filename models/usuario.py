from models import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    clave = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(100))
