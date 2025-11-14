from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.guiadespacho import GuiaDespacho
from datetime import datetime

bp = Blueprint('guiadespacho', __name__, url_prefix='/../templates/guiadespacho')

@bp.route('/')
def index():
    guias = GuiaDespacho.query.all()
    return render_template('guiadespacho/index.html', guias=guias)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        folio = request.form['folio']
        rut_cliente = request.form['rut_cliente']
        orden_trabajo = request.form['orden_trabajo']
        memo = request.form.get('memo', '')
        factura = request.form.get('factura', '')
        fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d')

        nueva_guia = GuiaDespacho(folio, rut_cliente, orden_trabajo, memo, factura, fecha)
        db.session.add(nueva_guia)
        db.session.commit()
        flash('Guía creada con éxito', 'success')
        return redirect(url_for('guia.index'))
    
    return render_template('guiadespacho/create.html')

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    guia = GuiaDespacho.query.get_or_404(id)
    if request.method == 'POST':
        guia.folio = request.form['folio']
        guia.rut_cliente = request.form['rut_cliente']
        guia.orden_trabajo = request.form['orden_trabajo']
        guia.memo = request.form.get('memo', '')
        guia.factura = request.form.get('factura', '')
        guia.fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d')
        db.session.commit()
        flash('Guía actualizada correctamente', 'success')
        return redirect(url_for('guia.index'))
    return render_template('guiadespacho/update.html', guia=guia)

@bp.route('/delete/<int:id>')
def delete(id):
    guia = GuiaDespacho.query.get_or_404(id)
    db.session.delete(guia)
    db.session.commit()
    flash('Guía eliminada correctamente', 'success')
    return redirect(url_for('guia.index'))
