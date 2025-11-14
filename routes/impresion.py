from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.impresion import Impresion

bp = Blueprint('impresion', __name__, template_folder='../templates/impresion')

@bp.route('/')
def index():
    impresiones = Impresion.query.all()
    return render_template('impresion/index.html', impresiones=impresiones)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nueva = Impresion(
            codigo=request.form['codigo'],
            descripcion=request.form['descripcion'],
            valorpormil=int(request.form['valorpormil'])
        )
        db.session.add(nueva)
        db.session.commit()
        flash('✅ Impresión agregada correctamente', 'success')
        return redirect(url_for('impresion.index'))
    
    return render_template('impresion/form.html', accion='Agregar')

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    impresion = Impresion.query.get_or_404(id)
    if request.method == 'POST':
        impresion.codigo = request.form['codigo']
        impresion.descripcion = request.form['descripcion']
        impresion.valorpormil = int(request.form['valorpormil'])
        db.session.commit()
        flash('✏️ Impresión actualizada correctamente', 'success')
        return redirect(url_for('impresion.index'))
    
    return render_template('impresion/form.html', impresion=impresion, accion='Editar')

@bp.route('/delete/<int:id>')
def delete(id):
    impresion = Impresion.query.get_or_404(id)
    db.session.delete(impresion)
    db.session.commit()
    flash('🗑️ Impresión eliminada correctamente', 'danger')
    return redirect(url_for('impresion.index'))
