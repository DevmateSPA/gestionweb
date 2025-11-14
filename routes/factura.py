from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from app import db
from models.factura import Factura

bp = Blueprint('factura', __name__, template_folder='../templates/factura')

@bp.route('/')
def index():
    facturas = Factura.query.order_by(Factura.fecha.desc()).all()
    return render_template('factura/index.html', facturas=facturas)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nueva = Factura(
            folio=request.form['folio'],
            fecha=datetime.strptime(request.form['fecha'], '%Y-%m-%d'),
            rutcliente=request.form['rut_cliente'],
            guia1=request.form.get('guia1', ''),
            ordentrabajo=request.form.get('orden_trabajo', ''),
            fechavencimiento=request.form.get('fecha_vencimiento', ''),
            tipocredito=int(request.form.get('tipo_credito', 0)),
            neto=int(request.form.get('neto', 0)),
            iva=int(request.form.get('iva', 0)),
            total=int(request.form.get('total', 0)),
            habe=int(request.form.get('habe', 0)),
            notacredito=int(request.form.get('notacredito', 0))
        )
        db.session.add(nueva)
        db.session.commit()
        flash('✅ Factura creada correctamente', 'success')
        return redirect(url_for('factura.index'))

    return render_template('factura/form.html', accion='Crear')

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    factura = Factura.query.get_or_404(id)

    if request.method == 'POST':
        factura.folio = request.form['folio']
        factura.fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d')
        factura.rut_cliente = request.form['rut_cliente']
        factura.guia1 = request.form.get('guia1', '')
        factura.orden_trabajo = request.form.get('orden_trabajo', '')
        factura.fecha_vencimiento = request.form.get('fecha_vencimiento', '')
        factura.tipo_credito = int(request.form.get('tipo_credito', 0))
        factura.neto = int(request.form.get('neto', 0))
        factura.iva = int(request.form.get('iva', 0))
        factura.total = int(request.form.get('total', 0))
        factura.habe = int(request.form.get('habe', 0))
        factura.notacredito = int(request.form.get('notacredito', 0))

        db.session.commit()
        flash('✏️ Factura actualizada correctamente', 'success')
        return redirect(url_for('factura.index'))

    return render_template('factura/form.html', factura=factura, accion='Editar')

@bp.route('/delete/<int:id>')
def delete(id):
    factura = Factura.query.get_or_404(id)
    db.session.delete(factura)
    db.session.commit()
    flash('🗑️ Factura eliminada correctamente', 'danger')
    return redirect(url_for('factura.index'))
