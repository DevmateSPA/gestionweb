from flask import Blueprint, render_template, request, redirect, url_for
from models import db
from models.cliente import Cliente

bp = Blueprint('cliente', __name__, template_folder='../templates/cliente')

@bp.route('/')
def index():
    clientes = Cliente.query.all()
    return render_template('cliente/index.html', clientes=clientes)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nuevo_cliente = Cliente(
            rut=request.form['rut'],
            razon_social=request.form['razon_social'],
            giro=request.form.get('giro'),
            direccion=request.form.get('direccion'),
            ciudad=request.form.get('ciudad'),
            telefono=request.form.get('telefono'),
            fax=request.form.get('fax')
        )
        db.session.add(nuevo_cliente)
        db.session.commit()
        return redirect(url_for('cliente.index'))
    return render_template('cliente/form.html', cliente=None)

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    cliente = Cliente.query.get_or_404(id)
    if request.method == 'POST':
        cliente.rut = request.form['rut']
        cliente.razon_social = request.form['razon_social']
        cliente.giro = request.form.get('giro')
        cliente.direccion = request.form.get('direccion')
        cliente.ciudad = request.form.get('ciudad')
        cliente.telefono = request.form.get('telefono')
        cliente.fax = request.form.get('fax')
        db.session.commit()
        return redirect(url_for('cliente.index'))
    return render_template('cliente/form.html', cliente=cliente)

@bp.route('/delete/<int:id>')
def delete(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('cliente.index'))
