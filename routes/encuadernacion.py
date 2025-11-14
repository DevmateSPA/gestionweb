from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.encuadernacion import Encuadernacion

bp = Blueprint('encuadernacion', __name__, template_folder='../templates/encuadernacion')

@bp.route('/')
def index():
    encuadernaciones = Encuadernacion.query.all()
    return render_template('encuadernacion/index.html', encuadernaciones=encuadernaciones)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nueva = Encuadernacion(
            codigo=request.form['codigo'],
            descripcion=request.form['descripcion'],
            valorpormil=int(request.form['valorpormil'])
        )
        db.session.add(nueva)
        db.session.commit()
        flash('✅ Encuadernación agregada correctamente', 'success')
        return redirect(url_for('encuadernacion.index'))
    
    return render_template('encuadernacion/form.html', accion='Agregar')

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    encuadernacion = Encuadernacion.query.get_or_404(id)
    if request.method == 'POST':
        encuadernacion.codigo = request.form['codigo']
        encuadernacion.descripcion = request.form['descripcion']
        encuadernacion.valorpormil = int(request.form['valorpormil'])
        db.session.commit()
        flash('✏️ Encuadernación actualizada correctamente', 'success')
        return redirect(url_for('encuadernacion.index'))
    
    return render_template('encuadernacion/form.html', encuadernacion=encuadernacion, accion='Editar')

@bp.route('/delete/<int:id>')
def delete(id):
    encuadernacion = Encuadernacion.query.get_or_404(id)
    db.session.delete(encuadernacion)
    db.session.commit()
    flash('🗑️ Encuadernación eliminada correctamente', 'danger')
    return redirect(url_for('encuadernacion.index'))
