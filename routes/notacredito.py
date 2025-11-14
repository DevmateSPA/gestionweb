from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from datetime import datetime
from models.notacredito import NotaCredito

bp = Blueprint("notacredito", __name__, url_prefix="../templates/notacredito")

@bp.route("/")
def index():
    notas = NotaCredito.query.all()
    return render_template("notacredito/index.html", notas=notas)

@bp.route("/create", methods=["GET", "POST"])
def create():
    nota = NotaCredito(
        folio=request.form['folio'],
        rut_cliente=request.form['rut_cliente'],
        factura=request.form['factura'],
        neto=int(request.form.get('neto', 0)),
        iva=int(request.form.get('iva', 0)),
        total=int(request.form.get('total', 0)),
        memoria=request.form['memoria'],
        fecha=datetime.strptime(request.form['fecha'], '%Y-%m-%d'),
    )
    db.session.add(nota)
    db.session.commit()
    flash("Nota de crédito creada correctamente", "success")
    return redirect(url_for("notacredito.index"))

@bp.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    notacredito = NotaCredito.query.get_or_404(id)
    notacredito.folio = request.form['folio']
    notacredito.fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d')
    notacredito.rut_cliente = request.form['rut_cliente']
    notacredito.neto = int(request.form.get('neto', 0))
    notacredito.iva = int(request.form.get('iva', 0))
    notacredito.total = int(request.form.get('total', 0))
    notacredito.memoria = int(request.form.get('memoria', 0))

    db.session.commit()
    flash("Nota de crédito actualizada", "success")
    return redirect(url_for("notacredito.index"))

@bp.route("/delete/<int:id>")
def delete(id):
    nota = NotaCredito.query.get_or_404(id)
    db.session.delete(nota)
    db.session.commit()
    flash("Nota de crédito eliminada", "danger")
    return redirect(url_for("notacredito.index"))
