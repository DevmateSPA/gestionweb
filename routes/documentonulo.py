from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from datetime import datetime
from models.documentonulo import DocumentoNulo

bp = Blueprint("documentonulo", __name__, url_prefix="/documentonulo")

@bp.route("/")
def index():
    documentos = DocumentoNulo.query.all()
    return render_template("documentonulo/index.html", documentos=documentos)

@bp.route("/create", methods=["GET", "POST"])
def create():
    doc = DocumentoNulo(
        tipo=request.form['tipo'],
        folio=request.form['folio'],
        glosa=request.form['glosa'],
        fecha=datetime.strptime(request.form['fecha'], '%Y-%m-%d')
    )
    db.session.add(doc)
    db.session.commit()
    flash("Documento nulo creado correctamente", "success")
    return redirect(url_for("documentonulo.index"))

@bp.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    doc = DocumentoNulo.query.get_or_404(id)
    doc.tipo=request.form['tipo']
    doc.folio=request.form['folio']
    doc.glosa=request.form['glosa']
    doc.fecha=datetime.strptime(request.form['fecha'], '%Y-%m-%d')
    db.session.commit()
    flash("Documento nulo actualizado correctamente", "success")
    return redirect(url_for("documentonulo.index"))

@bp.route("/delete/<int:id>")
def delete(id):
    doc = DocumentoNulo.query.get_or_404(id)
    db.session.delete(doc)
    db.session.commit()
    flash("Documento nulo eliminado", "danger")
    return redirect(url_for("documentonulo.index"))
