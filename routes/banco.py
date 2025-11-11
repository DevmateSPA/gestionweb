from flask import Blueprint, render_template, request, redirect, url_for
from models import db
from models.banco import Banco

bp = Blueprint('banco', __name__, template_folder='../templates/banco')

@bp.route('/')
def index():
    bancos = Banco.query.all()
    return render_template('banco/index.html', bancos=bancos)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nuevo_banco = Banco(
            codigo=request.form['codigo'],
            nombre=request.form['nombre'],
            direccion=request.form['direccion']
        )
        db.session.add(nuevo_banco)
        db.session.commit()
        return redirect(url_for('banco.index'))
    return render_template('banco/agregar.html')

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    banco = Banco.query.get_or_404(id)
    if request.method == 'POST':
        banco.codigo = request.form['codigo']
        banco.nombre = request.form['nombre']
        banco.direccion = request.form['direccion']
        db.session.commit()
        return redirect(url_for('banco.index'))
    return render_template('banco/modificar.html', banco=banco)

@bp.route('/delete/<int:id>')
def delete(id):
    banco = Banco.query.get_or_404(id)
    db.session.delete(banco)
    db.session.commit()
    return redirect(url_for('banco.index'))