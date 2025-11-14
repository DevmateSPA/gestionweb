from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.operario import Operario

bp = Blueprint('operario', __name__, template_folder='../templates/operario')

@bp.route('/')
def index():
    operarios = Operario.query.all()
    return render_template('operario/index.html', operarios=operarios)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nuevo = Operario(
            codigo=request.form['codigo'],
            nombre=request.form['nombre']
        )
        db.session.add(nuevo)
        db.session.commit()
        flash('✅ Operario agregado correctamente', 'success')
        return redirect(url_for('operario.index'))
    
    return render_template('operario/form.html', accion='Agregar')

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    operario = Operario.query.get_or_404(id)
    if request.method == 'POST':
        operario.codigo = request.form['codigo']
        operario.nombre = request.form['nombre']
        db.session.commit()
        flash('✏️ Operario actualizado correctamente', 'success')
        return redirect(url_for('operario.index'))
    
    return render_template('operario/form.html', operario=operario, accion='Editar')

@bp.route('/delete/<int:id>')
def delete(id):
    operario = Operario.query.get_or_404(id)
    db.session.delete(operario)
    db.session.commit()
    flash('🗑️ Operario eliminado correctamente', 'danger')
    return redirect(url_for('operario.index'))
