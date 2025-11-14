from flask import Blueprint, render_template, request, redirect, url_for
from models import db
from models.proveedor import Proveedor

bp = Blueprint('proveedor', __name__, template_folder='../templates/proveedor')

@bp.route('/')
def index():
    proveedores = Proveedor.query.all()
    return render_template('proveedor/index.html', proveedores=proveedores)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nuevo_proveedor = Proveedor(
            rut=request.form['rut'],
            razon_social=request.form['razon_social'],
            giro=request.form.get('giro'),
            direccion=request.form.get('direccion'),
            ciudad=request.form.get('ciudad'),
            telefono=request.form.get('telefono'),
            fax=request.form.get('fax'),
            observacion1=request.form.get('observacion1'),
            observacion2=request.form.get('observacion2'),
            debi=request.form.get('debi') or 0,
            habi=request.form.get('habi') or 0,
            debe=request.form.get('debe') or 0,
            habe=request.form.get('habe') or 0,
            saldo=request.form.get('saldo') or 0
        )
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return redirect(url_for('proveedor.index'))
    return render_template('proveedor/form.html', proveedor=None)

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    proveedor = Proveedor.query.get_or_404(id)
    if request.method == 'POST':
        proveedor.rut = request.form['rut']
        proveedor.razon_social = request.form['razon_social']
        proveedor.giro = request.form.get('giro')
        proveedor.direccion = request.form.get('direccion')
        proveedor.ciudad = request.form.get('ciudad')
        proveedor.telefono = request.form.get('telefono')
        proveedor.fax = request.form.get('fax')
        proveedor.observacion1 = request.form.get('observacion1')
        proveedor.observacion2 = request.form.get('observacion2')
        proveedor.debi = request.form.get('debi') or 0
        proveedor.habi = request.form.get('habi') or 0
        proveedor.debe = request.form.get('debe') or 0
        proveedor.habe = request.form.get('habe') or 0
        proveedor.saldo = request.form.get('saldo') or 0
        db.session.commit()
        return redirect(url_for('proveedor.index'))
    return render_template('proveedor/form.html', proveedor=proveedor)

@bp.route('/delete/<int:id>')
def delete(id):
    proveedor = Proveedor.query.get_or_404(id)
    db.session.delete(proveedor)
    db.session.commit()
    return redirect(url_for('proveedor.index'))
