from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.maquina import Maquina

bp = Blueprint('maquina', __name__, template_folder='../templates/maquina')

@bp.route('/')
def index():
    maquinas = Maquina.query.all()
    return render_template('maquina/index.html', maquinas=maquinas)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nueva = Maquina(
            codigo=request.form['codigo'],
            descripcion=request.form['descripcion']
        )
        db.session.add(nueva)
        db.session.commit()
        flash('✅ Máquina creada correctamente', 'success')
        return redirect(url_for('maquina.index'))

    return render_template('maquina/form.html', accion='Crear')

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    maquina = Maquina.query.get_or_404(id)

    if request.method == 'POST':
        maquina.codigo = request.form['codigo']
        maquina.descripcion = request.form['descripcion']
        db.session.commit()
        flash('✏️ Máquina actualizada correctamente', 'success')
        return redirect(url_for('maquina.index'))

    return render_template('maquina/form.html', maquina=maquina, accion='Editar')

@bp.route('/delete/<int:id>')
def delete(id):
    maquina = Maquina.query.get_or_404(id)
    db.session.delete(maquina)
    db.session.commit()
    flash('🗑️ Máquina eliminada correctamente', 'danger')
    return redirect(url_for('maquina.index'))
