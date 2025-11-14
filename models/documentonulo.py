from app import db

class DocumentoNulo(db.Model):
    __tablename__ = "documento_nulo"

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)
    folio = db.Column(db.String(50), nullable=False)
    glosa = db.Column(db.String(255), nullable=True)
    fecha = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<DocumentoNulo {self.folio}>"
